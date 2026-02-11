# Macro Reports

Скрипт для обработки CSV-файла.

В данный момент реализован отчёт **средний ВВП по странам**.

## Быстрый запуск

```bash
# примеры использования
python -m src.main --files data/*.csv --report average-gdp
python -m src.main --files data/2023.csv --report average-gdp

#Добавление нового отчета
В файле reports.py нужно прописать логику в новой функции и добавить запись в словарь REPORT_REGISTRY

#Установка зависимостей
Bashpip install -r requirements.txt

#Структура проекта
src/main.py          — запуск, аргументы, вызов отчёта
src/data_loader.py   — чтение и объединение csv файлов
src/reports.py       — логика отчётов 
tests/               — тесты 
data/                — csv файлы

##Результаты запуска

[Alt text](screenshots/economic1.png)

[Alt text](screenshots/economic2.png)

