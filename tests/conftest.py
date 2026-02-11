import pytest
from pathlib import Path
from typing import List, Dict


@pytest.fixture
def sample_rows() -> List[Dict[str, str]]:
    return [
        {"country": "USA", "year": "2023", "gdp": "25000", "gdp_growth": "2.1"},
        {"country": "USA", "year": "2022", "gdp": "24000", "gdp_growth": "1.8"},
        {"country": "China", "year": "2023", "gdp": "18000", "gdp_growth": "5.2"},
        {"country": "China", "year": "2022", "gdp": "17500", "gdp_growth": "3.0"},
        {"country": "Germany", "year": "2023", "gdp": "4100", "gdp_growth": "-0.3"},
    ]


@pytest.fixture
def temp_csv_file(tmp_path: Path):
    def _create(content: str, filename: str = "test.csv") -> Path:
        p = tmp_path / filename
        p.write_text(content.strip(), encoding="utf-8")
        return p

    return _create