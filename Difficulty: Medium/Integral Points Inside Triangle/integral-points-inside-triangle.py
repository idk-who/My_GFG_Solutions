#User function Template for python3

from math import gcd


class Solution:
    def InternalCount(self, p, q, r):
        def triangle_area(x1, y1, x2, y2, x3, y3):
            return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        # Function to calculate the number of boundary lattice points using gcd
        def boundary(x1, y1, x2, y2):
            return gcd(abs(x2 - x1), abs(y2 - y1))

        # Extract coordinates from the points
        x1, y1 = p
        x2, y2 = q
        x3, y3 = r

        # Calculate the area of the triangle
        area = triangle_area(x1, y1, x2, y2, x3, y3)

   
        b1 = boundary(x1, y1, x2, y2)
        b2 = boundary(x2, y2, x3, y3)
        b3 = boundary(x3, y3, x1, y1)

        
        boundary_points = b1 + b2 + b3

     
        ans = (area - boundary_points + 2) // 2

        return int(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        p=[0]*2
        q=[0]*2
        r=[0]*2
        p[0],p[1],q[0],q[1],r[0],r[1]=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.InternalCount(p,q,r);
        print(ans)
# } Driver Code Ends