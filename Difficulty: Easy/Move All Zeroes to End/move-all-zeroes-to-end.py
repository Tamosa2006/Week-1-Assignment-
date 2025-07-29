#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	p= 0
    	for i in range(len(arr)):
    	    if arr[i] !=0:
    	        arr[p], arr[i] = arr[i], arr[p]
    	        p+= 1