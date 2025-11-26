class Solution:
    def andInRange(self, l, r):
        i = 1 << r.bit_length() - 1
        answer = 0
        while i > 0:
            if (l & i) == (r & i):
                if l & i:
                    answer |= i
            else:
                break
            i >>= 1
        return answer
