import pandas as pd
import time
from datetime import datetime
import os  # Добавленный импорт модуля os

# Функция для подсчета баллов с учетом поддоменов и записи конкурентов
def calculate_scores_and_competitors(row, competitors, columns_dict):
    score = 0
    competitors_matched = []
    for competitor in competitors:
        if competitor in row['url']:
            score += 1
            competitors_matched.append(row['url'])
    columns_dict['Баллы'].append(score)
    for competitor in competitors:
        matched_urls = [url for url in competitors_matched if competitor in url]
        columns_dict[competitor].append(', '.join(matched_urls) if matched_urls else '')
    return score

# Запрос списка доменов конкурентов
competitors_input = input("Введите список конкурентов через запятую (пример: ozon.ru,ya.ru): ")
competitors = competitors_input.split(',')

# Путь к файлу import.xlsx
input_file = 'import.xlsx'

# Проверка на существование файла
if not os.path.exists(input_file):
    print(f"Файл {input_file} не найден. Пожалуйста, убедитесь, что файл находится в нужной директории.")
else:
    # Загрузка данных из import.xlsx
    df = pd.read_excel(input_file)

    # Инициализация словаря для колонок
    columns_dict = {'Баллы': []}
    for competitor in competitors:
        columns_dict[competitor] = []

    # Сводка
    start_time = time.time()

    # Применение функции calculate_scores_and_competitors для каждой строки
    df.apply(lambda row: calculate_scores_and_competitors(row, competitors, columns_dict), axis=1)

    # Добавление новых колонок к DataFrame
    for column_name, values in columns_dict.items():
        df[column_name] = values

    # Группировка по фразам и подсчет суммы баллов
    result_df = df.groupby('Фраза')[['Баллы'] + competitors].sum().reset_index()

    # Генерация названия файла с учетом более читаемой даты
    date_str = datetime.now().strftime("%d-%m-%Y")
    output_file = f'scores-{date_str}.xlsx'

    # Запись результатов в файл
    result_df.to_excel(output_file, index=False)

    # Сводка
    end_time = time.time()
    execution_time = end_time - start_time
    processed_queries = len(result_df)

    print(f"Результаты сохранены в файл {output_file}")
    print(f"Время выполнения: {execution_time:.2f} секунд")
    print(f"Количество обработанных поисковых запросов: {processed_queries}")
    print(f"Использованных конкурентов: {len(competitors)}")

    # Ожидание нажатия Enter
    input("Нажмите Enter для завершения...")
