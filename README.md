# Описание проекта
Этот проект представляет собой Telegram-бота, предназначенного для рекомендаций книг на английском языке пользователям согласно выбранному уровню владения языком и предпочитаемому жанру литературы.

# Функционал
`/start`
Запускает работу бота. После ввода этой команды пользователь получает приветственное сообщение с описанием возможностей бота и списком основных команд. 

Пример ответа:

_Привет! Я помогу тебе найти интересные книги на английском языке. Используй следующие команды:
/help, /recommend, /random_book_

`/help`
Команда выводит инструкцию по использованию бота. Она содержит перечень всех доступных команд и пояснения к каждой из них. Она служит руководством для пользователей, желающих узнать больше о возможностях бота и правильном способе их использования.

После ввода команды /help пользователь получает сообщение:

_/start — запустить бота_

_/help — инструкция по использованию_

_/recommend <уровень> <жанр> — получить рекомендации_

_/random_book — случайная книга на английском_

`/recommend`
Основная команда бота. Пользователь вводит сначала название уровня языка (А1,А2,B1,B2,C1) и затем жанра (фантастика, классика и тд) по которой он хотел бы получить рекомендации.
Вот несколько книг уровня A1 в жанре classic:

Пример ответа:

_📖 Alice's Adventures in Wonderland — A whimsical and classic tale of Alice's adventures in a fantastical world._

_📖 The Little Prince — A young prince visits Earth, meeting several characters that teach valuable life lessons._

_📖 The Tale of Peter Rabbit — The story of the mischievous Peter Rabbit and his adventures in Mr. McGregor's garden._

_📖 The Ugly Duckling — The story of a little bird who grows into a beautiful swan._

_📖 The Velveteen Rabbit — A toy rabbit wants to become real through the love of a child._

`/random_book`
Если пользователь затрудняется выбрать жанр, эта команда предлагает случайную книгу на английском языке. Бот генерирует рекомендацию, исходя из базы данных популярных произведений разных жанров.

Пример ответа:

_📚 Dune — A young nobleman must protect his family and control a vital spice on a desert planet.
Уровень: B2, жанр: science_fiction_

# Инструкция по запуску
1. Создайте виртуальное окружение Python командой:
```html 
python -m venv .venv
```

2. Установите необходимые библиотеки:
```html 
pip install aiogram==2.25.2
```

3. Запустите бот через файл main.py, выполнив команду:
```html 
python main.py
```

# Готово!
