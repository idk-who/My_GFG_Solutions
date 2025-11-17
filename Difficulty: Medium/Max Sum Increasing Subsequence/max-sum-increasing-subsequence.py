from functools import cache
class Solution:
	def maxSumIS(self, arr):
		@cache
		def dfs(i,prev):
            return 0 if i==len(arr) else max(dfs(i+1,prev),arr[i]+dfs(i+1,i) if prev==-1 or arr[i]>arr[prev] else 0)
        return dfs(0,-1)
