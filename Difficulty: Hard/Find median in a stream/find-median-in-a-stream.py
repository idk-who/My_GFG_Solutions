
from heapq import heappush, heappop

class Solution:
    def getMedian(self, arr):
        min_h = []
        max_h = []
        ans = []
        
        for i in arr:
            # print(i)
            if len(min_h) == len(max_h):
                heappush(max_h, -i)
            else:
                heappush(min_h, i)
            
            
            if len(min_h) > 0 and min_h[0] < -max_h[0]:
                ele = -heappop(max_h)
                heappush(min_h, ele)
                ele = heappop(min_h)
                heappush(max_h, -ele)
            
            
            if len(min_h) == len(max_h):
                ans.append((min_h[0]-max_h[0])/2)
            else:
                ans.append(-max_h[0])
            # print(min_h, max_h)
            
            
        return ans
        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends