elements_count = int(input("Введите количество элементов массива: "))
arr = []
for i in range(0, elements_count):
    arr.append(input())
for i in arr[::-1]:
    print(i, end=" ")