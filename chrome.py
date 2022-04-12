

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')

driver = webdriver.Chrome(executable_path="chromedriver",
                          chrome_options=options)
driver.get("http://localhost:4200/monitor/0")
driver.fullscreen_window()
wait = WebDriverWait(driver, 10)
# assert "Python" in driver.title
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
button = driver.find_element_by_xpath("//button")

username.send_keys("admin")
password.send_keys("admin123")
button.click()
# assert "No results found." not in driver.page_source
time.sleep(3)

nav = driver.find_elements_by_xpath("//li")
print(nav[1])
print(nav[2])
for num in range(0, 50):
    nav[1].click()
    time.sleep(0.5)
    nav[2].click()
    time.sleep(0.5)


# driver.close()
