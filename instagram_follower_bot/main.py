from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

SIMILAR_ACCOUNT = "knoroz__"
USERNAME = "bot00100100"
PASSWORD = "howtofree.org"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        user_name = self.driver.find_element(By.NAME, 'username')
        user_name.send_keys(USERNAME)

        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        time.sleep(2)

        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        time.sleep(20)
        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'followers')
        followers.click()
        time.sleep(2)

        modal = self.driver.find_element(By.CLASS_NAME, "_aano")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()
            finally:
                time.sleep(2)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
