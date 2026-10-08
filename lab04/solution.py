def winner(names, scores):
    (best_score, best_name) = (-10000000.0, '')
    if (len(names) > 0) and (len(scores) > 0):
        for i in range(len(scores)):
            if scores[i] > best_score:
                best_score = scores[i]
                best_name = names[i]

    return best_name

def average(scores):
    if len(scores) > 0:
        return round(sum(scores) / len(scores), 2)
    else:
        return 0

def ranking(names, scores):
    if (len(names) > 0) and (len(scores) > 0):
        arg_sort = sorted(range(len(scores)), key=lambda i: scores[i])
        return list(names[i] for i in arg_sort)[::-1]
    else:
        return []

def above_average(names, scores):
    if (len(names) > 0) and (len(scores) > 0):
        work_score = average(scores)
        names_list = []

        for i in range(len(scores)):
            if scores[i] > work_score:
                names_list.append(names[i])

        return names_list
    else:
        return []
