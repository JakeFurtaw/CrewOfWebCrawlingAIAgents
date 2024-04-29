from crew import WebCrawlingCrew

def run():
    website_link = input("Enter the website link: ")
    WebCrawlingCrew().crew().kickoff(website_link)

if __name__ == "__main__":
    run()