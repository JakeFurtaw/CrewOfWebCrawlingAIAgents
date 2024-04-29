from Crew import DataCrawlingCrew
from utils import get_website_link

def run():
    DataCrawlingCrew().crew().kickoff()

if __name__ == "__main__":
    run()