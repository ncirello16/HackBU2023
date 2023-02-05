import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def getDaysLeft():
    todayDate = datetime.today()
    endDate = datetime(2023, 5, 13)
    totalDaysLeft = (endDate - todayDate).days
    return totalDaysLeft


def parseBingWebpage(id,ps):
    username = id
    password = ps

    url = "https://bing.campuscardcenter.com/ch/login.html"
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op, service=Service(ChromeDriverManager().install()))
    driver.get(url)

    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("name", "action").click()
    time.sleep(2)
    moneyLeft = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/table[2]/tbody/tr[5]/td[4]/div')
    if(moneyLeft.text == "$ 0.00"):
        moneyLeft = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/table[2]/tbody/tr[4]/td[4]/div')


    return moneyLeft


def getMoneyPerDay(totalMoneyLeft):

    totalDaysLeft = getDaysLeft()

    formattedFinalTotal = "{:.2f}".format(float(totalMoneyLeft.text[2:]) / totalDaysLeft)
    output = [totalMoneyLeft.text,formattedFinalTotal]
    return output

if __name__ == "__main__":
    moneyLeft = parseBingWebpage('adwlkj','dawklj')
    getMoneyPerDay(moneyLeft)
