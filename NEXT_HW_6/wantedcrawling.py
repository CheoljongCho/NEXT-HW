import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

file = open('wantedjobpostdev', mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["num", "name","company"])

for i in range(1, 101):
    name = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div[2]/ul/li[{i}]/div/a/div[2]/p').text
    company = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div[2]/ul/li[{i}]/div/a/div[2]/span').text
    num = i
   
    print(num, name, company)

file.close()