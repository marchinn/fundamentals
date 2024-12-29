def multiplyMatrices (matrixA, matrixB):
    result = []
    rows = len(matrixA)
    cols = len(matrixA[0])

    for i in range(rows):
        stroke = []
        for j in range(cols):
            element = 0
            for k in range(cols):
                element += matrixA[i][k]*matrixB[k][j]
            stroke.append(element)
        result.append(stroke)
    return result

print( multiplyMatrices( [[1, 2],[3, 4]], [[1, 1],[2, 2]] ))
print( multiplyMatrices( [[1, 1, 1],[2, 3, 4],[5, 5, 5]], [[1, 3, 2],[2, 2, 0],[9, 2, 5]] ))