from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#call a chrome driver
service_obj= Service("/Users/shivarchetty/Downloads/chrome/chromedriver");
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("http://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("http://www.google.com")
driver.minimize_window()
driver.close()