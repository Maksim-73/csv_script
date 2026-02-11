import pytest
from src.data_loader import load_data
from pathlib import Path


def test_load_data_one_file_happy_path(temp_csv_file):
    content = """country,year,gdp
USA,2023,25000
China,2023,18000
"""
    path = temp_csv_file(content)
    data = load_data([str(path)])
    assert len(data) == 2
    assert data[0]["country"] == "USA"
    assert data[1]["gdp"] == "18000"


def test_load_multiple_files(temp_csv_file):
    f1 = temp_csv_file("""country,gdp
A,100""", "f1.csv")

    f2 = temp_csv_file("""country,gdp
B,200
A,150""", "f2.csv")

    data = load_data([str(f1), str(f2)])
    assert len(data) == 3
    countries = {row["country"] for row in data}
    assert countries == {"A", "B"}


def test_load_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_data(["/non/existent/file.csv"])


def test_load_data_empty_file(temp_csv_file):
    path = temp_csv_file("")
    with pytest.raises(ValueError, match="Нет данных после загрузки файлов"):
        load_data([str(path)])


def test_load_data_only_header_no_rows(temp_csv_file):
    content = "country,year,gdp\n"
    path = temp_csv_file(content)
    with pytest.raises(ValueError, match="Нет данных после загрузки файлов"):
        load_data([str(path)])