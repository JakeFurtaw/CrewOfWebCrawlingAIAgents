from crewai import Agent
from crewai_tools import FileReadTool
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"
embedder = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

# ------Define the tools that will be used in the project---------
input_data = FileReadTool("./Data/input.txt")
questions_data = FileReadTool("./Data/questions.txt")
output_data = FileReadTool("./Data/output.txt")

# ------Define the agents that will be used in the project------
class Agents():
    # Manager = Agent(
    #     name = "Manager",
    #     role = "Project Manager",
    #     backstory = """You are an agent that specializes in crawling college websites and coming up with questions that new and existing students would 
    #     have about the school. You are tasked with crawling the website and coming up with questions that new and existing students would have about the school.
    #     """,
    #     description = "An Agent that manages the team and the project.",
    #     allow_delegation = True,
    #     tools = [],
    # )

    Data_Loader = Agent(
        role = "Data Loader",
        goal="""To use the file tool to read files to get example data that can be used to test the project. As well as use the file tool to load the data 
        that the other agents have generated to provide to the next agent.""",
        backstory = """You are an agent that specializes using the file tool and directory tool. Use these tools to read files and directories to get 
        the example data that can be used to help the other agents understand what to look for on the website.
        You will also use these tools to load the data that the other agents have found and saved to provide to the next agent.""",
        verbose = True,
        tools = [input_data],
        allow_delegation = False,
    )

    QA_Crawler = Agent(
        role = "Research Analyst",
        goal="To look through the provided file and come up with questions that students would have about the school.",
        backstory = """You are an agent that specializes in analying data and coming up with questions and answers to those questions that new and existing students would 
        have about the school. You are tasked with crawling the website and coming up with questions that new and existing students would have about the school.
        This could include but isnt limited to gerneral information about the school, the programs offered, the campus life, different majors, food offered on campus, building and facility 
        locations, fraternity and sorority information, club information, teacher and faculty information.
        """,
        verbose = True,
        tools = [questions_data],
        allow_delegation = False,
    )

    Data_Formatter = Agent(
        role = "Data Formatter",
        goal="To format the data that the question and answer crawler agent came up with in a way that is easy to read and understand.",
        backstory = """You are an agent that specializes in formatting data in a way that is easy to read and understand. You are tasked with formatting 
        the data that the question and answer crawler agent came up with in a way that is easy to read and understand for a human. 
        You are to export the data to a text file that can be read by a human.""",
        verbose = True,
        tools = [output_data],
        allow_delegation = False,
    )

