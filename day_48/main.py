from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, 'fName')
first_name.click()
first_name.send_keys("Sugam")
first_name.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, 'lName')
first_name.click()
first_name.send_keys("Dahal")
first_name.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, 'email')
first_name.click()
first_name.send_keys("sdsdsdsd@gmail.com")
first_name.send_keys(Keys.ENTER)

sign_up = driver.find_element(By.CSS_SELECTOR, 'form')
sign_up.click()

time.sleep(60)
driver.quit()
