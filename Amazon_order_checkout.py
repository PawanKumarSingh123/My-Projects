import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("C:/Users/91971/Documents/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(6)
driver.get("https://www.amazon.in/ ")
driver.maximize_window()
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Samsung Galaxy Watch4 Classic Bluetooth(4.6 cm, Black, Compatible with Android Only)")
driver.find_element(By.ID,"nav-search-submit-button").click()

driver.find_element(By.XPATH,"//i[@class = 'a-icon a-icon-checkbox']").click()
Watches=driver.find_elements(By.CLASS_NAME,"a-size-medium a-color-base a-text-normal")

price_list=driver.find_elements(By.CLASS_NAME,"a-price-whole")
driver.find_element(By.LINK_TEXT,"Samsung Galaxy Watch4 Classic Bluetooth(4.6 cm, Black, Compatible with Android Only)").click()
windows_open = driver.window_handles
print(windows_open)
driver.switch_to.window(windows_open[1])
driver.maximize_window()
driver.find_element(By.NAME,"submit.add-to-cart").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span#attach-accessory-proceed-to-checkout-text")))
time.sleep(5)
#driver.find_element(By.ID,"attach-close_sideSheet-link").click()
driver.find_element(By.XPATH,"//input[@aria-labelledby='attach-sidesheet-checkout-button-announce']").click()
Amazon_ID=9719193171
Amazon_Pwd='Pawan9719'
driver.find_element(By.ID,"ap_email").send_keys(Amazon_ID)
driver.find_element(By.ID,"continue").click()
driver.find_element(By.ID,"ap_password").send_keys(Amazon_Pwd)
driver.find_element(By.ID,"signInSubmit").click()
driver.find_element(By.XPATH,"//input[@aria-labelledby='orderSummaryPrimaryActionBtn-announce']").click()
time.sleep(5)
driver.find_element(By.NAME,"ppw-claimCode").send_keys("Amazon_Pwd")
assert "Checkout"==driver.find_element(By.CSS_SELECTOR,"h1").text









