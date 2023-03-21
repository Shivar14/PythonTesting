from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Calling on the browser
service_obj= Service("/Users/shivarchetty/Downloads/chrome/chromedriver");
driver = webdriver.Chrome(service=service_obj)
#Getting onto the site page
driver.get('http://localhost:6464/')

#Template for CSS -tagname[attribute='value']

#Finding input box and entering wrong number in order for red form to appear
driver.find_element(By.CSS_SELECTOR,"input[type='text'").send_keys("0.1")

#Clicking on submit
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

#Finding the red form element on page
driver.find_element(By.CSS_SELECTOR,"input[style='border: 2px solid red;']")

#Findning the message printed and getting the text printed
message = driver.find_element(By.ID,"resultDiv").text
print(message)
assert "integer" in message