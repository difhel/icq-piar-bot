import requests, time, schedule
from random import choice

USER_AIMSID = ["XXX.XXXXXXXXXX.XXXXXXXXXX:XXXXXXXXX"]

chats = ["752738404"]
replics = ["Привет! Подписывайся на наши каналы ниже!", "https://icq.im/na_group"]
def setup():
    for i in chats:
        for j in replics:
            API_URL = "https://u.icq.net/api/v53/wim/im/sendIM?aimsid={token}&t={chatId}&message={text}&mentions=&f=json".format(token=choice(USER_AIMSID), chatId=i, text=j)
            r = requests.get(API_URL)
            print("Запрос выполнен. Попытка отправки сообщения \"{m}\" в чат \"{c}\".".format(m=j, c=i))
            print("Результат:")
            print(r.json())

    
schedule.every().day.at("07:01").do(setup)
schedule.every().day.at("08:02").do(setup)
schedule.every().day.at("09:03").do(setup)
schedule.every().day.at("10:04").do(setup)
schedule.every().day.at("11:05").do(setup)
schedule.every().day.at("12:06").do(setup)
schedule.every().day.at("13:07").do(setup)
schedule.every().day.at("14:08").do(setup)
schedule.every().day.at("15:09").do(setup)
schedule.every().day.at("16:10").do(setup)
schedule.every().day.at("17:11").do(setup)
schedule.every().day.at("18:12").do(setup)
schedule.every().day.at("19:13").do(setup)
schedule.every().day.at("20:14").do(setup)
schedule.every().day.at("21:15").do(setup)
schedule.every().day.at("22:03").do(setup)
schedule.every().day.at("23:17").do(setup)

while True:
    schedule.run_pending()
    time.sleep(1)
