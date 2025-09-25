from collections import deque

class Solution:    
    def rotateDeque(self, dq, type, k):
        n = len(dq)
        k %= n   # optimize unnecessary full rotations
        
        if type == 1:   # Right rotation
            dq.rotate(k)
        else:           # Left rotation
            dq.rotate(-k)
        
        return list(dq)  # convert to list for output consistency
