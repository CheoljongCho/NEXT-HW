#session4 과제

check1 = input('''
지금부터 숫자 게임을 시작하겠습니다.
1부터 100까지의 숫자 중 하나를 생각해주세요
결정하였다면 아무 텍스트나 입력해주세요
''')

start = 1
end = 100
mid = (start + end)//2

cnt = 0
while start <= end:
  print("생각한 숫자가 "+str(mid)+" 인가요?")
  check2 = input("맞다면 '맞음', 그보다 크다면 '큼', 그보다 작다면 '작음'을 입력해주세요.")
  cnt += 1
  if check2 == "맞음":
    break
    print()
  elif check2 == "큼":
    start = (start + end)//2
    mid = (mid + end)//2
  
  else:
    end = (start + end)//2
    mid = (start + mid)//2

print("{}번 만에 성공하셨습니다!".format(cnt))