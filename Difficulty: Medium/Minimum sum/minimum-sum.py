#User function Template for python3

class Solution:
    def minSum(self, arr):
        arr.sort()
        p1 = len(arr) - 1
        ans = []
        carry = 0
        
        while p1-1 >= 0:
            temp = arr[p1]+arr[p1-1] + carry 
            digit = temp % 10 
            carry = temp // 10
            ans.append(digit)
            p1 -= 2
            # print(ans)
        
        if p1 == 0:
            temp = arr[p1] + carry 
            digit = temp % 10 
            carry = temp // 10
            ans.append(digit)
        
        if carry > 0:
            ans.append(carry)
            
        while ans[-1] == 0:
            ans.pop()
        
        
        return "".join(map(str, reversed(ans)))
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends