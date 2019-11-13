from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


#Írj egy függvényt, ami paraméterül kap egy nevet, és kiírja a település koordinátáját!

driver.get("http://www.learnwebservices.com/locations/server")
def print_coords_by_name (name):
    xpath = "//tr[td[text() = 'name']]/td[3]".replace("name", name)
    coords = driver.find_element(By.XPATH, xpath).text
    print(coords)

    