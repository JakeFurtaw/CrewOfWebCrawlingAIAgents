from Crew import WebCrawlingCrew
from utils import get_website_link

def run():
    website_link = get_website_link()
    WebCrawlingCrew().crew().kickoff(website_link=website_link)

if __name__ == "__main__":
    run()