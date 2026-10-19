from tablestats import read_rows, count_types, total_minutes, to_csv


def main():
    # 1. Читаем имя файла из первой строки ввода
    file_name = input().strip()

    # 2. Открываем файл и читаем данные
    with open(file_name, "r", encoding="utf-8") as f:
        rows = read_rows(f)

    # 3. Считаем статистику
    counts = count_types(rows)

    # 4. Печатаем три числа (как в примере на сайте)
    print(len(rows))
    print(len(counts))
    print(total_minutes(rows, "ошибка"))

    # 5. Записываем сводку в summary.csv
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))


if __name__ == "__main__":
    main()