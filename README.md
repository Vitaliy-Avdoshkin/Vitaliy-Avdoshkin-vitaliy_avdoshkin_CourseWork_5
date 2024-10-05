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


