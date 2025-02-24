#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def calculateSpan(self, arr):
        st = []
        
        ans = []
        
        for i in range(len(arr)):
            if not st:
                ans.append(1)
                st.append((arr[i], 1))
            elif arr[i] < st[-1][0]:
                ans.append(1)
                st.append((arr[i], 1))
            else:
                span = 1
                while st and arr[i] >= st[-1][0]:
                    span += st[-1][1]
                    st.pop()
                ans.append(span)
                st.append((arr[i], span))
        
        return ans

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends