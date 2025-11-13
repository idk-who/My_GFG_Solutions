from functools import cache

class Solution:
    def isInterleave(self, s1, s2, s3):
        @cache
        def rec(p1, p2, p3):
            if p3 == len(s3):
                return True
            if p1 < len(s1) and p2 < len(s2) and s1[p1] == s2[p2] == s3[p3]:
                return (
                    rec(p1+1, p2, p3+1) or
                    rec(p1, p2+1, p3+1)
                    )
            elif p1 < len(s1) and s1[p1] == s3[p3]:
                return rec(p1+1, p2, p3+1)
            elif p2 < len(s2) and s2[p2] == s3[p3]:
                return rec(p1, p2+1, p3+1)
            else:
                return False
        
        return rec(0, 0, 0)