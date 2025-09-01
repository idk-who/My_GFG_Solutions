from heapq import heappop, heappush, heapify
from collections import defaultdict
class Solution:
    def sumOfModes(self, arr, k):
        # eliminationg edge cases
        if k > len(arr):
            return 0
            
        freq = defaultdict(int)
        heap = []
        for i in range(k):
            freq[arr[i]] += 1
            heappush(heap, [-freq[arr[i]], arr[i]])
        
        su = heap[0][1]
        
        for i in range(k, len(arr)):
            old = arr[i-k]
            new = arr[i]
            freq[old] -= 1
            freq[new] += 1
            heappush(heap, [-freq[new], new])
            while -heap[0][0] != freq[heap[0][1]]:
                heappop(heap)
            su += heap[0][1]
            
        return su
