from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

# Login flow
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()


# Check if login was successful
title = driver.find_element(By.CLASS_NAME, "post-title").text


assert "logged in successfully" in title.lower()

print("TEST 1 PASSED : LOGIN SUCCESSFUL")


driver.quit()