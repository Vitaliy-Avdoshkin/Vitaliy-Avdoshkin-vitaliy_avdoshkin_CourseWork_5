from src.db_class import DBManager
from src.db_connect import connect_params
from src.get_vacancy import HH
from src.utils import db_create, db_save_data

params = connect_params()


def main():
    """Функция для работы программы"""

    # Подключаемся к hh.ru через API и получаем информацию по вакансиям и работодателям
    employers_data = HH().get_employers()
    vacancies_data = HH().load_vacancies()

    # Создаем базу данных и таблицы
    db_create("cw_5", params)

    # Заполняем таблицы требуемой информацией
    db_save_data(employers_data, vacancies_data, "cw_5", params)

    # Запускаем класс DBManager (подробное описание класса указано в README)
    db_manager = DBManager(params)

    # Взаимодействуем с пользователем

    print(
        """
        Добрый день!
        Информация по вакансиям и работодателям получена
        Укажите, пожалуйста, цифру для получения требуемой информации
        0 - Выход из программы
        1 - Показать список всех компаний с количеством вакансий для каждой компании.
        2 - Показать список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        3 - Показать список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        4 - Поиск вакансий по заданному слову, например python.
    """
    )

    while True:
        user_input = input()
        if user_input == "1":
            vacancies_count = db_manager.get_companies_and_vacancies_count()
            print("Список всех компаний с количеством вакансий для каждой компании:")
            for i in vacancies_count:
                print(i)
            print("Укажите, пожалуйста, цифру для получения требуемой информации")
        elif user_input == "2":
            all_vacancies = db_manager.get_all_vacancies()
            print(
                "Список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию:"
            )
            for i in all_vacancies:
                print(i)
            print("Укажите, пожалуйста, цифру для получения требуемой информации")
        elif user_input == "3":
            vacancies_with_higher_salary = db_manager.get_vacancies_with_higher_salary()
            print(
                "список всех вакансий, у которых зарплата выше средней по всем вакансиям:"
            )
            for i in vacancies_with_higher_salary:
                print(i)
            print("Укажите, пожалуйста, цифру для получения требуемой информации")
        elif user_input == "4":
            user_word = input("Введите ключевое слово:\n").lower()
            vacancies_with_keyword = db_manager.get_vacancies_with_keyword(user_word)
            print("Список всех вакансий, в названии которых содержится ключевое слово:")
            for i in vacancies_with_keyword:
                print(i)
            print("Укажите, пожалуйста, цифру для получения требуемой информации")
        elif user_input == "0":
            print("Выход")
            break


if __name__ == "__main__":
    main()
