from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import info
import config
import time
from playsound import playsound
import AppKit
import requests


count=1
messages=10
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
no_add="This site can’t be reached\nwww.ghanahostels.org’s server IP address could not be found.\nTry:\nChecking the connection\nChecking the proxy, firewall and DNS configuration\nERR_NAME_NOT_RESOLVED\nReload\nDetails"
reach="This site can’t be reached\nwww.ghanahostels.org’s DNS address could not be found. Diagnosing the problem.\nDNS_PROBE_STARTED\nReload"
connect_close="This site can’t be reached\nwww.ghanahostels.org unexpectedly closed the connection.\nTry:\nChecking the connection\nChecking the proxy and the firewall\nERR_CONNECTION_CLOSED\nReload\nDetails"
interrupt="Your connection was interrupted\nA network change was detected.\nERR_NETWORK_CHANGED\nReload"
connect_off="This site can’t be reached\nwww.ghanahostels.org took too long to respond.\nTry:\nChecking the connection\nChecking the proxy and the firewall\nERR_TIMED_OUT\nReload\nDetails"
test="MAIN\nDashboard\nSETTINGS\nMy Profile\nLogout\nGhana Hostels Limited\nWelcome, Redeemer Kwame\nDashboard\nUniversity of Ghana Student Homepage\nNotice\nCongratulations !!\nYour profile has been validated.\nKindly visit the platform when the portal is opened for reservation / booking.\nClick here to view profile"
while True:
    time.sleep(3)
    if test ==driver.find_element(By.XPATH,"/html/body").text:   
        print("Checking....")
        AppKit.NSBeep()
        driver.refresh() 
    elif connect_off==driver.find_element(By.XPATH,"/html/body").text or interrupt==driver.find_element(By.XPATH,"/html/body").text or connect_close==driver.find_element(By.XPATH,"/html/body").text or reach==driver.find_element(By.XPATH,"/html/body").text or no_add==driver.find_element(By.XPATH,"/html/body").text:
        driver.refresh() 
    else:
        print(driver.find_element(By.XPATH,"/html/body").text)
        playsound("GhanaHostels.mp4")
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.COMMAND + 't')
        driver.get(whatsapp)
        playsound("GhanaHostels.mp4")
        time.sleep(20)
        
        while count <= messages:
            try:
                print(info.chat)
                group=driver.find_element(By.XPATH,f'//span[@title = "{info.chat}"]')
                group.click()
                driver.find_element(By.XPATH,chatbox).send_keys("GHL Bot v1.2: THE GHANA HOSTELS PORTAL IS OPEN. *Someone please call me if I am not online so I can book a room* ")
                button=driver.find_element(By.CLASS_NAME,'_4sWnG')
                button.click()
            except Exception as e:
                print(e)
            count+=1
        playsound("GhanaHostels.mp4")
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.COMMAND + 't')
   
   

