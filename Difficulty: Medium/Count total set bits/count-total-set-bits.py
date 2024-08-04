#User function Template for python3

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        n += 1
        x = 2
        cnt = 0
        while x//2 < n:
            quotient = n//x
            
            cnt += quotient * x // 2
            
            remainder = n%x
            if remainder > x//2:
                cnt += remainder - x//2
            
            x = x*2
        
        return cnt

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends