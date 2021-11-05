# mysql.connector для работы с базами данных (MySql)
import mysql.connector
from mysql.connector import errorcode
# getpass для ввода пароля чтоб его не видели
from getpass import getpass
# datetime для получения сегодняшенй даты
from datetime import date

# create_use_database_table: создает нового пользователья, создает для него базу данных называемую именем пользователя,
# создает таблицу в этой базе данные с названием cost и дает права пользователю только на его базу данных и таблицу
def create_use_database_table_access():
	try:
		# подключаемся к серверу как root пользователь для создания нового пользователя его базы данны, его таблицы
		# и для того чтоб дать ему права только на его базу данных
		cnx = mysql.connector.connect(host='localhost', user="root", password=getpass("Пароль root пользователя: "))
		# создаем соединение
		cursor = cnx.cursor()
		# вводим с консоли имя пользователя и пароль
		user_name = input("Введите имя пользователя: ")
		user_password = getpass("Введите парлоль для пользователя " + user_name + " : ")
		user_password_check = getpass("Введите для проверки пароль пользователя " + user_name + " : ")

		if user_password == "" or user_name == "\n":
			print("\nПароль не может быть пустой строкой")
			return
		if user_password == user_password_check:
			# создаем пользователя
			query = ("create user \'" + user_name + "\'@" + "\'localhost\'" + " IDENTIFIED BY \'" + user_password + "\'")
			cursor.execute(query)
			# создаем базу данных пользователья
			query = ("create database " + user_name + " character set utf8")
			cursor.execute(query)
			# юзаем базу данных пользователья
			query = ("use " + user_name)
			cursor.execute(query)
			# создаем таблицу
			query = ("create table cost "
				   +"(category_id smallint unsigned auto_increment, expense_category varchar(100),"
				   +"sum float, date_purchase date, constraint pk_category primary key (category_id))")
			cursor.execute(query)
			# даем права пользователья только к своей базе данных и таблице
			cursor.execute("GRANT ALL PRIVILEGES ON " 
						  + user_name + "." + "cost" + " TO "+ "\'"+user_name+"\'"+"@"+"'localhost'")
			# закрываем соединение
			cnx.close()
			cursor.close()
			# сообщения об успехе
			print("\nПоздравляем: пользователь " + user_name + " создан!")
			print("Для создание контроля расходов\nвыполните вход (1 - Log in) под своим иминем и парлолем")
		else:
			print("\nПароли не совпали попробуйте еще раз!")
	except mysql.connector.Error as err:
		print("\nНепралильное имя или пароль root пользовтеля\nили пользователь с таким именем уже существует!")
	else:
		cnx.close()
		cursor.close()

# format_statistics: выводит на стандартный вовод форматированную статистику
def format_statistics(cursor):
	full_id = 0 # всего категоий
	full_x_sum = 0.0 # общая сумма
	print("")
	print(" -------------------------------------------------------")
	print("%7s %15s %10s %20s" % ("номер"+"|", "категория"+"|", "цена"+"|", "дата приобретения"+"|"))
	print(" -------------------------------------------------------")
	for x in cursor:
		c_id,e_category,x_sum,date = x
		print("%7s %15s %10s %20s" % (str(c_id)+"|",e_category+"|",str(x_sum)+"|",str(date)+"|"))
		full_id += 1
		full_x_sum += x_sum
	print(" -------------------------------------------------------")
	print(" Всего категорий: ", full_id, "|  Общая сумма: ", full_x_sum)
	print(" -------------------------------------------------------")
	print("")

# statistics: выводит статистику расходов по категориям:
# статистика по всем категориям, cтатистика по названию категории, статистика расходов по дате
def statistics(user_name, cnx, cursor):
	choice_expense = None
	while choice_expense  != "0":
		print("\n\t\t\tВы вошли как пользователь: " + user_name)
		print(
		"""
			Контроль расходов:

			Меню пользователя -> Статистика расходов: 

			0 - Выйти в меню пользователя
			1 - Статистика по всем категориям
			2 - Статистика по названию категории
			3 - Статистика по дате

		""")
		choice_expense = input("Ваш выбор: ")
		# выводим всю статистику
		if choice_expense == "1":
			query = ("select * from cost")
			cursor.execute(query)
			# выводим форматированную статистику на экран
			format_statistics(cursor)
		# статистика по названию категории
		elif choice_expense == "2":
			expense = input("Введите категорию: ")
			query = ("select category_id, expense_category, sum, date_purchase "
					+"from cost where expense_category = '"+expense+"'")
			cursor.execute(query)
			# выводим форматированную статистику на экран
			format_statistics(cursor)
		# статистика по дате
		elif choice_expense == "3":
			choice_date = None
			while choice_date != "0":
				print("\n\t\t\tВы вошли как пользователь: " + user_name)
				print(
				"""
			Контроль расходов:

			Меню пользователя -> Статистика расходов ->
			-> Статистика расходов по дате: 

			0 - Выйти в статистику расходов
			1 - Статистика полная дата (формат: ГГГГ-ММ-ДД)
			2 - Статистика за день (формат: ДД)
			3 - Статистика за месяц (формат: ММ)
			4 - Статистика за год (формат: ГГГГ)
				""")				
				choice_date = input("Ваш выбор: ")
				# перехватываем ошибку формата даты (формат: ГГГГ-ММ-ДД)
				try:
					if choice_date == "1":
						choice_full = input("Введите дату полную дату (формат: ГГГГ-ММ-ДД): ")
						query = ("select category_id, expense_category, sum, date_purchase "
								+"from cost where date_purchase = '"+choice_full+"'")
						cursor.execute(query)
						# выводим форматированную статистику на экран
						format_statistics(cursor)
					elif choice_date == "2":
						choice_dd = input("Введите число дня месяца (формат: ДД): ")
						query = ("select category_id, expense_category, sum, date_purchase "
								+"from cost where date_purchase like '____-__-"+choice_dd+"'")
						cursor.execute(query)
						# выводим форматированную статистику на экран
						format_statistics(cursor)
					elif choice_date == "3":
						choice_mm = input("Введите месяц (формат: ММ): ")
						query = ("select category_id, expense_category, sum, date_purchase "
								+"from cost where date_purchase like '____-"+choice_mm+"-__'")
						cursor.execute(query)
						# выводим форматированную статистику на экран
						format_statistics(cursor)
					elif choice_date == "4":
						choice_gggg = input("Введите год (формат: ГГГГ): ")
						query = ("select category_id, expense_category, sum, date_purchase "
								+"from cost where date_purchase like '"+choice_gggg+"-__-__'")
						cursor.execute(query)
						# выводим форматированную статистику на экран
						format_statistics(cursor)
				except mysql.connector.Error as err:
  					print("\nОшибка неправильный формат даты!\nПопробуйте еще раз.")

# внеести данные в таблицу cost базы данных пользователя
def use_table(user_name, cnx, cursor):
	choice_make = None
	while choice_make != "0":
		print("\n\t\t\tВы вошли как пользователь: " + user_name)
		print(
		"""
			Контроль расходов:

			Меню пользователя -> Внести расход:

			0 - Выйти в меню пользователя
			1 - Внести расход за сегодня
			2 - Внести расход и внести дату

		""")
		choice_make = input("Ваш выбор: ")
		# перехватываем ошибук формата даты (формат: ГГГГ-ММ-ДД)
		try:
			# внести расход за сегодня
			if choice_make == "1":
				category = input("Введите категорию расхода: ")
				category_sum = input("Введите сумму: ")
				# сегодняшняя дата
				current_date = str(date.today())
				# создаем запрос
				query = ("insert into cost (category_id, expense_category, sum, date_purchase) "
						+"values (null, '"+category+"', '"+category_sum+"', '"+current_date+"')")
				# выполняем запрос
				cursor.execute(query)
				# Make sure data is committed to the database
				# Фиксируем изменения в таблице
				cnx.commit()
				# сообщение успеха
				print("\nРасход внесен.")
			# внести расход и дату
			elif choice_make == "2":
				category = input("Введите категорию расхода: ")
				category_sum = input("Введите сумму: ")
				current_date = input("Введите дату (формат: ГГГГ-ММ-ДД): ")
				# создаем запрос
				query = ("insert into cost (category_id, expense_category, sum, date_purchase) "
						+"values (null, '"+category+"', '"+category_sum+"', '"+current_date+"')")
				# выполняем запрос
				cursor.execute(query)
				# Make sure data is committed to the database
				# Фиксируем изменения в таблице
				cnx.commit()
				# сообщение успеха
				print("\nРасход внесен.")
		except mysql.connector.Error as err:
  			print("\nОшибка неправильный формат даты!\nПопробуйте еще раз.")

# удалить данные пользователья с таблицы
def del_data(user_name, cnx, cursor):
	del_data = None
	while del_data  != "0":
		print("\n\t\t\tВы вошли как пользователь: " + user_name)
		print(
		"""
			Контроль расходов:

			Меню пользователя -> Удалить данные:

			0 - Выйти в меню пользователя
			1 - Да (Yes)
			2 - Нет (No)
		""")
		del_data = input("Вы хотите удалить все ваши дынные?: ")
		if del_data == "1":
			# создаем запрос
			query = ("delete from cost")
			# выполняем запрос
			cursor.execute(query)
			# Фиксируем изменения в таблице
			cnx.commit()
			# обнуляем счетчик auto increment в таблице cost для category_id
			query = ("alter table cost AUTO_INCREMENT = 1")
			# выполняем запрос
			cursor.execute(query)
			# сообщение про успех удаления данных
			print("\nВаши данные были удалены!")
			del_data = "0"
		elif del_data == "2":
			del_data = "0"

# user: вход как зарегестрированный пользователь
def user():
	# перехватываем исключения (ошибки)
	try:
		user_name = input("Введите имя пользователя: ")
		# подключаемся к серверу
		cnx = mysql.connector.connect(host='localhost', user=user_name, password=getpass("Пароль пользователя: "))
		# создаем соединение
		cursor = cnx.cursor()
		# подключаемся к базе данных пользователя
		query = ("use " + user_name)
		cursor.execute(query)

		# выбор пользователя
		choice_user = None
		while choice_user != "0":
			print("\n\t\t\tВы вошли как пользователь: " + user_name)
			print(
			"""
			Контроль расходов:

			Меню пользователя: 

			0 - Выйти (Log out)
			1 - Внести расход
			2 - Статистика расходов
			3 - Удалить данные

			""")
			choice_user = input("Ваш выбор: ")
			# закрываем соединение с базой данный выходим в главное меню
			if choice_user == "0":
				cnx.close()
				cursor.close()
			# внесение расходов
			elif choice_user == "1":
				use_table(user_name, cnx, cursor)
			# просмотерть статистику
			elif choice_user == "2":
				statistics(user_name, cnx, cursor)
			# удалить данные расходов
			elif choice_user == "3":
				del_data(user_name, cnx, cursor)
	# если былоа ошибки при наботе имени или пароля
	except mysql.connector.Error as err:
  		print("")
  		print("Непралильное имя или пароль пользовтеля или его не существует!")

# main: приложение для контроля расходов
def main():
	choice = None
	while choice != "0":
		print(
			"""
			Контроль расходов:

			Главное меню:

			0 - Выйти из программы (Exit)
			1 - Войти (Log in)
			2 - Создать пользователя (Sing up)
			""")
		choice = input("Ваш выбор: ")
		print("")
		# выход
		if choice == "0":
			print("До свидания.")
		# входим как пользователь
		elif choice == "1":
			user()
		# создать пользователья
		elif choice == "2":	
			create_use_database_table_access()

# основная программа
main()


