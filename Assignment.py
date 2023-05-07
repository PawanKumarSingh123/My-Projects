import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("C:/Users/91971/Documents/chromedriver")
driver =webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windows_open=driver.window_handles
driver.switch_to.window(windows_open[1])
Text_Written=driver.find_element(By.XPATH,"//div[@class='container']/div/div/p[2]").text
words=Text_Written.split()
for word in words:
    if "@" in word:
        email=word
        #print(email)
        break;
driver.switch_to.window(windows_open[0])
driver.find_element(By.NAME,"username").send_keys(email)
driver.find_element(By.NAME,"password").send_keys("12345678")
driver.find_element(By.ID,"signInBtn").click()
wait =WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-danger col-md-12']")))
print(driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text)
