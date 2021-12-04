from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import info
import time
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

options=webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=/Library/Application Support/Google/Chrome") #User data direcotry for Chrome. This is for MAC
options.add_argument("profile-directory=Default")
driver.get("https://www.ghanahostels.org/student")
signup="/html/body/div/div/div/div/div/div[3]/form/button"
id_input="/html/body/div/div/div/div/div/div[3]/form/div[1]/input"
password_input="/html/body/div/div/div/div/div/div[3]/form/div[2]/input"
my_personal_whatsapp_group_xpath='//*[@id="pane-side"]/div[1]/div/div/div[12]/div/div/div[2]'
whatsapp="https://web.whatsapp.com"
chatbox='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'

driver.find_element(By.XPATH,id_input).send_keys(info.your_id)
driver.find_element(By.XPATH,password_input).send_keys(info.your_password)
driver.find_element(By.XPATH,signup).click()
while True:
    if "Kinly visit the platform when the portal is opened" in driver.find_element(By.XPATH,"/html/body").text:   
        break
    else:
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.COMMAND + 't') 
        driver.get(whatsapp)
        driver.find_element(By.XPATH,my_personal_whatsapp_group_xpath).click()
        driver.find_element(By.XPATH,chatbox).send_keys("Testing this GHL bot. It is not my who typed it")
        time.sleep(500) #Uncomment this if running code for the first time

