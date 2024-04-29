from crew import WebCrawlingCrew

def run():
    website_link = input("Enter the website link: ")
    results = WebCrawlingCrew().crew().kickoff( website_link = website_link)
    file_name = "output.txt"
    with open(file_name, "w") as file:
        file.write(str(results))
    print(f"Results saved to {file_name}")

if __name__ == "__main__":
    run()