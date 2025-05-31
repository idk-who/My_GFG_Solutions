class Solution:
    def kthSmallest(self, matrix, k):
        ans=[]
        for i in matrix:
            ans.extend(i)
        ans.sort()
        return ans[k-1]