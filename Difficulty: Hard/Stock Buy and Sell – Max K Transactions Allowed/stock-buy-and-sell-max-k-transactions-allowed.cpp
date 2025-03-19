//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
public:
    int maxProfit(std::vector<int>& prices, int k) {
        int n = prices.size();
        std::vector<std::vector<int>> dp(n, std::vector<int>(2 * k + 1, -1));
        
        std::function<int(int, int)> rec = [&](int ptr, int transactions) -> int {
            if (ptr == n) return 0;
            if (transactions == 0) return 0;
            
            if (dp[ptr][transactions] != -1) return dp[ptr][transactions];
            
            int money = 0;
            
            if (!(transactions & 1)) {
                money = std::max(
                    -prices[ptr] + rec(ptr + 1, transactions - 1),
                    rec(ptr + 1, transactions)
                );
            } else {
                money = std::max(
                    prices[ptr] + rec(ptr + 1, transactions - 1),
                    rec(ptr + 1, transactions)
                );
            }
            
            return dp[ptr][transactions] = money;
        };
        
        return rec(0, 2 * k);
    }
};



//{ Driver Code Starts.

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        string input;
        getline(cin, input);
        istringstream iss(input);
        vector<int> arr;
        int num;

        // Read integers from the input string
        while (iss >> num) {
            arr.push_back(num);
        }
        int k;
        cin >> k;
        cin.ignore();
        Solution ob;
        cout << ob.maxProfit(arr, k) << endl;
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends