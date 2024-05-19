
from typing import List
from bisect import bisect_right

class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        m = float("inf")
        ans = -1
        for i in range(len(arr)):
            if abs(arr[i]-k) <= m:
                m = abs(arr[i]-k)
                ans = arr[i]
                
        return ans
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends