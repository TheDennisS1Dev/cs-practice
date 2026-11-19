import numpy as np

##Задание №1
hours = np.arange(0, 21, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(5, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)
print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)

##Задание №2
print(hours[2])
print(hours[-1])
print(hours[2:5])
print(hours[::2])
print(hours[::-1])

##Задание №3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)
print(temperatures[1, 2])
print(temperatures[0])
print(temperatures[:,-1])
print(temperatures[:2,1:])
print(temperatures[0:2,1:3])
print(temperatures[:,1:3])

##Задание №4
matrix = np.arange(1, 26).reshape(5, 5)
print(matrix[:3])
print(matrix[:3].shape)
print(matrix[:,:2])
print(matrix[:,:2].shape)
print(matrix[1:3,2:4])
print(matrix[1:3,2:4].shape)
print(matrix[-2:,-2:])
print(matrix[-2:,-2:].shape)

##Задание №5
changed_hours = hours.copy()
#Функция copy() создаёт отдельную копию матрицы по значению, независимую по ссылке от своего оригинала
print(hours)
print(changed_hours)
changed_hours[2:4] = 99
changed_hours[1::2] = -1

changed_matrix = matrix.copy()
changed_matrix[1:4,1:4] = 100
print(matrix)
print(changed_matrix)

##Задание №6
numbers = np.arange(0, 12)
table = numbers.reshape(3, 4)
transposed = table.T
print(numbers.shape)
print(table.shape)
print(transposed.shape)
#reshape(5, 3) не сработает в нашем случае, так как нехватит элементов исходной. таблицы при преобразовании. В отличии reshpae(3, 4) где потребуется 12 элементов, которое есть в numbers, в reshape(5, 3) потребуется 15 элементов, а для данной операции нехватает трёх элементов в numbers.
