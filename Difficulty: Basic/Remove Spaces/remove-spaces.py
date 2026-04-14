class Solution:
    def removeSpaces(self, s):
        return "".join([i for i in s if i != " "])