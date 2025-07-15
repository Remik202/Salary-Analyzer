from terminaltables import AsciiTable


def print_salary_table(statistics, vacancies_data, title):
    table_data = [
        ['Язык программирования', 'Найдено вакансий', 'Обработано вакансий', 'Средняя зарплата']
    ]

    for language, vacancies_data in statistics.items():
        row = [
            language,
            vacancies_data['vacancies_found'],
            vacancies_data['vacancies_processed'],
            vacancies_data['average_salary']
        ]
        table_data.append(row)

    table = AsciiTable(table_data, title)
    print(table.table)