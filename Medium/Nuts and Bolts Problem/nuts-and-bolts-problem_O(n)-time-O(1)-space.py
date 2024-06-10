#User function Template for python3
class Solution:

	def matchPairs(self, n, nuts, bolts):
		# code here
		map = {
	        '!':0,
            '#':0,
            '$':0,
            '%':0,
            '&':0,
            '*':0,
            '?':0,
            '@':0,
            '^':0 
        }
		 
        for i in nuts:
            map[i]+=1
		 
        ptr = 0
        for c in '!#$%&*?@^':
            while map[c] != 0:
                nuts[ptr] = c
                bolts[ptr] = c
                ptr += 1
                map[c] -= 1

		 
		 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
