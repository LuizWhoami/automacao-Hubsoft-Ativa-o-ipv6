import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import pyautogui
sleep(10)
x,y = pyautogui.position()
print("""Posição x: {}
Posição y: {}""".format(x, y))