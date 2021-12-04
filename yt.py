import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import selenium
import time
import pyautogui
import webbrowser

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'

url = "https://www.youtube.com/watch?v=lkOiS5BXTAU&list=RDlkOiS5BXTAU&index=1"
list_ = ["https://www.youtube.com/watch?v=lkOiS5BXTAU&list=RDlkOiS5BXTAU&index=1",
 "https://www.youtube.com/watch?v=xxDqIbk-w9U"]

for j in range(1, 2):
    for i in list_:
        driver = webdriver.Chrome()
        pyautogui.press('k')
        webbrowser.open_new(i)
    time.sleep(5)

# driver = webdriver.Chrome()
# pyautogui.press('k')
# webbrowser.open_new(i)
# time.sleep(5)