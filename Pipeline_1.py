import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_launch():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://github.com/"
    driver.get(url)
    driver.maximize_window()
    assert driver.title == "GitHub"
    driver.save_screenshot("step1_login.png")
