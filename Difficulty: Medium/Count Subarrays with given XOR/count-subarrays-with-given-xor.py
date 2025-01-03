from collections import defaultdict
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        ans = 0
        d = defaultdict(int)
        d[0] = 1
        su = 0
        for i in arr:
            su ^= i
            if su^k in d:
                ans += d[su^k]
            d[su] += 1
        return ans
        
        

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends