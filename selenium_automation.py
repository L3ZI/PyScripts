import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

driver = webdriver.Firefox(executable_path = r'C:/Users/pasan/Downloads/geckodriver-v0.32.2-win64/geckodriver.exe') #web driver local file location

driver.get('https://lms.sliit.lk/login/index.php') #target website url

email = driver.find_element(By.ID, 'username')  #email or username section
email.send_keys('#Put your cute username here#');

password = driver.find_element(By.ID, 'password') #password section
password.send_keys('#Put your security keyword here#');

signInButton = driver.find_element(By.ID,'loginbtn') #sign in button trigger 
signInButton.click();

###################Happy Coding###################

###################CLAY###########################