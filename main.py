import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.maximize_window()

#Locate login
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

# Assert if the dashboard page contains the word "Dashboard"
dashboard_element = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
assert "Dashboard" in dashboard_element.text, "Dashboard was not found on the page!"

