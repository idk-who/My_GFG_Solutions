#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        total,unique,isPresent=0,0,[False]*26
        for val in string:
            if val.isalpha():
                total+=1
                i=ord(val)-ord("a")
                if not isPresent[i]:
                    isPresent[i]=True
                    unique+=1
        return 26-unique<=k and total>=26


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends