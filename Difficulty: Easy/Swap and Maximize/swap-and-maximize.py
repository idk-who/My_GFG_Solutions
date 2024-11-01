#User function Template for python3

class Solution:
    def maxSum(self,arr):
        arr.sort()
        left=0
        right=len(arr)-1
        res=[]
        while left<=right:
            if left==right:
                res.append(arr[left])
            else:
                res.append(arr[left])
                res.append(arr[right])
            left+=1
            right-=1
        sum=0 
        l=len(res)
        if l==2:
            k=abs(res[0]-res[1])
            return k*2
        else:
            for i in range(l-1):
                sum+=abs(res[i]-res[i+1])
                o=res[l-1]-res[0]
                p=o+sum
            return p  

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends