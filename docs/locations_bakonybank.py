from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/server")
id = driver.find_element(By.XPATH, "//tr[td[text() = 'Bakonybánk']]/td[1]").text
int_id= int(id)
print(int_id)
print(type(int_id))