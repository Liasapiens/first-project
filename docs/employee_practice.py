from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def print_welcome():
    print("Kezdodhet a teszteles!")


print_welcome()

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/create-employee.xhtml")


#irj egy olyan fuggvenyt, ami raklikkel a beviteli mezore:
def click_to_name_input():
    driver.find_element(By.ID, 'create-form:name-input').click()


#itt a beviteli mező:
#driver.find_element(By.ID, 'create-form:name-input').click()

click_to_name_input()
driver.find_element(By.XPATH, '//h1').click()

WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[@class = 'invalid-feedback']"), "Az alkalmazott nevét meg kell adni!"))


error_message = driver.find_element(By.XPATH, "//span[@class = 'invalid-feedback']").text
print(error_message)


#Irj egy olyan fuggvenyt, ami a parameterkent kapott nevet beirja a beviteli mezobe type_to_name_input neven

def type_to_name_input(name):
    driver.find_element(By.ID, 'create-form:name-input').send_keys(name)

#Irj egy olyan fuggvenyt, ami raklikkel a cimsorra: click_to_header()

def click_to_header():
    driver.find_element(By.XPATH, '//h1').click()



#Irj egy olyan fuggvenyt, ami a parameterkent megadott hibauzenetre var, wait_for_error_message

def wait_for_error_message(message):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[@class = 'invalid-feedback']"),
                                                          "Az alkalmazott nevét meg kell adni!"))
    error_message = driver.find_element(By.XPATH, "//span[@class = 'invalid-feedback']" ).text
    print(error_message)

#Olvassa be a monogramot, es azzal terjen vissza: read_monogram

def wait_for_monogram(expected_monogram):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "create-form:monogram-text"),
                                                          expected_monogram))


type_to_name_input("Name Input")
monogram = wait_for_monogram("NI")
print(monogram)