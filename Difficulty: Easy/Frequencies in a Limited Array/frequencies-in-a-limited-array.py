class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        freq = [0] * n

        # Fix: Iterate through each element in arr
        for num in arr:
            if 1 <= num <= n:
                freq[num - 1] += 1

        # Update arr in-place
        for i in range(n):
            arr[i] = freq[i]

        return arr