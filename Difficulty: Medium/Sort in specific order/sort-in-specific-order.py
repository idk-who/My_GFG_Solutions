class Solution:
    def sortIt(self, arr):
        arr.sort(key=lambda x : (1- x%2, -x if x%2 else x))
        return arr