#User function Template for python3

class Solution:
    def search(self,arr,key):
        lo = 0
        hi = len(arr) - 1
        
        while lo <= hi:
            m = (lo+hi)//2
            
            if arr[m] == key:
                return m
            
            if arr[lo] <= arr[m]:
                if arr[lo] <= key < arr[m]:
                    hi = m - 1
                else:
                    lo = m + 1
            else:
                if arr[m] < key <= arr[hi]:
                    lo = m + 1
                else:
                    hi = m - 1
                
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends