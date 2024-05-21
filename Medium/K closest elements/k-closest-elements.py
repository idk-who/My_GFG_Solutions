#User function Template for python3

from heapq import heappush ,heappop
class Solution:
    def printKClosest(self, arr, n, k, x):

        heap = []
        
        for val in arr[::-1] :
            if val==x:
                continue
            dist = abs(val - x)
            
            if len(heap) < k:
                heappush(heap, (-1 * dist, val))
            else:
                if -1 * heap[0][0] > dist:
                    heappop(heap)
                    heappush(heap, (-1 * dist, val))
                    
        result = []
        while heap:
            _, val = heappop(heap)
            result.append(val)
        return result[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k, x = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends