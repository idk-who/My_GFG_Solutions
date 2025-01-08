#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        n = len(arr)
        arr.sort()
        count = 0 
        for c in range(n-1, 1, -1):
            a= 0 
            b = c-1
            while  a< b :
                if arr[a]+ arr[b] > arr[c]:
                    count += b-a 
                    b-=1
                else : 
                    a+=1
                    
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends