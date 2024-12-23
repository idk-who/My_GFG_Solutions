
#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
        n, m = len(mat), len(mat[0])
        
    	def bn(i, x):
    	    lo = 0
    	    hi = m-1
    	    
    	    while lo <= hi:
    	        mi = (lo+hi)//2
    	        
    	        if mat[i][mi] == x:
    	            return True
    	        elif mat[i][mi] < x:
    	            lo = mi + 1
    	        else:
    	            hi = mi - 1
    	    return False
        
        for i in range(n):
            if bn(i, x):
                return True
        
        return False
    	



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchRowMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends