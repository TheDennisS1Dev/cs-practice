def count_items(values):
    result = {}

    if len(values) != 0:
        for item in values:
            print(result)
            if item in result:
                result[item] += 1
            else:
                result.update({item: 1})

    return result

def unique_sorted(values):
    return sorted(set(values))

def common(first, second):
    result = []

    if (len(first) != 0) or (len(second) != 0):
        for item in first:
            if item in second:
                result.append(item)
        result.sort()

    return result

def only_in_first(first, second):
    result = []

    if (len(first) != 0) or (len(second) != 0):
        for item in first:
            if item not in second:
                result.append(item)

        result.sort()

    return result
