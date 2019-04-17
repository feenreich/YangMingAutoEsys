from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://webitr.gov.taipei/WebITR/plugins/app/login/login.jsp.htm?fbclid=IwAR1oypmQIH-VCzqSawEpR7fFS_JDVQ9cd-JNFsTZNy2K4nVTBwWn9rSFSbs")

#driver.implicitly_wait(10)

elem = driver.find_element_by_id("userName")
elem.send_keys("feenreich")
elem = driver.find_element_by_id("login_key")
elem.send_keys("Dasfeenreich811223")
elem = driver.find_element_by_id("sendBtn")
elem.click()

driver.get("https://webitr.gov.taipei/WebITR/p4/apply/leave/apply.ug")
s = Select(driver.find_element_by_name('leavetype'))
s.select_by_value("19")

elem = driver.find_element_by_id("reason")
elem.send_keys("爽")
#wait = input("PRESS ENTER TO CONTINUE.")

#driver.close()