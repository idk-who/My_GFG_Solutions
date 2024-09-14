#User function Template for python3

class Solution:
    def rearrange(self,arr):
        n = len(arr)
        ans = [0]*n
        
        pos = 0
        neg = 0
        
        ptr = 0
        
        while ptr < n:
            while pos < n and arr[pos] < 0:
                pos += 1
            while neg < n and arr[neg] >= 0:
                neg += 1
            if pos == n or (ptr & 1 and neg < n):
                # print(ptr, arr[neg])
                ans[ptr] = arr[neg]
                neg += 1
            else:
                # print(ptr, arr[pos])
                ans[ptr] = arr[pos]
                pos += 1
            ptr += 1
        
        arr[:] = ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends