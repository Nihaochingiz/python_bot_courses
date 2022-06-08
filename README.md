# python_bot_courses

This is a bot for recording users for a real estate course
Added the pyTelegramBotApi and gspread libraries
1. The bot asks the user if he would like to enroll in the course
2. Next, the bot asks for the phone (checks the phone with a regular expression)
3. Then asks for the Name
4. Adds data to the user_data array
5. Next name, phone number and date
7. The last step of user_data is sent via Google docs, columns are filled in the table - name, phone number, and date of entry.

Это бот для записи пользователей для курса по недвижимости
Добавлены библиотеки pyTelegramBotApi и gspread
1. Бот спрашивает пользователя хотел бы он записаться на курс
2. Далее Бот спрашивает телефон(проверяет телефон регулярным выражением)
3. Потом спрашивает Имя
4. Добавляет данные в массив user_data
5. Далее имя, телефон и дата
7. Последний шаг user_data отправляется по google docs в табличку заполняются столбцы - имя, номер телефона, и дата записи.
