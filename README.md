# Vitaliy_Avdoshkin_CourseWork_5

# Проект по БД

## Описание

В рамках проекта вам необходимо получить данные о компаниях и вакансиях с сайта hh.ru,
спроектировать таблицы в БД PostgreSQL и загрузить полученные данные в созданные таблицы.

## Установка:

1. Клонируйте репозиторий:

```
git clone https://github.com/Vitaliy-Avdoshkin/vitaliy_avdoshkin_CourseWork_5
```
## Конфигурация
1. Создайте виртуальное окружение poetry.

```
poetry env
```

2. Установите библиотеки Flake8, black, isort, mypy в группу lint.

```commandline
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
```

3. Создайте файл .flake8 для настройки библиотеки flak8


4. Настройте установленные библиотеки, используя кода ниже

Файл .flake8

```
[flake8]
max-line-length = 119
```

5. Установите библиотеки requests и dotenv
````commandline
poetry add requests
poetry add python-dotenv
````

6. Установите библиотеку psycopg2 для работы с БД
````commandline
poetry add psycopg2
````

# Модули

## Модуль main.py
В модуле реализована основная работа по взаимодействию с пользователем.
Создана функция взаимодействия с пользователем - main.

## Модуль db_class.py

Содержит класс DBManager для работы с БД.
У данного класса есть несколько методов:

```get_companies_and_vacancies_count```
Метод получает список всех компаний и количество вакансий у каждой компании

```get_all_vacancies```
Метод получает список всех вакансий с указанием названия компании,
названия вакансии и зарплаты и ссылки на вакансию

```get_avg_salary```
Метод получает среднюю зарплату по вакансиям

```get_vacancies_with_higher_salary```
Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям

```get_vacancies_with_keyword```
Метод получает список всех вакансий,
в названии которых содержатся переданные в метод слова, например python


## Модуль db_connect.py

Содержит функцию ```connect_params```,
которая получает список параметров из файла data/database.ini для подключения к БД.
Файл имеет следующий вид и не коммитится с GitHub.
```
[postgresql]
host=localhost
user=postgres
password='Укажите свой пароль'
```

## Модуль get_vacancy.py

Содержит класс HH.
В модуле реализован функционал по подключению к сайту hh.ru, используя API.
С помощью методов класса HH получаем:
 - список работодателей - HH().get_employers();
 - список вакансий - HH().load_vacancies().

## Модуль utils.py

В модуле реализован основной функционал по работе с БДЖ
 - функция ```db_create``` создает БД и требуемые таблицы;
 - функция ```db_save_data``` заполняет созданные таблици информацией.






