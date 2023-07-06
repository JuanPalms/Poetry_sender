"""
This python module implements the extraction of one poem from the page POETRY FOUNDATION
link: https://www.poetryfoundation.org/poems/browse#page=1&sort_by=recently_added
and stores it as a txt temporary file
"""
import os
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import random

# Add the parent directory to sys.path
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
    
from outils import load_config, get_driver

def scrap_poem():

    
    # random integer for selecting page for scrapping  poem
    page_random = random.randint(1, 133)
    # random integer for selecting page for generating poem
    poem_random = random.randint(1,20)
    # principal page for getting the poems
    path_poems=f'https://www.poetryfoundation.org/poems/browse#page={page_random}&sort_by=recently_added&topics=20'
    
    # Get the driver for the provided url
    driver=get_driver(path_poems)
    time.sleep(3)
    title = driver.find_element(by = "xpath",value = f"/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/div[3]/ol/li[{poem_random}]/div/div[1]/h2/a/span").text
    time.sleep(3)
    driver.find_element(by = "xpath",value = f"/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/div[3]/ol/li[{poem_random}]/div/div[1]/h2/a/span").click()
    author = driver.find_element(by = "xpath", value ="/html/body/div[1]/div[2]/div/div[1]/article/div/div/div/div/div[1]/div/div[2]/div/span/a").text
    time.sleep(3)
    poem = driver.find_element(by = "xpath", value = "/html/body/div[1]/div[2]/div/div[1]/article/div/div/div/div/div[1]/div/div[3]/div").text
    time.sleep(3)
    return title, author, poem