temp_list, error_count, temp_trashhold, count_trashhold = [], 0, 0, 0
max_temp, sum_temp, count_temp = -10000000000, 0, 0

temp_trashhold = float(input('Введите пороговую температуру: '))
n = int(input("Введите количество записей: "))

for i in range(n):
    prompt_temp = input()

    if prompt_temp == "error":
        error_count += 1
    else:
        temp = float(prompt_temp)
        max_temp = max(max_temp, temp)

        if temp > temp_trashhold:
            count_trashhold += 1

        sum_temp += temp
        count_temp += 1

print(f'Количество записей: {n}')
print(f'Количество ошибок: {error_count}')
print(f'Количество привышений: {count_trashhold}')
print(f'Максимальная темпратура: {max_temp:.1f}')
print(f'Средняя температура: {(sum_temp / count_temp):.1f}')
input()
