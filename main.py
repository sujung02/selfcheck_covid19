from datetime import datetime
import hcskr
import schedule
import time


def main():
    name = "홍길동"
    birth = "010203"
    level = "고등학교"
    region = "경기"
    school = "○○고"
    password = "1234"
    customloginname = ""

    data = hcskr.selfcheck(name,birth,region,school,level,password,customloginname)
    print(name + "님 " + data['message'] + " -> " + "커스텀 네임 : " + customloginname)
    print("{0} 완료. ".format(time_set))

time_set = "07:10"
schedule.every().day.at(time_set).do(main)


while True:
    schedule.run_pending()
    print("현재 시간 : {0}".format(datetime.now()))
    time.sleep(10)
