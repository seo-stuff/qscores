# Query Scores - чистка семантического ядра на основе конкурентов в топе
Query Scores (ft. Arsenkin.ru)

Задача скрипта на основе данных поисковой выдачи Яндекс/Google рассчитывать баллы для поисковых запросов.  
Рассчета баллов осуществляется на основе указанных конкурентов.  
Чем больше баллов из топа по выдаче набирает запрос, тем больше вероятность что он является целевым.  
Ключевая задача - правильно определить конкурентов и указать их при работе.
  
Через командную строку в Windows (CMD) установить библиотеки - pip install pandas openpyxl

Алгоритм работы:  
1. Собрать данные выдачи в сервисе - https://arsenkin.ru/tools/check-top/
2. Выбрать из топа по видимости доменов ваших конкурентов (в сервисе Arsenkin)
3. Скачать XLSX файл и переименовать в import.xlsx
4. Положить рядом со скриптом scores.py 
5. Запустить скрипт и указать конкурентов из пункта 2
