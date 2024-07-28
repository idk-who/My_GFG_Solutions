#User function Template for python3
class Solution:
	def removeDups(self, str):
		visited = [False]*26
        ans = []
        
        for i in str:
            if not visited[ord(i)-ord('a')]:
                visited[ord(i)-ord('a')] = True
                ans.append(i)
        
        return "".join(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends