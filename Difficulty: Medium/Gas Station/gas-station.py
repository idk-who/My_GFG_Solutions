class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        
        tank = 0
        le = 0
        
        for i in range(2*n):
            j = i%n
            
            tank += gas[j]
            tank -= cost[j]
            
            if tank >= 0:
                le += 1
            else:
                le = 0
                tank = 0
            
            if le == n:
                return i-n+1
        
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends