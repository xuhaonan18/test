import numpy as np
def rotate(matrix):
    #********* Begin *********#
    s = [[0 for e in range(len(matrix[0]))]for q in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            s[j][len(matrix)-1-i] = matrix[i][j]
    return s
matrix = [[1,1,1],
          [2,2,2],
          [3,3,3]]
print(np.array(rotate(matrix)))      