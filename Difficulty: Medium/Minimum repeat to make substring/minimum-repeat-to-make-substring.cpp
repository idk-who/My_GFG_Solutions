//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int minRepeats(string& s1, string& s2) {
        int n1 = s1.length();
        int n2 = s2.length();
        
        int factor = n2 / n1 + ((n2 % n1) > 0);
        
        string new_s1 = "";
        for (int i = 0; i < factor; ++i) {
            new_s1 += s1;
        }
        
        if (new_s1.find(s2) != string::npos) {
            return factor;
        } else {
            new_s1 += s1;
            if (new_s1.find(s2) != string::npos) {
                return factor + 1;
            }
            return -1;
        }
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {
        string A, B;
        getline(cin, A);
        getline(cin, B);

        Solution ob;
        cout << ob.minRepeats(A, B) << endl;
    }
    return 0;
}
// } Driver Code Ends