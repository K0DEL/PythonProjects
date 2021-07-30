from selenium import webdriver

firefox_driver_path = "C:/Users/Keshav/Documents/CP/webdriver/geckodriver"

driver = webdriver.Firefox(executable_path=firefox_driver_path)

driver.get("https://www.python.org/")
price = driver.find_element_by_id("SIvCob")
print(price.text)
driver.close()
