from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#call a chrome driver
service_obj= Service("/Users/shivarchetty/Downloads/chrome/chromedriver");
driver = webdriver.Chrome(service=service_obj)


driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSselector, name, linktext
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345");
driver.find_element(By.ID,"exampleCheck1").click()

# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
# CSS - tagname[attribute='value' ->
driver.find_element(By.CSS_SELECTOR,"input[name='name'").send_keys("Shivar")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

