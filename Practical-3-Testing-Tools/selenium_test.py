"""
Automation Testing Tool Demo
Tool type: Automation Testing (Selenium category)

Requires: pip install selenium  +  a browser driver (e.g. Chrome + chromedriver)
Run: python3 selenium_test.py

This is a real Selenium script — run it on a machine with Chrome installed
to see it drive an actual browser.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")
    assert "Login" in driver.title or "The Internet" in driver.title

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    flash = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area" in flash
    print("[Selenium Test] PASS - login flow works, message:", flash.strip())
finally:
    driver.quit()
