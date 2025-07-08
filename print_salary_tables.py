import os
from dotenv import load_dotenv

from hh_api import calculate_average_salaries
from sj_api import calculate_average_salaries_superjob
from salary_table import print_salary_table


if __name__ == '__main__':
    load_dotenv()
    superjob_key = os.getenv('SUPERJOB_API_KEY')
    
    SJ_DEVELOPMENT_CATALOGUE_ID = 48,
    SJ_PAGE_SIZE = 100

    languages = ['Python', 'Java', 'C++', 'C#', 'JavaScript', 'Ruby', 'Go', '1C']

    hh_stats = calculate_average_salaries(languages)
    print_salary_table(hh_stats, 'HeadHunter Moscow')

    sj_stats = calculate_average_salaries_superjob(
        languages,
        superjob_key,
        SJ_DEVELOPMENT_CATALOGUE_ID,
        SJ_PAGE_SIZE
    )
    print_salary_table(sj_stats, 'SuperJob Moscow')