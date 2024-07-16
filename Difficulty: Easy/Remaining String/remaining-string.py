#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		
		ptr = 0
		while ptr < len(s) and count > 0:
		    if s[ptr] == ch:
		        count -= 1
            ptr += 1
        
        return s[ptr:]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends