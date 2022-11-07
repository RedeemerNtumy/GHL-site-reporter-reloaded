from gettext import find
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
You do not need to import the info and config files as you can directly input your details here
'''
import time
from playsound import playsound


driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get("https://ghanahostels.org/student/reserve_room")

signup="/html/body/div/div/div/div/div/div[3]/form/button"

id_input="/html/body/div/div/div/div/div/div[3]/form/div[1]/input"

password_input="/html/body/div/div/div/div/div/div[3]/form/div[2]/input"



driver.find_element(By.XPATH,id_input).send_keys("Your ID")
driver.find_element(By.XPATH,password_input).send_keys("Your Password")
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
test="MAIN\nDashboard\nSETTINGS\nMy Profile\nLogout\nGhana Hostels Limited\nWelcome, Redeemer Kwame\nDashboard\nUniversity of Ghana Student Homepage\nNotice\nCongratulations !!\nYour profile has been validated.\nKindly visit the platform when the portal is opened for reservation / booking.\nClick here to view profile"
notice="Notices\nNo notices available"
while True:
    time.sleep(3)
    # If your profile just got validated and the option to select rooms is not showing, change the 'Redeemer Ntumy' in the test variable to the name that appears on your profile and uncomment the code below
    # if test ==driver.find_element(By.XPATH,"/html/body").text:   
    #     print("Checking....")
    #     playsound("beeps.mp4")
    #     driver.refresh() 
    #If the you uncomment the above code, you will have to comment the code below up to driver.refresh()
    if "No notices available" in driver.find_element(By.XPATH,'/html/body').text:
        print("Checking....")
        playsound("beeps.mp4")
        driver.refresh() 

    elif connect_off==driver.find_element(By.XPATH,"/html/body").text or interrupt==driver.find_element(By.XPATH,"/html/body").text or connect_close==driver.find_element(By.XPATH,"/html/body").text or reach==driver.find_element(By.XPATH,"/html/body").text or no_add==driver.find_element(By.XPATH,"/html/body").text:
        driver.refresh() 
    else:
        print(driver.find_element(By.XPATH,"/html/body").text)
        playsound("hostels.mp4") # Replace this mp4 file with your own
        time.sleep(3) 
        driver.refresh() 
        
    
   

