#User function Template for python3
class Solution:
    def findSubString(self, str):
        # code here
        n=len(str)
        s=set(str)
        l=len(s)

        d={}
        i=0
        start=0
        length=n+1

        for j in range(n):
            d[str[j]]=d.get(str[j],0)+1
            if d[str[j]]==1:
                i+=1
            while i==l:
                length=min(length,j-start+1)

                d[str[start]]-=1
                if d[str[start]]==0:
                    i-=1
                start+=1
        return length
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        str = input()
        ob = Solution()
        print(ob.findSubString(str))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends