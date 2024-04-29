website_link = None

def get_website_link():
    global website_link
    if website_link is None:
        website_link = input("Enter the website link: ")
    return website_link