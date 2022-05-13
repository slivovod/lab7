n = 3
matrix = []
for i in range(n):
    temporary_list_of_vars = []
    for j in range(n):
        temporary_list_of_vars.append(int(input()))
    matrix.append(temporary_list_of_vars)

trans_matrix = []
for i in range(n):
    temporary_trans_list_of_vars = []
    for j in range(n):
        temporary_trans_list_of_vars.append(matrix[j][i])
    trans_matrix.append(temporary_trans_list_of_vars)

#print(trans_matrix)

print("matrix")
for i in matrix:
    print(i)

print("\n")

print("transposed matrix")
for i in trans_matrix:
    print(i)