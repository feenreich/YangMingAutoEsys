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

#login
elem = driver.find_element_by_name("user_id")
#s = input("帳號:\n")
#elem.send_keys(s)
elem.send_keys("df_byadofu")
elem = driver.find_element_by_name("password")
#s = input("密碼:\n")
#elem.send_keys(s)
elem.send_keys("Q223553582d@")
elem = driver.find_element_by_name("confirm")
s = input("驗證碼:\n")
elem.send_keys(s)
btn = driver.find_element(By.XPATH, '//button')
btn.click()

driver.get("http://192.168.1.4:8080/familycontact_record.jsp")

f = open('output.txt', 'w')
for district in district_jiaobao:
	'''
	s = input("是否檢查" + district + "區?(y/n), 按z離開\n")
	if s == 'n':
		continue
	elif s == 'z':
		break
	elif s != 'y':
		print("請輸入y,n,或z")
	'''	
	s = Select(driver.find_element_by_id('s_area'))
	s.select_by_visible_text(district)
	print(district)
	f.write(district + '\n')
	s = Select(driver.find_element_by_id('s_si_id'))
	ops = s.options
	names = []
	for op in ops:
		names.append(op.text)
	for name in names:
		if name == "請選擇":
			continue
		#wait = WebDriverWait(driver, 10)
		#wait.until(EC.element_to_be_clickable((By.ID, 's_si_id')))
		s = Select(driver.find_element_by_id('s_si_id'))
		s.select_by_visible_text(name)
		print(name)
		#f.write(name)
		#wait = WebDriverWait(driver, 10)
		#wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="search_btn"]')))
		btn = driver.find_element(By.XPATH, '//button[@id="search_btn"]')
		driver.execute_script("arguments[0].click()", btn)
		
		table = driver.find_element(By.XPATH, '//table[@id="simple-table"]/tbody')
		rows = table.find_elements(By.TAG_NAME, 'tr')
		pre_date = ''
		for row in rows:
			content = row.find_elements(By.XPATH, 'td')
			if len(content) < 2:
				continue
			cur_date = row.find_element(By.XPATH, 'td[2]').text
			#print('\t' + date)
			if pre_date != '':
				p_date = datetime.strptime(pre_date, date_format)
				c_date = datetime.strptime(cur_date, date_format)
				diff = p_date - c_date
				if diff.days > 90:
					f.write(name + ': ' + pre_date + ' - ' + cur_date + '\n')
				pre_date = cur_date
		#f.write('\n')
f.close()
driver.close()