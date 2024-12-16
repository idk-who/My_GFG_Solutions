#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        ans = 0
        p1 = p2 = 0
        for _ in range(k):
            if p1 >= len(a):
                ans = b[p2]
                p2 += 1
            elif p2 >= len(b):
                ans = a[p1]
                p1 += 1
            elif a[p1] < b[p2]:
                ans = a[p1]
                p1 += 1
            else:
                ans = b[p2]
                p2 += 1
        
        return ans
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends