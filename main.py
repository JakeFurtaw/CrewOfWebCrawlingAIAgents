from crewai import Crew
from crewai.process import Process
from agents import Data_Loader, Questions_Crawler, Answer_Crawler, Data_Formatter, Manager
from tasks import Load_Example_Data, Question_Crawl, Answer_Crawl, Format_Output_Data, Manager_Agents
from dotenv import load_dotenv
import os

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

print("Starting the project...")
website_link = input("Enter the website link: ")

print("Creating the crew...")
crew = Crew(
    agents=[Data_Loader, Questions_Crawler, Answer_Crawler, Data_Formatter],
    tasks=[Load_Example_Data, Question_Crawl, Answer_Crawl, Format_Output_Data],
    process=Process.sequential,
    full_output=True,
    max_rpm=30,
    verbose=2
)

print("Kicking off project....")
results = crew.kickoff()