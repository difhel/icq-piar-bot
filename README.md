<img src="https://github.com/mail-ru-im/bot-python/blob/master/logo.png" width="100" height="100">

# icq-piar-bot

Интерфейс ICQ User API для массовой запланированной рассылки сообщений на Python с открытым исходным кодом.

# Содержание
- [Описание](#описание)
- [Начало работы](#начало-работы)
- [Запуск и развёртывание](#запуск-и-развёртывание)
- [Послесловие от разработчика](#послесловие-от-разработчика)

# Описание

Данная программа разработана [Марком Фоминым](https://vk.com/na_official) для помощи в пиаре своих групп. Программа асинхронно в заданное время отправляет GET-запрос на сервер ICQ от лица пользователя и отсылает все указанные сообщения во все указанные чаты.
Программа обладает рядом преимуществ:
- Асинхронность. Запрос потребляет меньше оперативной памяти и времени.
- Простота. Просто вставьте нужные данные, и бот готов работать.
- Человечность. Главная особенность бота - программа отправляет сообщения как обычный пользователь, а не как бот. С ботами есть вполне актуальные проблемы: во многие рекламные чаты нельзя добавлять ботов, если вы не админ, и таких спам-ботов банят часто. Поэтому рассылка от лица пользователя решает обе этих проблемы, однако мы все равно рекомендуем использовать фейковый аккаунт.

# Начало работы
>Обратите внимание: данные действия можно выполнять ТОЛЬКО в браузере с инструментами разработчика. Здесь и далее пойдет речь о Chrome Desktop.
- Зайдите на сайт [https://mail.ru](https://mail.ru) и создайте новую почту на MailRu.
- Сохраните и запишите себе логин и пароль от нового аккаунта.
- Перейдите по ссылке [https://webagent.mail.ru](https://webagent.mail.ru) и войдите, используя логин и пароль. Проигнорируйте окно с добавлением телефона, нажав "Отмена".
    >Вуаля! У вас новый аккаунт для ICQ New, который абсолютно идентичен аккаунту ICQ. Но не спешите! Нельзя писать НИ В ОДИН ЧАТ, пока до этого не дойдёт дело!
- Зайдите в настройки и настройте имя и аватар (ник изменить нельзя).
- Теперь найдите свой основной аккаунт. Ничего ему не пишите.
- Нажмите Ctrl+Shift+I и перейдите на вкладку Network.
- Теперь крайне внимательно пишите следующий текст:
  >Привет!
  Теперь посмотрите на вкладку Network. Последняя запись должна иметь заголовок "sendIM".
- Нажимаем на неё. Видимо что-то вроде этого:

    <img src="https://raw.githubusercontent.com/nightadmin/icq-piar-bot/master/screen1.png" height="250px">
    
- Отлично. Листаем ниже:
    <img src="https://github.com/nightadmin/icq-piar-bot/blob/master/screen2.png">
- Видим текст: "Привет!". Значит, все правильно. Копируем значение поля "aimsid".
- Вставляем его в файл logic.py в значение переменной USER_AIMSID.
- В replics добавляем сообщения по порядку, в chats добавляем чаты для рассылки.
- Все сохраняем. Вкладку с аккаунтом можно закрыть, но нужно заходить в него раз в неделю и не нажимать кнопку "Выход", иначе токен перестанет быть действительным.


# Запуск и развертывание
Вы должны запустить бота на виртуальном или физическом выделенном сервере. Он стоит денег (или читайте мою статью о [сервере из старого телефона](http://icq.a0001.net/server_based_on_old_phone)).
На нем перейдите в консоль и выполните команды:
```bash
mkdir piar
cd piar
git clone https://github.com/nightadmin/icq-piar-bot.git
cd icq-piar-bot
```
Теперь бот лежит тут:
>/{директория по умолчанию}/piar/icq-piar-bot/logic.py

Отредактируйте и вставьте нужные значения (см. [Начало работы](#начало-работы)).
Теперь проверьте, что у вас установлены нужные пакеты:
```bash
pip3 install aiohttp
```

# Послесловие от разработчика
<ul>
    <li><a href="https://icq.com/botapi/">icq.com/botapi/</a></li>
    <li><a href="https://agent.mail.ru/botapi/">agent.mail.ru/botapi/</a></li>
</ul>
