import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

token = "xoxb-토큰 값" #슬랙 토큰 값
channel = "#project-message" #슬랙 채널 이름
#text = "{0}\n합격자 발표 페이지 변동 발생!!!".format(str(datetime.today())[:19])
url = "채용홈페이지 주소"

while True:
    now_time = str(datetime.today())[:19]
    if now_time >= "2021-09-10 08:00:00":
        print(str(datetime.today())[:19])
        print("*****  채용홈페이지 변동사항 추적을 시작합니다  *****")
        requests.post("https://slack.com/api/chat.postMessage", headers={"Authorization": "Bearer " + token},
                      data={"channel": channel,
                            "text": "{0}\n채용홈페이지 변동사항 추적을 시작합니다".format(str(datetime.today())[:19])})
        while True:
            req = requests.get(url)
            html = req.text
            soup = BeautifulSoup(req.content.decode('euc-kr', 'replace'), 'html.parser') #바로 크롤링 해오면 한글 깨짐 현상때문에 디코딩 과정 추가
            target_text = soup.select('td > font')[0].text #특정 태그 값을 검사
            if target_text == "합격자발표 시간이 아닙니다.":
                print(str(datetime.today())[:19])
                print("OOOOO  일 치  OOOOO")
            else:
                print(str(datetime.today())[:19])
                print("XXXXX  불 일 치  XXXXX")
                requests.post("https://slack.com/api/chat.postMessage", headers={"Authorization": "Bearer " + token},
                              data={"channel": channel,
                                    "text": "{0}\n!!!합격자 발표 페이지 변동 발생!!!".format(str(datetime.today())[:19])})
            time.sleep(60)
    else:
        print(now_time)
        print("^^^^^ 아직 시간이 되지 않았습니다 ^^^^^") #서버 및 내 컴퓨터에 대한 부하를 줄이기 위해 발표 날 아침부터 모니터링 시작
        time.sleep(60)
