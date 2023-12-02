import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("drivers/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()
bot.get("https://www.viajesexito.com")