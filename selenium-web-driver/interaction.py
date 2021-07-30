from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

firefox_driver_path = "C:/Users/Keshav/Documents/CP/webdriver/geckodriver"

driver = webdriver.Firefox(executable_path=firefox_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
fname.send_keys("Pintu")

lname = driver.find_element_by_name("lName")
lname.send_keys("Kumar")

email = driver.find_element_by_name("email")
email.send_keys("classwaliid@gmail.com")

button = driver.find_element_by_css_selector("button")
button.click()
