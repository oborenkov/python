# Практическое задание 8. «Работа с файлами»
# Обновлено 22.05.2023

# Усложнение задач выделены (*). Они необязательны для решения и нужны для тех, кому мало выполнить обычное задание.
# Если вы хотите решить усложненное задание - сначала сделайте задание обычной сложности.

# 8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание

# Корректность и уникальность данных не обязательны.

# Вы продлили срок сдачи задания до 27 июня, 10:00 +03:00 UTC

# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.

# 2) CRUD: Create, Read, Update, Delete

# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv

# 4) импорт данных из текстового файла формата csv

# Используйте функции для реализации значимых действий в программе

# (*) Усложнение.

# Сделать тесты для функций
# Разделить на model-view-controller
