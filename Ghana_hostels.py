from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://www.ghanahostels.org/student")
signup="/html/body/div/div/div/div/div/div[3]/form/button"
id_input="/html/body/div/div/div/div/div/div[3]/form/div[1]/input"
password_input="/html/body/div/div/div/div/div/div[3]/form/div[2]/input"
<<<<<<< HEAD
driver.find_element(By.XPATH,id_input).send_keys("10712863")
driver.find_element(By.XPATH,password_input).send_keys("redeemerntumy4019")
driver.find_element(By.XPATH,signup).click()
while True:
    if "Kindly visit the platform when the portal is opened for reservation / booking." in driver.find_element(By.XPATH,"/html/body").text:   
        print(1)
=======
driver.find_element_by_xpath(id_input).send_keys("YOUR ID")
driver.find_element_by_xpath(password_input).send_keys("YOUR PASSWORD")
driver.find_element_by_xpath(signup).click()
no_rooms=driver.find_element(By.XPATH,"/html/body").text
while no_rooms==driver.find_element(By.XPATH,"/html/body").text:
    time.sleep(5)
    print(1)


>>>>>>> 95ea6508373bb2d19a8861252db814840c424694
