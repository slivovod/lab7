n = 4
matrix = []
for i in range(n):
    temporary_list_of_vars = []
    for j in range(n):
        value = int(input())
        if(value < 0):
            value = 0
        temporary_list_of_vars.append(value)
    matrix.append(temporary_list_of_vars)

for i in matrix:
    print(i)