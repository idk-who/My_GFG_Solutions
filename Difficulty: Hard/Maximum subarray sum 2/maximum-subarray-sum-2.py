from collections import deque

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        
        # Step 1: prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        
        dq = deque()  # store indices of prefix sums
        max_sum = float('-inf')
        
        for r in range(a, n + 1):
            # Maintain deque for valid l range:
            # remove elements out of window (l < r-b)
            while dq and dq[0] < r - b:
                dq.popleft()
            
            # Add new candidate start index for length >= a
            l = r - a
            # Maintain deque as increasing prefix sum
            while dq and prefix[dq[-1]] >= prefix[l]:
                dq.pop()
            dq.append(l)
            
            # Compute maximum sum using current window
            if dq:
                max_sum = max(max_sum, prefix[r] - prefix[dq[0]])
        
        return max_sum