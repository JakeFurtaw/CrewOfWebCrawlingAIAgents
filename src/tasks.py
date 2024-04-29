from crewai import Task
from agents import Data_Loader, QA_Crawler, Data_Formatter, Manager

# Define the tasks that will be used in the project
class Tasks():
    # Manage_Agents = Task(
    #     description = "Manage the team of agents and provide tasks to each agent that will help further guide the project to sucess.",
    #     expected_output = "A well managed team and project.",
    #     agent = Manager
    # )

    Load_Example_Data = Task(
        description = "Read files and directories to get example data that can be used to provide the agents with the kind of data they are looking to complete the project.",
        expected_output = "Example data that can be used to help the llm find data on the website provided.",
        agent = Data_Loader
    )

    Load_Data = Task(
        description = "Load the data that was collected by the Question_Crawler so the Answer_Crawler can find the answers to the questions.",
        expected_output = "The data that was collected by the data loader agent.",
        agent = Data_Loader
    )
    
    QA_Crawl = Task(
        description = """Look through the provided text file to come up with questions and answers to those questions that students would have about the school.
        This could include gerneral information about the school, the programs offered, the campus life, different majors, food offered on campus, building and facility 
        locations, fraternity and sorority information, club information, teacher and faculty information.""",
        expected_output = "A list of questions that students would have about the school.",
        agent = QA_Crawler
    )

    Format_Output_Data = Task(
        description = """Format the data that was collected by the question and answer crawler agents so that it can be used to create a datset to finetune a model.
        Format it so that you have a Question on one line and the answer on the next line.
        """,
        expected_output = "Formatted data that can be used to create a chatbot.",
        agent = Data_Formatter
    )
