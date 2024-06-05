#User function Template for python3

def max_sum(a,n):
    s = 0
    ts = 0
    
    for i in range(n):
        s += a[i]
        ts += a[i]*i
    
    ans = ts  
    for i in range(1, n):
        ts = ts + s - n*a[n-i]
        ans = max(ans, ts)
        
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends