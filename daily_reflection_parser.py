#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to ChromeDriver
driver_path = '/usr/bin/chromedriver'

# Chrome options to simulate a real user environment
chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")  # Start maximized
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Initialize the browser driver
s = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=s, options=chrome_options)

# Open the website
driver.get('https://www.aa.org/daily-reflections')

# Wait for JavaScript to load
time.sleep(10)  # Adjust the sleep time as necessary based on your internet speed and website's response time

try:
    # Extract and print the title (Equality) directly using CSS Selector
    title = driver.find_element(By.CSS_SELECTOR, 'span.field--name-title').text
    print(title)

    # Extract and print the text inside the specified div directly using CSS Selector
    body_text = driver.find_element(By.CSS_SELECTOR, 'div.field--name-body').text
    print(body_text)
except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()
