class Solution:
    def maxProfit(self, arr, k):
        if not arr:
            return 0
        
        hold = -arr[0]   # max profit when holding a stock
        cash = 0         # max profit when not holding
        
        for price in arr[1:]:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - k)
        
        return cash     