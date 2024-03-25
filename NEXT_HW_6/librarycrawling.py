import time
from bs4 import BeautifulSoup as bs
import requests
from openpyxl import Workbook

url='https://library.korea.ac.kr/datause/advanced-search/advanced-search-form/advanced-search-result/?verb=detail&target=catalog&st=KWRD&lmt0[]=TOTAL&lmtsn0=000000000001&lmtst0=OR&lmt1=TOTAL&lmt2=TOTAL&fi1=TOTAL&q1=%EC%8B%AC%EB%A6%AC%EC%B2%A0%ED%95%99'

try:
  headers = {
    
  }
  response = requests.get(url, headers=headers)
  
  if response.status_code == 200:
    html_text = response.text
    
    soup = bs(response.text, 'html.parser')
    
    #책 제목
    titles=soup.select('h4 a')
    titles = list(map(lambda x: x.text.replace('<highlight>','').replace('</highlight>',''), titles))
    #print(titles)

    #wjwk
    authors=soup.select('.item-author')
    authors = list(map(lambda x: x.text.replace('\n\t\t\t\t\t\t\t\t\t\t','').replace('\n\t\t\t\t\t\t\t\t\t',''), authors))
    print(authors)
    
    presses=soup.select('.item-pub')
    presses = list(map(lambda x: x.text.replace('\n\t\t\t\t\t\t\t\t\t\t','').replace('\n\t\t\t\t\t\t\t\t\t',''), presses))
    print(presses)
    
    wb = Workbook()
    ws = wb.active
  
    ws.append(["순서", "제목", "저자", "출판사"])
  
    for i, (title, author, press) in enumerate(zip(titles, authors, presses), start=1):
      ws.append([i, title, author, press])
  
    file_path = 'C:/Users/Cheoljong/Desktop/NEXT/HW/NEXT_HW_6/philsophy_of_mind_book.xlsx'
    wb.save(file_path)
    print("엑셀 파일 저장 완료")
  
  else:
    print(f"Error: HTTP 요청 실패. 상태 코드: {response.status_code}")
    
except requests.exceptions.RequestException as e:
  print(f"Error: 요청 중 오류 발생, 오류 메시지: {e}")
  
  