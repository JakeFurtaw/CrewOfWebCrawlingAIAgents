from crewai import Crew
from crewai.process import Process
from agents import Questions_crawler, Answer_crawler, Get_example_data, Manager
from tasks import Questions_crawler_task, Answer_crawler_task, Get_example_data , Manager_task

print("Starting the project...")
website_link = input("Enter the website link: ")

print("Creating the crew...")
crew = Crew(
    agents=[Questions_crawler, Answer_crawler, Get_example_data],
    tasks=[Questions_crawler_task, Answer_crawler_task, Get_example_data],
    process=Process.sequential,
    full_output=True,
    max_rpm=30,
    verbose=2
)

print("Kicking off project....")
results = crew.kickoff()
