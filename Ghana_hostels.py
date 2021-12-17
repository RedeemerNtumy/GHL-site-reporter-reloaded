from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
'''
You do not need to import the info and config files as you can directly input your details here
'''
import time
from playsound import playsound
import AppKit # This may not work on windows to play a sound
import requests

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get("https://ghanahostels.org/student/reserve_room")

signup="/html/body/div/div/div/div/div/div[3]/form/button"

id_input="/html/body/div/div/div/div/div/div[3]/form/div[1]/input"

password_input="/html/body/div/div/div/div/div/div[3]/form/div[2]/input"

my_personal_whatsapp_group_xpath='//*[@id="pane-side"]/div[1]/div/div/div[12]/div/div/div[2]'

chatbox='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'


driver.find_element(By.XPATH,id_input).send_keys(info.your_id) #Replace info.your_id with a string of your ID
driver.find_element(By.XPATH,password_input).send_keys(info.yout_password)# Replace info.your_password with a string of your password
driver.find_element(By.XPATH,signup).click()


'''
Below are some of the network errors that may arise during the process.Check to see if is would be different from Windows
'''
dino="No Internet\nTry:\nChecking the network cables, modem and router\nReconnecting to Wi-Fi\nERR_INTERNET_DISCONNECTED\nDino game. A pixelated dinosaur dodges cacti and pterodactyls as it runs across a desolate landscape. When you hear an audio cue, press space to jump over obstacles."
no_add="This site can’t be reached\nwww.ghanahostels.org’s server IP address could not be found.\nTry:\nChecking the connection\nChecking the proxy, firewall and DNS configuration\nERR_NAME_NOT_RESOLVED\nReload\nDetails"
reach="This site can’t be reached\nwww.ghanahostels.org’s DNS address could not be found. Diagnosing the problem.\nDNS_PROBE_STARTED\nReload"
connect_close="This site can’t be reached\nwww.ghanahostels.org unexpectedly closed the connection.\nTry:\nChecking the connection\nChecking the proxy and the firewall\nERR_CONNECTION_CLOSED\nReload\nDetails"
interrupt="Your connection was interrupted\nA network change was detected.\nERR_NETWORK_CHANGED\nReload"
connect_off="This site can’t be reached\nwww.ghanahostels.org took too long to respond.\nTry:\nChecking the connection\nChecking the proxy and the firewall\nERR_TIMED_OUT\nReload\nDetails"
block="Select a block"
while True:
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/ul/li[4]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="block"]').click()
    if block ==driver.find_element(By.XPATH,'//*[@id="block"]').text:
        print("Checking....")
        driver.refresh() 
    else:
        playsound("YOUR MP4 THAT WOULD PLAY WHEN THE PORTAL IS OPEN.mp4") #PLACE IN SAME DIRECTORY
        
    
   

