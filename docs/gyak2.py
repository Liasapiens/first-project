from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/server")
coordinates = driver.find_element(By.XPATH, "//tr[td[text() = 'Alattyán']]/td[1]").text
print(coordinates)
print(type(coordinates))