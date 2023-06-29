def transposeMatrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed.append([])
        for j in range(len(matrix)):
            transposed[i].append(matrix[j][i])
    return transposed 