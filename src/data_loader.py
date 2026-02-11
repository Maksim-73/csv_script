import csv
from pathlib import Path
from typing import List, Dict


def load_data(file_paths: List[str]) -> List[Dict[str, str]]:
    """Загрузка данных из csv файлов"""
    all_rows: List[Dict[str, str]] = []

    for path_str in file_paths:
        path = Path(path_str)
        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {path}")

        with open(path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            all_rows.extend(list(reader))

    if not all_rows:
        raise ValueError("Нет данных после загрузки файлов")

    return all_rows