# control_expenses

English version see below.

RUSSIAN VERSION (РУССКАЯ ВЕРСИЯ):

control_expenses.py - приложение контроль расходов.

Инструменты которые использовались при написании приложения: Python 3.9.5, mysql  Ver 8.0.26 .

Чтоб использовать приложение control_expenses.py у вас должен быть установлен Python3 последней версии и MySQL последней версии.

Скачать эти программы:
Python3 - https://www.python.org .
MySQL - https://www.mysql.com .

ЗАПУСК ПРОЛОЖЕНИЯ control_expenses.py:

1. Зарегистрируйтесь в MySQL как root пользователь. (Запомните или запишите пароль).
Пароль root пользователя базы данных MySQL будет использоваться только при регистрации нового пользователя приложения control_expenses.py .
Чтоб дать ему права доступа только к своей базе данных под совим именем user_name.
База данных пользователя user_name будет создана с таким же именем как и имя пользователя (user_name)

2. Вам нужно установить Connector/Python для соединения python с MySQl
   
   Для большинства операционных систем команда: 
   
   			pip install mysql-connector-python

   Оригинальный документ: https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html

3. Запустите файл control_expenses.py с помощюь python3.
Вы увидите в консоли:


			Контроль расходов:

			Главное меню:

			0 - Выйти из программы (Exit)
			1 - Войти (Log in)
			2 - Создать пользователя (Sing up)
			
		Ваш выбор: 

В строку "Ваш выбор:" вводятся цифры с меню 
(например: если вы хотите Создать пользователь нужно ввести цифру 2 и нажать Enter).

4. При создании пользователя вам нужно будет ввести пароль root пользователя MySQL из пункта 1. 
Потом ввести имя которое вы выбрали для пользователя и пароль. 
Пароль нужно будет ввести два раза для правильности.
Пароль root пользователя базы данных MySQL будет использоваться только при регистрации нового пользователя приложения.
Чтоб дать ему права доступа только к своей базе данных под совим именем user_name.
База данных пользователя user_name будет создана с таким же именем как и имя пользователя (user_name)

Пример:

			Пароль root пользователя: password
			Введите имя пользователя: user_name
			Введите парлоль для пользователя user_name : password
			Введите для проверки пароль пользователя user_name : password

После этого будет сообщение про успех и приложение выйдет в главне меню.
Пример:

			Поздравляем: пользователь user_name создан!
			Для создание контроля расходов
			выполните вход (1 - Log in) под своим иминем и парлолем

			Контроль расходов:

			Главное меню:

			0 - Выйти из программы (Exit)
			1 - Войти (Log in)
			2 - Создать пользователя (Sing up)

		Ваш выбор: 

5. Войдите в приложение (введите цифру - 1) в строку "Ваш выбор: 1" и нажмите Enter.

			Вы вошли как пользователь: user_name

			Контроль расходов:

			Меню пользователя: 

			0 - Выйти (Log out)
			1 - Внести расход
			2 - Статистика расходов
			3 - Удалить данные
	
		Ваш выбор:

6. В "Меню пользователя" Если захотите ввести расход введите цифру - 1, 
просмотреть статистику расходов введите цифру - 2, 
удалить расходы введите цифру - 3 и нажмите Enter.

7. В пункте "1 - Внести расход" расходы можно вносить за сегодняшнее число 
(приложение вводит число автоматически) и за лобое число выбранное вами.
Примечание: при выборе пункта "2 - Внести расход и внести дату"
Придерживайтесь правильного формат (формат: ГГГГ-ММ-ДД)
Например: 2021-10-11 
Сначала идет год, потом месяц, потом день. Обязательно ставте дефисы.

			Вы вошли как пользователь: user_name

			Контроль расходов:

			Меню пользователя -> Внести расход:

			0 - Выйти в меню пользователя
			1 - Внести расход за сегодня
			2 - Внести расход и внести дату

		Ваш выбор: 


8. В пункте "2 - Статистика расходов" можно просмотреть всю статистику расходов, 
Статистику по конкретной категории и статистику расходов по дате.
Примечание: при выборе пункта "3 - Статистика по дате"
Придержуйтесь правильного форматф (формат: ГГГГ-ММ-ДД)
Например: 2021-10-11

			Вы вошли как пользователь: user_name

			Контроль расходов:

			Меню пользователя -> Статистика расходов: 

			0 - Выйти в меню пользователя
			1 - Статистика по всем категориям
			2 - Статистика по названию категории
			3 - Статистика по дате

		Ваш выбор: 



			Вы вошли как пользователь: user_name

			Контроль расходов:

			Меню пользователя -> Статистика расходов ->
			-> Статистика расходов по дате: 

			0 - Выйти в статистику расходов
			1 - Статистика полная дата (формат: ГГГГ-ММ-ДД)
			2 - Статистика за день (формат: ДД)
			3 - Статистика за месяц (формат: ММ)
			4 - Статистика за год (формат: ГГГГ)
				
		Ваш выбор: 
9. В пункте "3 - Удалить данные" удаляются все внесенные вами расходы.
			
			Вы вошли как пользователь: user_name

			Контроль расходов:

			Меню пользователя -> Удалить данные:

			0 - Выйти в меню пользователя
			1 - Да (Yes)
			2 - Нет (No)
			
		Вы хотите удалить все ваши дынные?:
		
10. Что бы выйти из любого меню в предыдущее меню введите - 0 (ноль) и нажмите Enter. Выход с главного меню выходит с приложения и разлогинивает пользователя.

----------------------------------------------------------------------------------------------------

CONTROL_EXPENSES

ENGLISH VERSION:

control_expenses.py - Expense control application.

Tools used to write the application: Python 3.9.5, mysql Ver 8.0.26.

To use the control_expenses.py application you must have the latest version of Python3 and the latest version of MySQL installed.

Download these programs: Python3 - https://www.python.org . MySQL - https://www.mysql.com .

RUNNING AN APP control_expenses.py:

1. Log in to MySQL as root user. (Remember or write down the password).
The MySQL database user root password will only be used when registering a new application user control_expenses.py.
To give him access rights only to his database under the same name (user_name).
The user database (user_name) will be created with the same name as the username (user_name).

2. You need to install Connector / Python to connect python to MySQl

	For most operating systems, the command is:

		pip install mysql-connector-python

	Original document: https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html

3. Run the control_expenses.py file with python3. You will see in the console:

	 		Контроль расходов:

 			Главное меню:

 			0 - Выйти из программы (Exit)
 			1 - Войти (Log in)
 			2 - Создать пользователя (Sing up)
 	
 		Ваш выбор:

In the line "Your choice:" are entered numbers from the menu (for example: if you want to Create a user, you need to enter the number 2 and press Enter).

4. When creating a user, you will need to enter the MySQL root user password from step 1.
Then enter the name you have chosen for the user and the password.
The password will need to be entered twice to be correct.
The MySQL database user root password will only be used when registering a new application user.
To give him access rights only to his own database under the name user_name.
The user database user_name will be created with the same name as the username (user_name)

Example:

			Пароль root пользователя: password
			Введите имя пользователя: user_name
			Введите парлоль для пользователя user_name : password
			Введите для проверки пароль пользователя user_name : password

After that, there will be a message about success and the application will be released in the main menu. Example:

			Поздравляем: пользователь user_name создан!
			Для создание контроля расходов
			выполните вход (1 - Log in) под своим иминем и парлолем

			Контроль расходов:

			Главное меню:

			0 - Выйти из программы (Exit)
			1 - Войти (Log in)
			2 - Создать пользователя (Sing up)

		Ваш выбор:

5. Enter the application (enter the number - 1) in the line "Your choice: 1" and press Enter.

 			Вы вошли как пользователь: user_name

 			Контроль расходов:

 			Меню пользователя: 

 			0 - Выйти (Log out)
 			1 - Внести расход
 			2 - Статистика расходов
 			3 - Удалить данные

 		Ваш выбор:

6. In the "User menu" If you want to enter the flow rate, enter the number - 1,
view expense statistics enter the number - 2,
delete costs enter the number - 3 and press Enter.

7. In paragraph "1 - Add expense" expenses can be entered for today 's date (the application enters the number automatically) and for the number chosen by you.
Note: when selecting the item "2 - Enter consumption and enter the date" Adhere to the correct format (format: YYYY-MM-DD)
For example: 2021-10-11 First comes the year, then the month, then the day. Be sure to use hyphens.

	 		Вы вошли как пользователь: user_name

 			Контроль расходов:

 			Меню пользователя -> Внести расход:

 			0 - Выйти в меню пользователя
 			1 - Внести расход за сегодня
 			2 - Внести расход и внести дату

 		Ваш выбор:

8. In paragraph "2 - Expense Statistics", you can view all expense statistics, statistics for a specific category, and expense statistics by date.
Note: when selecting the item "3 - Statistics by date", adhere to the correct format (format: YYYY-MM-DD) For example: 2021-10-11

 			Вы вошли как пользователь: user_name

 			Контроль расходов:

 			Меню пользователя -> Статистика расходов: 

 			0 - Выйти в меню пользователя
 			1 - Статистика по всем категориям
 			2 - Статистика по названию категории
 			3 - Статистика по дате

 		Ваш выбор: 



 			Вы вошли как пользователь: user_name

 			Контроль расходов:

 			Меню пользователя -> Статистика расходов ->
 			-> Статистика расходов по дате: 

 			0 - Выйти в статистику расходов
 			1 - Статистика полная дата (формат: ГГГГ-ММ-ДД)
 			2 - Статистика за день (формат: ДД)
 			3 - Статистика за месяц (формат: ММ)
 			4 - Статистика за год (формат: ГГГГ)
 		
 		Ваш выбор:

9. In paragraph "3 - Delete data" all costs you have entered are deleted.

 			Вы вошли как пользователь: user_name

 			Контроль расходов:

 			Меню пользователя -> Удалить данные:

 			0 - Выйти в меню пользователя
 			1 - Да (Yes)
 			2 - Нет (No)
 	
 		Вы хотите удалить все ваши дынные?:

10. To exit any menu in the previous menu, enter - 0 (zero) and press Enter.
Exit from the main menu exits the application and logs out the user.


