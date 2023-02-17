import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s) 