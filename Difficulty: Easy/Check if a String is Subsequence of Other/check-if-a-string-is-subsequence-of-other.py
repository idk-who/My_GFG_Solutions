class Solution:
    def isSubSeq(self, s1, s2):
        p1 = p2 = 0
        
        while p1 < len(s1) and p2 < len(s2):
            if s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        
        return p1 == len(s1)
        