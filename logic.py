import asyncio, aiohttp, time, schedule

USER_AIMSID = "XXX.XXXXXXXXXX.XXXXXXXXXX:XXXXXXXXX"

chats = ["752738404"]
replics = ["Привет! Подписывайся на наши каналы ниже!", "https://icq.im/na_group"]
async def main():

    async with aiohttp.ClientSession() as session:
        for i in chats:
            for j in replics:
                API_URL = "https://u.icq.net/api/v51/wim/im/sendIM?aimsid={token}&t={chatId}&message={text}&mentions=&f=json".format(token=USER_AIMSID, chatId=i, text=j)
                async with session.get(API_URL) as response:
                print("Отправка сообщения {1} в чат {2}".format(1=j, 2=i))
                print("Статус:", response.status)
                print("Content-type:", response.headers['content-type'])
                html = await response.text()
                print("Результат:", html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
def setup():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
schedule.every().day.at("19:00").do(setup)
while True:
    schedule.run_pending()
    time.sleep(1)
