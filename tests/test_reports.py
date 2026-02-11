import pytest
from src.reports import average_gdp_report


def test_average_gdp_basic_calculation(sample_rows):
    headers, rows = average_gdp_report(sample_rows)

    assert headers == ["Country", "Average GDP"]
    assert len(rows) == 3

    country_to_avg = {r[0]: float(r[1]) for r in rows}

    assert country_to_avg["USA"] == pytest.approx(24500.0, 0.01)
    assert country_to_avg["China"] == pytest.approx(17750.0, 0.01)
    assert country_to_avg["Germany"] == 4100.0

    # проверка сортировки по убыванию
    gdps = [float(r[1]) for r in rows]
    assert gdps == sorted(gdps, reverse=True)


def test_average_gdp_empty_input():
    headers, rows = average_gdp_report([])
    assert headers == ["Country", "Average GDP"]
    assert rows == []


def test_average_gdp_skip_invalid_gdp():
    data = [
        {"country": "A", "gdp": "1000"},
        {"country": "B", "gdp": "invalid"},
        {"country": "B", "gdp": "2000"},
        {"country": "C", "gdp": ""},
        {"country": "D", "gdp": "abc"},
    ]
    _, rows = average_gdp_report(data)

    country_to_avg = {r[0]: float(r[1]) for r in rows}
    assert "A" in country_to_avg
    assert "B" in country_to_avg
    assert "C" not in country_to_avg
    assert "D" not in country_to_avg
    assert country_to_avg["B"] == 2000.0  # только валидное значение


def test_average_gdp_negative_and_zero_values():
    data = [
        {"country": "X", "gdp": "-500"},
        {"country": "X", "gdp": "0"},
        {"country": "Y", "gdp": "3000"},
    ]
    _, rows = average_gdp_report(data)

    country_to_avg = {r[0]: float(r[1]) for r in rows}
    assert country_to_avg["X"] == pytest.approx(-250.0)
    assert country_to_avg["Y"] == 3000.0


def test_average_gdp_rounding():
    data = [
        {"country": "Z", "gdp": "1234.567"},
        {"country": "Z", "gdp": "8765.432"},
    ]
    _, rows = average_gdp_report(data)
    assert rows[0][1] == 5000.0   # (1234.567 + 8765.432) / 2 = 4999.9995 → 5000.00 после round(2)