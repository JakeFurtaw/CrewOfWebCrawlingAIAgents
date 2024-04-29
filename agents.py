from crewai import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool, FileReadTool, DirectoryReadTool

search_tool = WebsiteSearchTool()
serper_tool = SerperDevTool()
file_tool = FileReadTool()
directory_tool = DirectoryReadTool()

# Define the agents that will be used in the project
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

    Get_example_data = Agent(
        name = "Data Analyst",
        role = "Data Analyst",
        backstory = """You are an agent that specializes in reading files and directories to get example data that can be used to test the project.""",
        goal="To read files and directories to get example data that can be used to test the project.",
        verbose = True,
        tools = [file_tool, directory_tool],
        allow_delegation = False,
    )

    Question_crawler = Agent(
        name = "Webcrawler",
        role = "Senior Research Analyst",
        backstory = """You are an agent that specializes in crawling college websites and coming up with questions that new and existing students would 
        have about the school. You are tasked with crawling the website and coming up with questions that new and existing students would have about the school.
        """,
        goal="To crawl the provided website and come up with questions that students would have about the school.",
        verbose = True,
        tools = [serper_tool, search_tool],
        allow_delegation = False,
    )

    # Question_crawler2 = Agent(
    #     name = "Webcrawler2",
    #     role = "Senior Research Analyst",
    #     description = "Agent that is used to crawl a website and come up with questions that students would have about the school.",
    #     tools = ["webcrawler"],
    # )

    Answer_crawler = Agent(
        name = "Webcrawler",
        role = "Senior Research Analyst",
        backstory = """You are an agent that specializes in crawling college websites and coming up with answers to the questions that the question crawler 
        agent came up with.""",
        goal="To crawl the website and come up with answers to the questions that the question crawler agent came up with.",
        verbose = True,
        tools = [serper_tool, search_tool],
        allow_delegation = False,
    )

    # Answer_crawler2 = Agent(
    #     name = "Webcrawler2",
    #     role = "Senior Research Analyst",
    #     description = "Agent that is used to crawl a website and come up with questions that students would have about the school.",
    #     tools = ["webcrawler"],
    # )

