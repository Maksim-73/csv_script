from collections import defaultdict
from typing import List, Dict, Any, Tuple, Callable

ReportResult = Tuple[List[str], List[List[Any]]]

def average_gdp_report(data: List[Dict[str, str]]) -> ReportResult:
    """Среднее ВВП по странам"""
    country_gdps: Dict[str, List[float]] = defaultdict(list)

    for row in data:
        country = row.get("country")
        gdp_str = row.get("gdp")
        if not country or not gdp_str:
            continue
        try:
            gdp = float(gdp_str)
            country_gdps[country].append(gdp)
        except ValueError:
            continue

    averages = []
    for country, values in country_gdps.items():
        if values:
            avg = sum(values) / len(values)
            averages.append((country, round(avg, 2)))

    averages.sort(key=lambda x: x[1], reverse=True)

    headers = ["Country", "Average GDP"]
    rows = [[country, avg] for country, avg in averages]

    return headers, rows

# Регистрация возможных отчетов
REPORT_REGISTRY: Dict[str, Callable[[List[Dict[str, str]]], ReportResult]] = {
    "average-gdp": average_gdp_report,

}