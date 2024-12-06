#User function Template for python3
class Solution:
    def hIndex(self, citations):
    #code here
        res=0
        citations.sort()
        citations.reverse()
        for k in range(len(citations)):
            if citations[k]>=k+1:
                res=k+1
            else:
                break
        return res


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends