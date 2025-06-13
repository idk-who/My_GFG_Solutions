#User function Template for python3

class Solution:
    def kokoEat(self,arr,k):
        # Code here
        
        left, right = 1, max(arr)
        while left < right:
            mid = (left + right) // 2
            hours = sum((pile + mid - 1) // mid for pile in arr)
            if hours <= k:
                right = mid
            else:
                left = mid + 1
        return left