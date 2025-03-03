from collections import deque
class Solution:
    def longestSubarray(self, arr, x):
        maq = deque()
        miq = deque()
        ans = 1
        ids = (0, 0)
        left = 0
        for i in range(len(arr)):
            while maq and arr[maq[-1]] <= arr[i]:
                maq.pop()
            while miq and arr[miq[-1]] >= arr[i]:
                miq.pop()
            maq.append(i)
            miq.append(i)
            
            while miq and maq and arr[maq[0]] - arr[miq[0]] > x:
                if maq[0] == left:
                    maq.popleft()
                if miq[0] == left:
                    miq.popleft()
                left += 1
            
            if i - left + 1 > ans:
                ans = i - left + 1
                ids = (left, i)
        
        return arr[ids[0]:ids[1]+1]
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.longestSubarray(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends