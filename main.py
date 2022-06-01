import random

from faker import Faker

import file_operations


def main():
    fake = Faker('ru_RU')
    low_level = 3
    high_level = 18
    skills = [
        'Стремительный прыжок',
        'Электрический выстрел',
        'Ледяной удар',
        'Стремительный удар',
        'Кислотный взгляд',
        'Тайный побег',
        'Ледяной выстрел',
        'Огненный заряд',
    ]

    letters_mapping = {
        'а': 'а͠',
        'б': 'б̋',
        'в': 'в͒͠',
        'г': 'г͒͠',
        'д': 'д̋',
        'е': 'е͠',
        'ё': 'ё͒͠',
        'ж': 'ж͒',
        'з': 'з̋̋͠',
        'и': 'и',
        'й': 'й͒͠',
        'к': 'к̋̋',
        'л': 'л̋͠',
        'м': 'м͒͠',
        'н': 'н͒',
        'о': 'о̋',
        'п': 'п̋͠',
        'р': 'р̋͠',
        'с': 'с͒',
        'т': 'т͒',
        'у': 'у͒͠',
        'ф': 'ф̋̋͠',
        'х': 'х͒͠',
        'ц': 'ц̋',
        'ч': 'ч̋͠',
        'ш': 'ш͒͠',
        'щ': 'щ̋',
        'ъ': 'ъ̋͠',
        'ы': 'ы̋͠',
        'ь': 'ь̋',
        'э': 'э͒͠͠',
        'ю': 'ю̋͠',
        'я': 'я̋',
        'А': 'А͠',
        'Б': 'Б̋',
        'В': 'В͒͠',
        'Г': 'Г͒͠',
        'Д': 'Д̋',
        'Е': 'Е',
        'Ё': 'Ё͒͠',
        'Ж': 'Ж͒',
        'З': 'З̋̋͠',
        'И': 'И',
        'Й': 'Й͒͠',
        'К': 'К̋̋',
        'Л': 'Л̋͠',
        'М': 'М͒͠',
        'Н': 'Н͒',
        'О': 'О̋',
        'П': 'П̋͠',
        'Р': 'Р̋͠',
        'С': 'С͒',
        'Т': 'Т͒',
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠',
        'Х': 'Х͒͠',
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠',
        'Ш': 'Ш͒͠',
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠',
        'Ы': 'Ы̋͠',
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠',
        'Ю': 'Ю̋͠',
        'Я': 'Я̋',
        ' ': ' ',
    }
    files_total = 10
    file_numbers = list(range(1, files_total + 1))
    for file_number in file_numbers:
        chosen_skills = random.sample(skills, 3)
        runic_skills = []
        for chosen_skill in chosen_skills:
            runic_skill = ""
            for i in chosen_skill:
                runic_skill = runic_skill + letters_mapping[i]

            runic_skills.append(runic_skill)

        context = {
            'first_name': fake.first_name_male(),
            'last_name': fake.last_name_male(),
            'job': fake.job(),
            'town': fake.city(),
            'strength': random.randint(low_level, high_level),
            'agility': random.randint(low_level, high_level),
            'endurance': random.randint(low_level, high_level),
            'intelligence': random.randint(low_level, high_level),
            'luck': random.randint(low_level, high_level),
            'skill_1': runic_skills[0],
            'skill_2': runic_skills[1],
            'skill_3': runic_skills[2],
        }
        file_name = 'forms/form_{}.svg'.format(file_number)
        file_operations.render_template('charsheet.svg', file_name, context)


if __name__ == '__main__':
    main()
