class Solution:
    def countConsec(self, n: int) -> int:
        one,zero=1,1
        for i in range(2,n+1):
            one,zero=zero,zero+one
        return 2**n-one-zero