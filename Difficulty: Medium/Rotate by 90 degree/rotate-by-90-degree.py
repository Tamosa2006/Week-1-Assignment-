class Solution:
    def rotateMatrix(self, mat):
        n = len(mat)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        # Step 2: Reverse each column
        for col in range(n):
            for row in range(n // 2):
                mat[row][col], mat[n - 1 - row][col] = mat[n - 1 - row][col], mat[row][col]

        return mat
