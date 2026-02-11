import argparse
import sys

from tabulate import tabulate

from .data_loader import load_data
from .reports import REPORT_REGISTRY


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Генератор макроэкономических отчётов"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Пути к csv файлам",
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=list(REPORT_REGISTRY.keys()),
        help="Название отчёта",
    )

    args = parser.parse_args()

    try:
        data = load_data(args.files)
        report_func = REPORT_REGISTRY[args.report]
        headers, rows = report_func(data)

        print(tabulate(rows, headers=headers, tablefmt="grid"))

    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()