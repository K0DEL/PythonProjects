from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

email = "great__immortal"
password = "animethighs"

firefox_driver_path = "C:/Users/Keshav/Documents/CP/webdriver/geckodriver"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=firefox_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element_by_class_name("js-start-test").click()
        time.sleep(60)
        self.down = float(self.driver.find_element_by_class_name(
            "download-speed").text)
        self.up = float(self.driver.find_element_by_class_name(
            "upload-speed").text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]'
            '/label/div/div[2]/div/input').send_keys(email)
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]'
            '/label/div/div[2]/div/input').send_keys(password)
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/'
            'div/div/div[2]/form/div/div[3]/div/div').click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/'
            'div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/'
            'div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        ).click()
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/'
            'div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/'
            'div/div/div/label/div[1]/div/div/div/div/div[2]/div'
        ).send_keys(
            f'hey Internet Provider my speed is{self.down}down/{self.up}up'
            f'when i pay for 100down/100up.'
        )
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/'
            'div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/'
            'div/div/div[2]/div[3]/div'
        ).click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < 100 or bot.up < 100:
    bot.tweet_at_provider()
