#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        d = {0:1}
        ans = 0
        su = 0
        
        for i in range(len(arr)):
            su += arr[i]
            if su - tar in d:
                ans +=  d[su-tar]
            if su in d:
                d[su] += 1
            else:
                d[su] = 1
        
        return ans
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends