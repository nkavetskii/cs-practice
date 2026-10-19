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