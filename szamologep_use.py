from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://liasapiens.github.io/first-project/")
driver.find_element(By.NAME, "a").send_keys("23")
driver.find_element(By.NAME, "b").send_keys("32")

header_text = driver.find_element(By.XPATH, "//h1").text
assert header_text == "Szamologep"

driver.find_element(By.XPATH, "//input[3]").click
print(header_text)
assert header_text == "Szamologep"