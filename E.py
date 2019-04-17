from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time
import xlrd
import pprint

def get_list(sheet):
    return [sheet.row_values(row) for row in range(sheet.nrows)]

#district_jiaobao = ["1-1","1-2","1-4","2-2","2-8","3-5","3-2","3-7"]
driver = webdriver.Chrome()
driver.get("http://192.168.1.4:8080/?fbclid=IwAR2xk3BV_2iDu_z721JMYoVcdOkvEY6I-Nd27Bx604eBSnkvOzYgnvdV05g")

#login
elem = driver.find_element_by_name("user_id")
elem.send_keys("df_byadofu")
elem = driver.find_element_by_name("password")
elem.send_keys("Q223553582d@")
elem = driver.find_element_by_name("confirm")
s = input("GoGo:\n")
elem.send_keys(s)
btn = driver.find_element(By.XPATH, '//button')
btn.click()

#ADD
wb = xlrd.open_workbook('family_E.xlsx')
sheet = wb.sheet_by_name('sheet1')
list = get_list(sheet)

for i in range(sheet.nrows):
	district = list[i][0]
	name = list[i][1]
	date = list[i][2]
	stime = list[i][3]
	stime_h = stime[0:2]
	stime_m = stime[3:5]
	etime = list[i][4]
	etime_h = etime[0:2]
	etime_m = etime[3:5]
	job_title = list[i][5]
	way = list[i][6]
	objects = list[i][7]
	cause = list[i][8]
	content = list[i][9]
	memo = list[i][10]

	driver.get("http://192.168.1.4:8080/familycontact_record.jsp?VIEW=ADD")
	s = Select(driver.find_element_by_name('s_area'))
	s.select_by_visible_text(district)
	s = Select(driver.find_element_by_name('s_si_id'))
	s.select_by_visible_text(name)
	driver.execute_script('document.querySelector("#fc_date").value = ' + '"' + date + '"')
	s = Select(driver.find_element_by_id('fc_star_time_h'))
	s.select_by_visible_text(stime_h)
	s = Select(driver.find_element_by_id('fc_star_time_m'))
	s.select_by_visible_text(stime_m)
	s = Select(driver.find_element_by_id('fc_end_time_h'))
	s.select_by_visible_text(etime_h)
	s = Select(driver.find_element_by_id('fc_end_time_m'))
	s.select_by_visible_text(etime_m)
	s = Select(driver.find_element_by_name('job_title'))
	s.select_by_visible_text(job_title)
	s = Select(driver.find_element_by_name('way'))
	s.select_by_visible_text(way)
	elem = driver.find_element_by_name("objects")
	elem.send_keys(objects)
	elem = driver.find_element_by_name("cause")
	elem.send_keys(cause)
	elem = driver.find_element_by_name("contact")
	elem.send_keys(content)
	elem = driver.find_element_by_name("memo")
	elem.send_keys(memo)
	driver.execute_script('checkform()')
	btn = driver.find_element(By.XPATH, '//div[@class="ui-dialog-buttonset"]/button')
	btn.click()