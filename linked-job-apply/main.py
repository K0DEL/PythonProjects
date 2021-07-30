from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

email = "codeschooldxd@gmail.com"
password = "0ld$choolMitraDi"

firefox_driver_path = "C:/Users/Keshav/Documents/CP/webdriver/geckodriver"

driver = webdriver.Firefox(executable_path=firefox_driver_path)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer&location=London%2C%20England%2C%20"
    "United%20Kingdom&redirect=false&position=1&pageNum=0"
)
# click sign in
driver.find_element_by_class_name("nav__button-secondary").click()

# enter email
driver.find_element_by_id("username").send_keys(email)

# enter password
driver.find_element_by_id("password").send_keys(password)

# click final button
driver.find_element_by_css_selector(
    ".login__form_action_container button").click()


# not_now = driver.find_element_by_class_name("btn__secondary--large-muted")
# not_now.click()

time.sleep(3)
# click apply button
driver.find_element_by_xpath(
    '/html/body/div[6]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/'
    'div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div/button/span'
).click()

# enter mobile number
driver.find_element_by_css_selector(
    ".fb-single-line-text .display-flex input").send_keys("123456789")


driver.find_element_by_class_name("artdeco-button--primary").click()


# time.sleep(1)
driver.find_element_by_class_name("artdeco-button--primary").click()


# time.sleep(1)
close = driver.find_element_by_class_name("artdeco-modal__dismiss").click()

# time.sleep(1)
dismiss = driver.find_elements_by_class_name(
    "artdeco-modal__confirm-dialog-btn")[1].click()

jobs = driver.find_elements_by_css_selector(
    ".jobs-search-results__list li")
for job in jobs[1:]:
    job.click()
    time.sleep(1)
