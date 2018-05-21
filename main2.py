from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path='chromedriver')
driver.get("http://www.facebook.com")

driver.find_element_by_id("email").send_keys("USERNAME")
driver.find_element_by_id("pass").send_keys("PASSWORD")
driver.find_element_by_id("login_form").submit()

sleep(2)
for i in driver.find_elements_by_class_name("userContent"):
    print(i.text)
sleep(2)
# driver.close()