#User function Template for python3
    
class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def bs(self,arr,key):
        n=len(arr)
        l,h=0,n-1
        ind=-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]<=key:
                ind=mid
                l=mid+1
            else:
                h=mid-1
        return ind
    
    def countPairs(self,arr,brr):
        ans,one,two,threeFour=0,0,0,0
        for item in brr:
            if item==1:
                one+=1
            elif item==2:
                two+=1
            elif item==3 or item ==4:
                threeFour+=1
        brr.sort()
        for item in arr:
            if item!=1:
                ans+=one
                if item==2:
                    ans-=threeFour
                elif item==3:
                    ans+=two
                ans+=len(brr)-1-self.bs(brr,item)
        return ans
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        # M, N = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countPairs(a, b))
        #code here

# } Driver Code Ends