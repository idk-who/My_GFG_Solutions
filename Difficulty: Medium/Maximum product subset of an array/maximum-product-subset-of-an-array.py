#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        nn = 0
        np = 0
        mn = float("-inf")
        tp = 1
        has_zero = False
        for i in arr:
            if i < 0:
                nn += 1
                mn = max(i, mn)
            elif i > 0:
                np += 1
            if i != 0:
                tp *= i
            else:
                has_zero = True
        if np == nn == 0: return 0
        if tp > 0: return tp % (10**9+7)
        if tp < 0:
            if np+nn > 1:
                return (tp//mn) % (10**9+7)
            else:
                return 0 if has_zero else tp
    


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends