

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/server")

#Velence és Báta azonosítója --> int --> összead

idv = driver.find_element(By.XPATH, "//tr[td[text() = 'Velence']]/td[1]").text
idb = driver.find_element(By.XPATH, "//tr[td[text() = 'Báta']]/td[1]").text
int_idv= int(idv)
int_idb= int(idb)

print(int_idv + int_idb)

#Keresd ki a 9876 azonosítójú település nevét, majd írd ki az első három karakterét!
city_name = driver.find_element(By.XPATH, "//tr[td[text() = '9876']]/td[2]").text
print(city_name[0:3])

#Keresd ki a 9898 azonosítójú település nevét, majd írd ki visszafele!
city_name_backwards = driver.find_element(By.XPATH, "//tr[td[text() = '9742']]/td[2]").text
print(city_name_backwards[::-1])

#Keresd ki a 11115 azonosítójú település nevét, majd írd ki a csupa nagy és csupa kisbetűvel, hogy hány karakterből áll!
city_name_length = driver.find_element(By.XPATH, "//tr[td[text() = '11115']]/td[2]").text
print(len(city_name_length))
print(city_name_length.upper())
print(city_name_length.lower())


#Keresd ki a 11116, 11117, 11118 azonosítójú település nevét, majd írd ki egymástól kötőjelekkel elválasztva!
name_one=driver.find_element(By.XPATH, "//tr[td[text() = '11116']]/td[2]").text
name_two=driver.find_element(By.XPATH, "//tr[td[text() = '11117']]/td[2]").text
name_three=driver.find_element(By.XPATH, "//tr[td[text() = '11118']]/td[2]").text









