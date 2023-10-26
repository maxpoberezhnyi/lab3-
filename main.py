import random

def get_matrix_size():
    while True:
        try:
            size = int(input("Введіть розмірність матриці:"))
            if size > 0:
                return size
            else:
                print("Розмірність повинна бути більшою за 0")
        except ValueError:
            print("Потрібне ціле число")

size = get_matrix_size()

matrix = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):
    for j in range(size):
        matrix[i][j] = random.randint(1, 99)

for row in matrix:
    for num in row:
        print(f'-{num}-', end=' ')
    print()

def get_user_input():
    while True:
        try:
            user_input = int(input("Введіть число:"))
            return user_input
        except ValueError:
            print("Потрібне ціло число")

user_input = get_user_input()

for i in range(size):
    for j in range(size):
        if matrix[i][j] > user_input:
            matrix[i][j] = f'*{matrix[i][j]}*'
        else:
            matrix[i][j] = f'-{matrix[i][j]}-'

print("Новий масив:")
for row in matrix:
    for num in row:
        print(num, end=' ')
    print()