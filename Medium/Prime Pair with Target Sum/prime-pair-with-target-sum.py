
from typing import List


class Solution:
    def getPrimes(self, n : int) -> List[int]:
        primes = [True]*(n)
        ptr = 2
        while ptr < len(primes):
            if primes[ptr]:
                for i in range(ptr*ptr, len(primes), ptr):
                    primes[i] = False
            ptr += 1
        
        for i in range(2, len(primes)):
            if primes[i] and primes[n-i]:
                return [i, n-i]
            
        return [-1, -1]
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends