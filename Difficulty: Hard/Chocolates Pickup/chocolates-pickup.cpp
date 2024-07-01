//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
public:
    int solve(int n, int m, vector<vector<int>>& grid) {
        vector<vector<int>> dp(m, vector<int>(m, 0));
        vector<vector<int>> new_dp(m, vector<int>(m, 0));
        
        for (int i = n - 1; i >= 0; i--) {
            for (int p1 = m - 1; p1 >= 0; p1--) {
                for (int p2 = m - 1; p2 >= 0; p2--) {
                    int ma = dp[p1][p2];
                    
                    for (int d1 = p1 - 1; d1 <= p1 + 1; d1++) {
                        for (int d2 = p2 - 1; d2 <= p2 + 1; d2++) {
                            if (d1 >= 0 && d1 < m && d2 >= 0 && d2 < m) {
                                ma = max(ma, dp[d1][d2]);
                            }
                        }
                    }
                    
                    if (p1 == p2) {
                        ma += grid[i][p1];
                    } else {
                        ma += grid[i][p1] + grid[i][p2];
                    }
                    
                    new_dp[p1][p2] = ma;
                }
            }
            dp = new_dp;
        }
        
        return dp[0][m-1];
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> grid;
        for (int i = 0; i < n; i++) {
            vector<int> temp;
            for (int j = 0; j < m; j++) {
                int x;
                cin >> x;
                temp.push_back(x);
            }
            grid.push_back(temp);
        }

        Solution obj;
        cout << obj.solve(n, m, grid) << "\n";
    }
    return 0;
}
// } Driver Code Ends