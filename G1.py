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
import sys

def get_list(sheet):
    return [sheet.row_values(row) for row in range(sheet.nrows)]

#ADD
s = input("檔案名稱:\n")
try:
    wb = xlrd.open_workbook(s)
except:
    print(f'找不到{s!r},請放在同一個資料夾內')
    sys.exit(0)
sheet = wb.sheet_by_index(0)
list = get_list(sheet)

date_format = '%Y-%m-%d'
district_jiaobao = ["1-1","1-2","1-4","2-2","2-8","3-5","3-2","3-7"]
driver = webdriver.Chrome()
driver.get("http://192.168.1.4:8080/?fbclid=IwAR2xk3BV_2iDu_z721JMYoVcdOkvEY6I-Nd27Bx604eBSnkvOzYgnvdV05g")

#login
elem = driver.find_element_by_name("user_id")
s = input("帳號:\n")
elem.send_keys(s)
#elem.send_keys("df_byadofu")
elem = driver.find_element_by_name("password")
s = input("密碼:\n")
elem.send_keys(s)
#elem.send_keys("Q223553582d@")
elem = driver.find_element_by_name("confirm")
s = input("驗證碼:\n")
elem.send_keys(s)
btn = driver.find_element(By.XPATH, '//button')
btn.click()

for i in range(sheet.nrows):
    district = list[i][0]
    name = list[i][1]
    category = list[i][2]
    date = list[i][3]
    memo = list[i][4]
    training_category = list[i][5]
    if category == '生活紀錄':
        str1 = 'liferecord' 
    elif category == '訓練紀錄':
        str1 = 'training'
    elif category == '就醫紀錄':
        str1 = 'medical'
    elif category == '特殊行為紀錄':
        str1 = 'behavior'
    elif category == '分析處遇':
        str1 = 'analysisWrite'
    elif category == '輔導員評析':
        str1 = 'comment'
    else:
        print(category + ' 為不合法的選項')
        continue
    
    driver.get("http://192.168.1.4:8080/life_record.jsp")
    s = Select(driver.find_element_by_id('s_area'))
    s.select_by_visible_text(district)
    s = Select(driver.find_element_by_id('s_si_id'))
    s.select_by_visible_text(name)
    btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
    driver.execute_script("arguments[0].click()", btn)
    tbody = driver.find_element(By.XPATH, '//table[@id="simple-table"]/tbody')
    links = tbody.find_elements(By.TAG_NAME, 'a')
    print(f'新增:{name}-{category}')
    if len(links) > 1:
        link = links[1].get_attribute('href')
        driver.get(link)   
        script = f"add_item('{str1}_table')"
        driver.execute_script(script)
        tbody = driver.find_element_by_id(f'{str1}_tbody')
        trs = tbody.find_elements(By.TAG_NAME, 'tr')
        script = f"document.querySelectorAll(\"input[name='{str1}_date']\")[%d].value = {date!r}" % (len(trs)-1)
        driver.execute_script(script)
        script = f"document.querySelectorAll(\"textarea[name='{str1}_memo']\")[%d].value = {memo!r}" % (len(trs)-1)
        driver.execute_script(script)
        if category == '訓練紀錄':
            s = Select(driver.find_element_by_id('training_selection'))
            ops = s.options
            for op in ops:
                if op.text[:4] == training_category:
                    s.select_by_visible_text(op.text)
                    break
        script = f"save_item({str1!r}, %d)" % (len(trs))
        driver.execute_script(script)
    #s = input(f"{category}\n")
print('succeed!')
sys.exit(0)