from crewai import Agent

class Agents():
    Question_crawler = Agent(
        name = "Webcrawler",
        role = "Senior Research Analyst",
        description = "An Agent that is used to crawl a website and come up with questions that students would have about the school.",
        tools = ["webcrawler"],
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
        description = "An Agent that is used to crawl a website and come up with questions that students would have about the school.",
        tools = ["webcrawler"],
    )

    # Answer_crawler2 = Agent(
    #     name = "Webcrawler2",
    #     role = "Senior Research Analyst",
    #     description = "Agent that is used to crawl a website and come up with questions that students would have about the school.",
    #     tools = ["webcrawler"],
    # )
