from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import info
import config
import time

count=1
messages=50
options=webdriver.ChromeOptions()
options.add_argument(config.CHROME_PROFILE_PATH) 
driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=options)

driver.get("https://www.ghanahostels.org/student")

signup="/html/body/div/div/div/div/div/div[3]/form/button"

id_input="/html/body/div/div/div/div/div/div[3]/form/div[1]/input"

password_input="/html/body/div/div/div/div/div/div[3]/form/div[2]/input"

my_personal_whatsapp_group_xpath='//*[@id="pane-side"]/div[1]/div/div/div[12]/div/div/div[2]'

chatbox='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'

whatsapp="https://web.whatsapp.com"



driver.find_element(By.XPATH,id_input).send_keys(info.your_id)
driver.find_element(By.XPATH,password_input).send_keys(info.your_password)
driver.find_element(By.XPATH,signup).click()
while True:
    if "Kindvisit the platform when the portal is opened" in driver.find_element(By.XPATH,"/html/body").text:   
        print(1)
        #time.sleep(20)
    else:
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.get(whatsapp)
        time.sleep(20) # Change time to 20 after first login
        while count <= messages:
            try:
                group=driver.find_element(By.XPATH,'//span[@title = "{}"]'.format(info.chat))
                group.click()
                driver.find_element(By.XPATH,chatbox).send_keys("GHL bot v1.2 Speaking: The Ghana Hostels portal is open ‼️‼️‼️‼️")
                button=driver.find_element(By.CLASS_NAME,'_4sWnG')
                button.click()
                count = count + 1
                time.sleep(1)
            except Exception as e:
                print(e)
driver.close()  

