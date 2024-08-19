#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        
        me = max(arr)
        
        eles = [False]*(me+1)
        
        for i in arr:
            eles[i] = True
        
        ptr = 0
        while k > 1:
            if eles[ptr]:
                k -= 1
            ptr += 1
            
        while not eles[ptr]:
            ptr += 1
        
        return ptr
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends