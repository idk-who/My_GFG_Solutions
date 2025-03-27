from collections import defaultdict

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        timeline = defaultdict(int)
        
        for i in arr:
            timeline[i] += 1
        for j in dep:
            timeline[j+1] -= 1
        
        plats = 0
        max_plats = 0
        
        for k, v in sorted(timeline.items()):
            plats += v
            max_plats = max(
                max_plats,
                plats
            )
        
        return max_plats


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(arrival, departure))
        print("~")

# } Driver Code Ends