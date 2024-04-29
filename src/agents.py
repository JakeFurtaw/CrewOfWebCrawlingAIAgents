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
example_data = FileReadTool("./Data/examples.txt")
data = FileReadTool("./Data/cleaned_docs.txt")
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
        goal="To load the example data that the question and answer crawler agent will use to come up with questions that students would have about the school.",
        backstory = """You are an agent that specializes in loading data that the question and answer crawler agent will use to come up with questions that students would have about the school.
        You are tasked with loading the example data that the question and answer crawler agent will use to come up with questions that students would have about the school.
        """,
        verbose = True,
        tools = [example_data],
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
        tools = [data],
        allow_delegation = False,
    )

    # QA_Crawler2 = Agent(
    #     role = "Research Analyst",
    #     goal="To look through the provided file and come up with questions that students would have about the school.",
    #     backstory = """You are an agent that specializes in analying data and coming up with questions and answers to those questions that new and existing students would 
    #     have about the school. You are tasked with crawling the website and coming up with questions that new and existing students would have about the school.
    #     This could include but isnt limited to gerneral information about the school, the programs offered, the campus life, different majors, food offered on campus, building and facility 
    #     locations, fraternity and sorority information, club information, teacher and faculty information.
    #     """,
    #     verbose = True,
    #     tools = [data],
    #     allow_delegation = False,
    # )

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

