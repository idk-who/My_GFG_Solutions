import heapq
class Solution:
    def findSmallestRange(self, arr):
        # code here
        n=len(arr)
        m=len(arr[0])
        l=[]
        mx=float('-inf')
        for i in range(n):
            v=arr[i][0]
            heapq.heappush(l,(v,i,0))
            mx=max(mx,v)
        a,b=float('-inf'),float('inf')
        while True:
            mn,i,j=heapq.heappop(l)
            if mx-mn<b-a:
                a,b=mn,mx
            if j+1<m:
                v=arr[i][j+1]
                heapq.heappush(l,(v,i,j+1))
                mx=max(mx,v)
            else:
                break
        return [a,b]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(k):
        arr.append(list(map(int, input().strip().split())))
    r = Solution().findSmallestRange(arr)
    print(r[0], r[1])
    print("~")

# } Driver Code Ends