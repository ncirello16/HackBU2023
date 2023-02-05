import urllib3
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from selenium import webdriver
from sys import platform


def Diction(html):
    URL = f"https://www.merriam-webster.com/dictionary/{html}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        mydivs = soup.find("div",{"class": "sense-content w-100"})
        my = mydivs.find("span", {"dtText"})
        output = f"DicBot: {my.text[1:]}"

    except:
        output = f"DicBot: Cannot find {html}!"

    return output

def valentine(q):
    if platform == "linux" or platform == "linux2":
    # linux
        pass
    elif platform == "darwin":
        PATH = "bin/chromedriver"
    # OS X
        pass
    elif platform == "win32":

        PATH = "bin/chromedriver.exe"

    driver = webdriver.Chrome(PATH)
    driver.get("https://amazon.com")


    print(driver.title)
if __name__ == "__main__":

    x = input("what do you want to know?\n")
    # Diction(f"https://www.merriam-webster.com/dictionary/{x}")
    valentine(x)