import urllib3
from bs4 import BeautifulSoup
import requests



def Diction(html):
    URL = f"https://www.merriam-webster.com/dictionary/{html}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        mydivs = soup.find("div",{"class": "sense-content w-100"})
        my = mydivs.find("span", {"dtText"})
        output = f"DicBot: {html} - {my.text[1:]}"

    except:
        output = f"DicBot: Cannot find {html}!"

    return output

if __name__ == "__main__":

    x = input("what do you want to know?\n")
    # Diction(f"https://www.merriam-webster.com/dictionary/{x}")
