from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Calling on the chrome browser
service_obj= Service("/Users/shivarchetty/Downloads/chrome/chromedriver");
driver = webdriver.Chrome(service=service_obj)
#Getting ontp the site page
driver.get('http://localhost:6464/')

#Finding the textbox element and typing in the box
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("7")

#Finding the submit button and clicking on the button to subnit
driver.find_element(By.XPATH,"//button[@type='submit']").click()

#Finding the message printed after submiting the factorial
message = driver.find_element(By.ID,"resultDiv").text
print(message)
assert "5040" in message