#!/usr/bin/env python
# coding: utf-8

# In[2]:


## User log-in functionality

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Firefox
driver = webdriver.Firefox()

# Navigate to the login page
driver.get("https://camerarentals.store/user/login")

# Find the "Email" field by name and type in an email address
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("bhuvaneshcsu47@gmail.com")

# Find the "Password" field by name and type in a password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Bhuvaneshqwer@098")

wait = WebDriverWait(driver, 10)
Click_Now = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha"]')))

# click on the recaptcha element
Click_Now.click()


# In[9]:


## User log-in with invalid email

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Firefox
driver = webdriver.Firefox()

# Navigate to the login page
driver.get("https://camerarentals.store/user/login")

# Find the "Email" field by name and type in an email address
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("bhuvaneshnohar22@gmail.com")

# Find the "Password" field by name and type in a password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Bhuvaneshqwer@098")

wait = WebDriverWait(driver, 10)
Click_Now = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha"]')))

# click on the recaptcha element
Click_Now.click()


# In[6]:


## User log-in with invalid password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Firefox
driver = webdriver.Firefox()

# Navigate to the login page
driver.get("https://camerarentals.store/user/login")

# Find the "Email" field by name and type in an email address
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("bhuvaneshcsu47@gmail.com")

# Find the "Password" field by name and type in a password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Bhu098@qwer")

wait = WebDriverWait(driver, 10)
Click_Now = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha"]')))

# click on the recaptcha element
Click_Now.click()

