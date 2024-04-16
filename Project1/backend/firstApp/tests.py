from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

#creating a dictionary named 'credentials'
credentials = {
    "username": "srks",
    "password": "123"
}
#Convert dictionary to a Json string
credentials_json = json.dumps(credentials) 

driver = webdriver.Chrome()

#Maximize the Window
driver.maximize_window()

#Search fo The URL
driver.get("http://127.0.0.1:8000/")
print("Your Server is running..!!")


#login
time.sleep(2)
textarea_input = driver.find_element(By.NAME, "_content")
textarea_input.send_keys(credentials_json)
post_button = driver.find_element(By.XPATH, "//button[text()='POST']")
post_button.click()
print("login success ")
time.sleep(2)

#Adding Data
id_input = driver.find_element(By.CLASS_NAME, 'id' )
id_input.clear()
id_input.send_keys("1")
title_input = driver.find_element(By.CLASS_NAME, 'title' )
title_input.clear()
title_input.send_keys("test")
date_input = driver.find_element(By.CLASS_NAME, 'date' )
date_input.clear()
date_input.send_keys("2024-05-05")
post_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
post_button.click()
print("Data added successfully ")
time.sleep(2)

#Search Data
search_input = driver.find_element(By.CLASS_NAME, "search-bar")
search_input.clear()
search_input.send_keys('1')
search_btn = driver.find_element(By.XPATH, "//button[text()='Search']")
search_btn.click()
print("Search function is working perfectly")
time.sleep(2)

#Delete Data
delete_input = driver.find_element(By.CLASS_NAME, 'delete')
delete_input.clear()
delete_input.send_keys('1')
delete_btn = driver.find_element(By.XPATH, "//button[text()='Completed']")
delete_btn.click()
print("Delete function is working perfectly")
time.sleep(2)


#Re-Login
textarea_input = driver.find_element(By.NAME, "_content")
textarea_input.send_keys(credentials_json)
post_button = driver.find_element(By.XPATH, "//button[text()='POST']")
post_button.click()
print("Re-login success ")

print("Everything Works Well..!!!")
time.sleep(2)
driver.quit()
