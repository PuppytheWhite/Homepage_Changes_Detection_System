import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

token = "xoxb-2465671549126-2496058717824-6Lrli9Pb0PNCOIks6u6COJMz"
channel = "#project-message"
#text = "{0}\n합격자 발표 페이지 변동 발생!!!".format(str(datetime.today())[:19])
url = "https://kbsec.incruit.com/success/index.asp?projectid=102"

while True:
    now_time = str(datetime.today())[:19]
    if now_time >= "2021-09-10 08:00:00":
        print(str(datetime.today())[:19])
        print("*****  KB증권 채용홈페이지 변동사항 추적을 시작합니다  *****")
        requests.post("https://slack.com/api/chat.postMessage", headers={"Authorization": "Bearer " + token},
                      data={"channel": channel,
                            "text": "{0}\nKB증권 채용홈페이지 변동사항 추적을 시작합니다".format(str(datetime.today())[:19])})
        while True:
            req = requests.get(url)
            html = req.text
            soup = BeautifulSoup(req.content.decode('euc-kr', 'replace'), 'html.parser')
            target_text = soup.select('td > font')[0].text
            if target_text == "합격자발표 시간이 아닙니다.":
                print(str(datetime.today())[:19])
                print("OOOOO  일 치  OOOOO")
            else:
                count = 0
                while True:
                    print(str(datetime.today())[:19])
                    print("XXXXX  불 일 치  XXXXX")
                    requests.post("https://slack.com/api/chat.postMessage", headers={"Authorization": "Bearer " + token},
                                  data={"channel": channel,
                                        "text": "{0}\n!!!!!  합격자 발표 페이지 변동 발생  !!!!!".format(str(datetime.today())[:19])})
                    count = count + 1
                    time.sleep(1)
                    if count == 1800: #30분 동안 메세지를 보냄
                        break
                break

            time.sleep(60)
        break
    else:
        print(now_time)
        print("^^^^^ 아직 시간이 되지 않았습니다 ^^^^^")
        time.sleep(60)
print("*****  결과가 어떻게 나왔나요?  *****")