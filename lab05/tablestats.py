def read_rows(lines):
    work_lines = list(lines)
    titles = list(map(lambda l: l.strip(), work_lines[0].split(',')))
    result = []

    for line in work_lines[1:]:
        work = line.split(',')

        if len(work) == len(titles):
            result_line = {}

            for i in range(len(work)):
                result_line.update({titles[i]: work[i].strip()})

            result.append(result_line)

    return result

def count_types(rows):
    types = {}

    for line in rows:
        if line['тип'] in types:
            types[line['тип']] += 1
        else:
            types.update({line['тип']: 1})

    return types

def total_minutes(rows, kind):
    sum = 0.0

    for line in rows:
        if line['тип'] == kind:
            sum += float(line['минуты'])

    return sum

def to_csv(counts):
    result = "тип;количество\n"
    types = sorted(counts, key=lambda c: c[0])

    for type in types:
        result += type + f",{counts[type]}\n"

    return result
