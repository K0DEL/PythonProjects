from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

email = "_thedarkdeveloper_"
password = "<Tech!e><$her10ck>Ig"

firefox_driver_path = "C:/Users/Keshav/Documents/CP/webdriver/geckodriver"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=firefox_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        self.driver.find_element_by_name("username").send_keys(email)
        self.driver.find_element_by_name("password").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div[1]/div/'
            'form/div/div[3]/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div/div/button'
        ).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]'
        ).click()

    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/'
            'ul/li[2]/a').click()
        pop_up_window = WebDriverWait(
            self.driver, 2).until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='isgrP']")))
        while True:
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + '
                'arguments[0].offsetHeight;',
                pop_up_window)
            time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
