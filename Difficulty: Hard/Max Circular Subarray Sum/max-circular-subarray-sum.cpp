//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends

class Solution {
  public:
    // arr: input array
    // Function to find maximum circular subarray sum.
    int circularSubarraySum(vector<int> &arr) {
        int totalSum = 0;
        int maxSum = INT_MIN, currentMax = 0;
        int minSum = INT_MAX, currentMin = 0;

        for (int num : arr) {
            // Calculate total sum of the array
            totalSum += num;

            // Calculate max subarray sum (Kadane's Algorithm)
            currentMax = max(num, currentMax + num);
            maxSum = max(maxSum, currentMax);

            // Calculate min subarray sum (Kadane's Algorithm for negatives)
            currentMin = min(num, currentMin + num);
            minSum = min(minSum, currentMin);
        }

        // Handle the case where all elements are negative
        if (totalSum == minSum) return maxSum;

        // Return the maximum of non-circular and circular subarray sums
        return max(maxSum, totalSum - minSum);
    }
};




//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;

        // Read first array
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        int res = ob.circularSubarraySum(arr);

        cout << res << endl;
    }
    return 0;
}

// } Driver Code Ends