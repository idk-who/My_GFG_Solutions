#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends

import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            arr.append((distance, point))
            
        arr.sort(key=lambda x: x[0])
    
        closestPoints = [arr[i][1] for i in range(k)]
        return closestPoints
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends