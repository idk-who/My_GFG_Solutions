#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        rows = [[False]*10 for i in range(10)]
        cols = [[False]*10 for i in range(10)]
        blocks = [
            [
                [False]*10 for i in range(3)
            ] for j in range(3)
        ]
        
        for i in range(9):
            for j in range(9):
                ele = mat[i][j]
                rows[i][ele] = True
                cols[j][ele] = True
                blocks[i//3][j//3][ele] = True
        
        
        def rec(mat, i, j):
            if i == 9:
                return True
            if mat[i][j] == 0:
                for ele in range(1, 10):
                    if rows[i][ele] == False and cols[j][ele] == False and blocks[i//3][j//3][ele] == False:
                        rows[i][ele] = True
                        cols[j][ele] = True
                        blocks[i//3][j//3][ele] = True
                        mat[i][j] = ele
                        if rec(mat, i, j):
                            return True
                        mat[i][j] = 0
                        rows[i][ele] = False
                        cols[j][ele] = False
                        blocks[i//3][j//3][ele] = False
            else:
                if j == 8:
                    return rec(mat, i+1, 0)
                else:
                    return rec(mat, i, j+1)
        rec(mat, 0, 0)
        return mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends