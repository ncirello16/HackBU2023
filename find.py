from bs4 import BeautifulSoup
import requests

def Diction(html):
    URL = html
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    mydivs = soup.find("div",{"class": "sense-content w-100"})
    my = mydivs.find("span", {"dtText"})
    print(my.text[1:])
    return my.text[1:]


if __name__ == "__main__":

    x = input("what do you want to know?\n")
    Diction(f"https://www.merriam-webster.com/dictionary/{x}")