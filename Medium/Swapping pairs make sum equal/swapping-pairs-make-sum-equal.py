class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        suma = sum(a)
        sumb = sum(b)
        diff = sumb-suma
        
        if diff & 1:
            return -1
            
        diff /= 2
        
        a.sort()
        b.sort()
        
        p1 = 0
        p2 = 0
        # print(a, '\n', b)
        while p1 < n and p2 < m:
            diff2 = b[p2] - a[p1]
            # print(p1, p2, diff, diff2)
            if diff2 == diff:
                return 1
            elif diff2 > diff:
                p1 += 1
            else:
                p2 += 1
        
        return -1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends