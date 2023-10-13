import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://127.0.0.1:5000/")
time.sleep(2)
driver.find_element(By.ID,"readButton").click()
time.sleep(5)
driver.find_element(By.ID,"createButton").click()
driver.find_element(By.ID,"createName").send_keys("Pavitra")
driver.find_element(By.ID,"createDoj").send_keys("15092021")
driver.find_element(By.ID,"createLocation").send_keys("Vijayawda")
driver.find_element(By.ID,"createProject").send_keys("CISCO")
driver.find_element(By.XPATH,"(//button[@type='submit'])[1]").click()
driver.find_element(By.ID,"readButton").click()
time.sleep(5)
driver.find_element(By.ID,"updateButton").click()
driver.find_element(By.ID,"updateEmployeeId").send_keys("6")
driver.find_element(By.ID,"updateName").send_keys("Pavitra.V")
driver.find_element(By.ID,"updateDoj").send_keys("15092021")
driver.find_element(By.ID,"updateLocation").send_keys("Vijyawada")
driver.find_element(By.ID,"updateProject").send_keys("CISCO")
driver.find_element(By.XPATH,"(//button[@type='submit'])[2]").click()
driver.find_element(By.ID,"readButton").click()
time.sleep(5)
driver.find_element(By.ID,"deleteButton").click()
driver.find_element(By.ID,"deleteEmployeeId").send_keys("6")
driver.find_element(By.XPATH,"(//button[@type='submit'])[3]").click()
driver.find_element(By.ID,"readButton").click()
time.sleep(5)
print("Test passed")

driver.quit()
