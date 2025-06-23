from collections import deque

class Solution:
    def get(self,count):
        n=len(count)
        i=n-1
        while i>=0:
            if count[i]:
                count[i]-=1
                return i
            i-=1
        return 0
        
    def minSum(self, arr):
        count=[0]*10
        for item in arr:
            count[item]+=1
        ans=deque()
        carry=0
        while True:
            total=self.get(count)+self.get(count)+carry
            carry=total//10
            val=total%10
            if carry or val:
                ans.appendleft(str(val))
            else:
                return "".join(ans)