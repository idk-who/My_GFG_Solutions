class Solution:  
    def findMaxSum(self,arr):
        # code here
        one, two = 0, arr[0]
        
        for i in range(1, len(arr)):
            two, one = max(two, arr[i]+one), two
        
        return two

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends