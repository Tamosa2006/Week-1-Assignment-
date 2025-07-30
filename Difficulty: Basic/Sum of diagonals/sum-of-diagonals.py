from typing import List

class Solution:
    def sumDiagonal(self, N: int, M: List[List[int]]) -> int:
        diagonal_sum = 0
        for i in range(N):
            diagonal_sum += M[i][i]
        return diagonal_sum
