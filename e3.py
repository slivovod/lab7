print("matrix multiplication | matrix size = 3x3", end="")
print("\n--------------------", end="")
print("\nchoose way: \n 1.use pre-written matrices \n 2.define your own matrices", end= "")
print("\nenter 1 or 2, according to your choice: ")
way_selector = 1
way_selector = int(input())

n = 3
matrix_a = []
matrix_b = []
matrix_c = []
if(way_selector == 1):
    matrix_a = [[2, 11, 3],
                [5, 6, 18],
                [7, 2, 5]]
    matrix_b = [[4, 5, 7],
                [12, 3, 8],
                [6, 4, 22]]
else:
    print("\nenter the values of the elements of matrix A")
    for i in range(n):
        temporary_list_of_vars_a = []
        for j in range(n):
            temporary_list_of_vars_a.append(int(input()))
        matrix_a.append(temporary_list_of_vars_a)

    print("\nenter the values of the elements of matrix B")
    for i in range(n):
        temporary_list_of_vars_b = []
        for j in range(n):
            temporary_list_of_vars_b.append(int(input()))
        matrix_b.append(temporary_list_of_vars_b)
#----------
#for i in range(n):
#    temporary_list_of_zeros_c = []
#    for j in range(n):
#        temporary_list_of_zeros_c.append(0)
#    matrix_c.append(temporary_list_of_zeros_c)
#----------
for i in range(n):
    temporary_list_of_vars_c = []
    for j in range(n):
        c_value = 0
        for k in range(n):
            c_value += matrix_a[i][k] * matrix_b[k][j]
        temporary_list_of_vars_c.append(c_value)
    matrix_c.append(temporary_list_of_vars_c)

for i in matrix_c:
    print(i)