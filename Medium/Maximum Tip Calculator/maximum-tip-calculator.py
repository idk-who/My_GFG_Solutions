
from typing import List
from heapq import heappush, heappop

class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        ah = []
        bh = []
        ans = 0
        for a, b in zip(arr, brr):
            if a > b:
                heappush(ah, a-b)
                if x>0:
                    ans += a
                else:
                    # print("revert a")
                    ans += a - heappop(ah)
                x -= 1
            else:
                heappush(bh, b-a)
                if y>0:
                    ans += b
                else:
                    # print("revert b")
                    ans += b - heappop(bh)
                y -= 1
            # print(ans)
        
        return ans



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends