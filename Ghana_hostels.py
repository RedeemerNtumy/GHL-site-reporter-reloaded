from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://www.ghanahostels.org/student")
signup="/html/body/div/div/div/div/div/div[3]/form/button"
id_input="/html/body/div/div/div/div/div/div[3]/form/div[1]/input"
password_input="/html/body/div/div/div/div/div/div[3]/form/div[2]/input"

driver.find_element(By.XPATH,id_input).send_keys("YOUR ID")
driver.find_element(By.XPATH,password_input).send_keys("YOUR PASSWORD")
driver.find_element(By.XPATH,signup).click()
while True:
    if "Kindly visit the platform when the portal is opened" in driver.find_element(By.XPATH,"/html/body").text:   
        print(1)
        time.sleep(5)

