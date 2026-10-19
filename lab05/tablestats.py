def read_rows(lines):
    """
        Разбирает CSV с заголовком в список словарей.
        Пустые и короткие строки пропускаются.
        """
    rows = []
    header = None

    for line in lines:
        line = line.strip()
        if not line:
            continue  # Пропускаем пустые строки

        parts = [p.strip() for p in line.split(',')]
        # Первая непустая строка — заголовок
        if header is None:
            header = parts
            continue
        # Пропускаем строки, где число полей не совпадает с заголовком
        if len(parts) != len(header):
            continue
        # Создаем словарь и добавляем в список
        row_dict = dict(zip(header, parts))
        rows.append(row_dict)

    return rows

def count_types(rows):
    """
        Считает, сколько записей каждого типа.
        """
    counts = {}
    for row in rows:
        t = row.get("тип")
        if t is not None:
            counts[t] = counts.get(t, 0) + 1
    return counts


def total_minutes(rows, kind):
    """
    Суммарные минуты записей одного типа, округленные до десятых.
    """
    total = 0.0
    for row in rows:
        if row.get("тип") == kind:
            # Заменяем запятую на точку для float()
            minutes_str = row.get("минуты", "").replace(',', '.')
            try:
                total += float(minutes_str)
            except ValueError:
                continue  # Пропускаем нечисловые значения

    return round(total, 1)


