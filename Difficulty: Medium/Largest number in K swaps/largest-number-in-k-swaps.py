#User function Template for python3

class Solution:
   
   #Function to find the largest number after k swaps.
   def findMaximumNum(self,s,k):
       #code here
       maxi = [s]
       string = [char for char in s]
       idx = 0

       self.findMaxNumUtil(string, k, idx, maxi)
       
       return maxi[0]
   
   def findMaxNumUtil(self, string, k, idx, maxi):
       if k <= 0 or idx >= len(string)-1:
           return
       # Find maximum for idx+1 to n
       max_in_str = string[idx]
       for m in range(idx+1, len(string)):
           if int(string[m]) > int(max_in_str):
               max_in_str = string[m]
       
       if string[idx] != max_in_str:
           k -= 1

       # swap idx with max_in_str and recursively find maximum
       for i in range(idx, len(string)):
           if string[i] == max_in_str:
               string[idx], string[i] = string[i], string[idx]
               
               new_str = "".join(string)
               if int(new_str) > int(maxi[0]):
                   maxi[0] = new_str
               
               # recur for chars idx+1 to n
               self.findMaxNumUtil(string, k, idx+1, maxi)
               
               # backtrack
               string[idx], string[i] = string[i], string[idx]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

        print("~")

# } Driver Code Ends