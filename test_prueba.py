# https://onecore.net/selenium-webdriver-for-python.htm
import time
# import outlook
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://localhost:8116/")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")

driver.find_element(By.CSS_SELECTOR, "input.form-control.btn.btn-primary").click()

time.sleep(10)


elemento3=driver.find_element(By.NAME,"Subject")
elemento3.clear()
elemento3.send_keys("Prueba 2")

driver.find_element(By.NAME, "SubmitTicket").click()


time.sleep(20)



driver.close()
