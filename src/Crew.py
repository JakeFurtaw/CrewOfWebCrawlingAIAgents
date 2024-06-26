from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from agents import Data_Loader, QA_Crawler, Data_Formatter, Manager
from tasks import Load_Example_Data, Load_Data, QA_Crawl, Format_Output_Data, Manager_Agents
from transformers import AutoModelForCausalLM, GenerationConfig
from dotenv import load_dotenv
import os
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
llm = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B", device_map = {"auto": device})

@CrewBase
class DataCrawlingCrew():
    def __init__(self) -> None:
        self.llm = llm
        self.generation_config = GenerationConfig(
            temperature=0.9,
            max_new_tokens=100)

    #Agents for the project.
    @agent
    def Data_Loader(self) -> Agent:
        return Agent(
            config = Data_Loader,
            llm = self.llm
        )
    @agent
    def QA_Crawler(self) -> Agent:
        return Agent(
            config = QA_Crawler,
            llm = self.llm
        )

    @agent
    def Data_Formatter(self) -> Agent:
        return Agent(
            config = Data_Formatter,
            llm = self.llm
        )
    
    #Tasks for the project.
    @task
    def Load_Example_Data(self) -> Task:
        return Task(
            config = Load_Example_Data,
            agent = self.Data_Loader()
        )
    @task
    def Load_Data(self) -> Task:
        return Task(
            config = Load_Data,
            agent = self.Data_Loader()
        )
    @task
    def QA_Crawl(self) -> Task:
        return Task(
            config = QA_Crawl,
            agent = self.QA_Crawler()
        )
    @task
    def Format_Output_Data(self) -> Task:
        return Task(
            config = Format_Output_Data,
            agent = self.Data_Formatter()
        )
    
    #Crew for the project.
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process= Process.sequential,
            verbose=2
        )