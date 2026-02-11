# Скрипт для обработки CSV-файла.



В данный момент реализован отчёт **средний ВВП по странам**.

## Быстрый запуск

## Клонирование репозитория:
```bash
git clone https://github.com/Maksim-73/csv_script.git
cd csv_script 
```

## Установка зависимостей
```Bash
pip install -r requirements.txt
```

## примеры использования
```bash
python -m src.main --files data/*.csv --report average-gdp
python -m src.main --files data/2023.csv --report average-gdp
```

## Добавление нового отчета
В файле reports.py нужно прописать логику в новой функции и добавить запись в словарь REPORT_REGISTRY


## Структура проекта
src/main.py          — запуск, аргументы, вызов отчёта  
src/data_loader.py   — чтение и объединение csv файлов  
src/reports.py       — логика отчётов   
tests/               — тесты   
data/                — csv файлы  

## Результаты запуска

[Запуск](screenshots/economic1.png)

[Запуск](screenshots/economic2.png)
