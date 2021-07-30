from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

firefox_driver_path = "C:/Users/Keshav/Documents/CP/webdriver/geckodriver"

driver = webdriver.Firefox(executable_path=firefox_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


def check():
    store_items = driver.find_elements_by_css_selector("#store b")
    prices = []
    for item in store_items[:-1]:
        print(item.text.split("\n"))
        if item.get_attribute("class") != "grayed":
            price = item.text.split("\n")[0].split(" - ")[1].replace(",", "_")
            prices.append(int(price))
    if len(prices) != 0:
        min_price = min(prices)
        min_index = prices.index(min_price)
        store_items[min_index].click()


check_time = time.time() + 5
end_time = time.time() + (60)


cookie = driver.find_element_by_id("cookie")
while end_time > time.time():
    cookie.click()
    if time.time() > check_time:
        check_time += 5
        check()

driver.quit()
