//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{

  public:
	int minDifference(int arr[], int n)  { 
	    long long sum=accumulate(arr, arr+n, (long long)0);
	    long long target = sum/2;
	    
	    
	    vector<vector<bool>> dp(n, vector<bool>(target+1));
	    
	    dp[0][0] = true;
	    if(arr[0]<=target)
	        dp[0][arr[0]] = true;
	        
	    for(int i=1; i<n; i++) {
	        for(long long j=0; j<=target; j++) {
	            
	            bool res=false;
	            res = res|dp[i-1][j];
	            
	            if(j-arr[i]>=0)
	                res = res|dp[i-1][j-arr[i]];
	                
	            dp[i][j] = res;
	        }
	    }
	    
	    for(int j=target; j>=0; j--) {
	        if(dp[n-1][j]) {
	           // cout<<sum<<", "<<j<<endl;
	            return (sum-j)-j;
	        }
	    }
	    
	    return -1;
	} 
};


//{ Driver Code Starts.
int main() 
{
   
   
   	int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        int a[n];
        for(int i = 0; i < n; i++)
        	cin >> a[i];

       

	    Solution ob;
	    cout << ob.minDifference(a, n) << "\n";
	     
    }
    return 0;
}
// } Driver Code Ends