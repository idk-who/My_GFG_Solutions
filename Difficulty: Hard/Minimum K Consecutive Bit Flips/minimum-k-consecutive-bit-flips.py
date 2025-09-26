class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        isFlipped = [0] * n
        flips = 0
        res = 0
        
        for i in range(n):
            # remove the effect of flips that ended k steps ago
            if i >= k:
                flips ^= isFlipped[i - k]
            
            # check effective value at arr[i]
            if (arr[i] ^ flips) == 0:  # needs flipping
                if i + k > n:
                    return -1
                isFlipped[i] = 1
                flips ^= 1
                res += 1
        
        return res