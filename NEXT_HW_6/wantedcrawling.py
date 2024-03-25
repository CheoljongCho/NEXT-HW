import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook

# 엑셀 파일 경로
file_path = 'C:/Users/Cheoljong/Desktop/NEXT/HW/NEXT_HW_6/wanted_jobpost_dev.xlsx'

# 엑셀 워크북 생성
wb = Workbook()

# 엑셀 시트 선택
ws = wb.active

# 데이터 생성
header = ["번호", "제목", "회사"]
ws.append(header)
chromedriver_path = "C:/Users/Cheoljong/Desktop/NEXT/Session6/chromedriver.exe"

user_data_dir = "C:/Users/Cheoljong/Desktop/NEXT/HW/NEXT_HW_6/cash"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome (service=service, options=chrome_options)


driver.get("https://www.wanted.co.kr/")

jobpost = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section/article[1]/ul/li[1]')
jobpost.click()
time.sleep(1)

morepost = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/article/div/div[1]/button/span[2]')
morepost.click()
time.sleep(1)

dev = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/article/div/div[1]/section/ul/li[1]/a')
dev.click()
time.sleep(1)

f5 = 0
while f5 < 8:
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(2)
  f5 += 1


for i in range(1, 101):
    names = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div[2]/ul/li[{i}]/div/a/div[2]/p').text
    companies = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div[2]/ul/li[{i}]/div/a/div[2]/span').text
    num = i
   
    print(num, names, companies)
    
    ws.append([num, names, companies])

wb.save(file_path)

print("엑셀 파일 저장 완료")