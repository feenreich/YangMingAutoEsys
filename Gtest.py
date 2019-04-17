from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import time
import xlrd
import pprint

date_format = '%Y-%m-%d'
district_jiaobao = ["1-1","1-2","1-4","2-2","2-8","3-5","3-2","3-7"]
driver = webdriver.Chrome()
driver.get("http://192.168.1.4:8080/?fbclid=IwAR2xk3BV_2iDu_z721JMYoVcdOkvEY6I-Nd27Bx604eBSnkvOzYgnvdV05g")

elem = driver.find_element_by_name("user_id")
elem.send_keys("df_byadofu")
elem = driver.find_element_by_name("password")
elem.send_keys("Q223553582d@")
elem = driver.find_element_by_name("confirm")
s = input("verification:\n")
elem.send_keys(s)
btn = driver.find_element(By.XPATH, '//button')
btn.click()

driver.get("http://192.168.1.4:8080/life_record.jsp")

district = '3-5'
s = Select(driver.find_element_by_id('s_area'))
s.select_by_visible_text(district)
name = input("name: ")
s = Select(driver.find_element_by_id('s_si_id'))
s.select_by_visible_text(name)
btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
driver.execute_script("arguments[0].click()", btn)
tbody = driver.find_element(By.XPATH, '//table[@id="simple-table"]/tbody')
links = tbody.find_elements(By.TAG_NAME, 'a')
if len(links) > 1:
	link = links[1].get_attribute('href')
	driver.get(link)
	tbody = driver.find_element_by_id('liferecord_tbody')
	script = "add_item('liferecord_table')"
	driver.execute_script(script)
	trs = tbody.find_elements(By.TAG_NAME, 'tr')
	idx = str(len(trs) - 1)
	date = '2019-03-01'
	script = "document.querySelectorAll(\"input[name='liferecord_date']\")[" + str(len(trs) - 1) + "].value = '" + date + "'"
	driver.execute_script(script)
	memo = 'ABCCCCC'
	script = "document.querySelectorAll(\"textarea[name='liferecord_memo']\")[" + str(len(trs) - 1) + "].value = '" + memo + "'"
	driver.execute_script(script)
	script = "save_item('liferecord', " + str(len(trs)) + ")"
	driver.execute_script(script)