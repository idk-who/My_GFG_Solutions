class Data:
    def __init__(self, k, frq):
        self.k = k
        self.frq = frq
        
    def __lt__(self, other):
        if self.frq < other.frq:
            return True
        elif self.frq > other.frq:
            return False
        elif self.k < other.k:
            return True
            
        return False

class Solution:
	def topKFreq(self, arr, k):
		# Code here
		frq = {}
		for i in arr:
		    frq[i] = frq.get(i, 0) + 1
		    
		arr = [Data(*i) for i in frq.items()]
		arr.sort(reverse=True)
		return [ d.k for d in arr[:k]]