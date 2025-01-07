#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        n = len(arr)
        
        lo = 0
        hi = n-1
        cnt = 0
        while lo < hi:
            su = arr[lo] + arr[hi]
            
            if su < target:
                lo += 1
            elif su > target:
                hi -= 1
            else:
                if arr[lo] == arr[hi]:
                    cnt += ((hi-lo)*(hi-lo+1))//2
                    return cnt
                else:
                    nle = 1
                    while arr[lo] == arr[lo+1]:
                        lo += 1
                        nle += 1
                    
                    nri = 1
                    while arr[hi] == arr[hi-1]:
                        hi -= 1
                        nri += 1
                    
                    cnt += nle*nri
                lo += 1
                hi -= 1
        
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends