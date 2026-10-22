def count_items(values):
    result = {}

    if len(values) != 0:
        for item in values:
            if item in result:
                result[item] += 1
            else:
                result.update({item: 1})

    return result

def unique_sorted(values):
    return sorted(set(values))

def common(first, second):
    return sorted(list(set(first) & set(second)))

def only_in_first(first, second):
    return sorted(list(set(first) - set(second)))
