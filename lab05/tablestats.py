def read_rows(lines):
    rows = []
    header = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = [p.strip() for p in line.split(',')]

        if header is None:
            header = parts
            continue

        if len(parts) != len(header):
            continue

        row_dict = dict(zip(header, parts))
        rows.append(row_dict)

    return rows

def count_types(rows):
    counts = {}
    for row in rows:
        t = row.get("тип")
        if t is not None:
            counts[t] = counts.get(t, 0) + 1
    return counts
