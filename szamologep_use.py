from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://liasapiens.github.io/first-project/")
driver.find_element(By.NAME, "a").send_keys("24")
driver.find_element(By.NAME, "b").send_keys("42")

header_text = driver.find_element(By.XPATH, "//h1").text
assert header_text == "Szamologep"

print(header_text)
assert header_text == "Szamologep"

driver.find_element(By.XPATH, "//input[3]").click()

result = driver.find_element (By.ID, "result-input").get_attribute("value")

driver.save_screenshot("result.png")

assert result == "66"