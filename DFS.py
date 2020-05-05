#%%
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def dfs(self,grid,r,c):
        grid[r][c] = 0
        rows = len(grid)
        cols = len(grid[0])
        for x,y in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)]:
            if 0<=x<rows and 0<=y<cols and grid[x][y] == '1':
                self.dfs(grid,x,y)


    def numIslands(self, grid) -> int:

        nums = 0
        rows = len(grid)
        if rows == 0:
            return nums
        cols = len(grid[0])



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    nums +=1
                    self.dfs(grid,i,j)

        return nums

#%%
class Solution:
    def dfs(self,grid,r,c):
        grid[r][c] = '1'
        rows = len(grid)
        cols = len(grid[0])
        for x,y in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)]:
            if 0<=x<rows and 0<=y<cols and grid[x][y] == 'O':
                self.dfs(grid,x,y)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        if rows == 0:
            return
        cols = len(board[0])

        for i in [0,rows-1]:
             for j in range(cols):
                 if board[i][j] == 'O':
                     self.dfs(board,i,j)

        for j in [0,cols-1]:
             for i in range(rows):
                 if board[i][j] == 'O':
                     self.dfs(board,i,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '1':
                    board[i][j] = 'O'

#%%
class Solution:
    def __init__(self):
        self.nums = 0

    def dfs(self,grid,r,c):
        print(self.nums)
        grid[r][c] = 0
        rows = len(grid)
        cols = len(grid[0])
        for x,y in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)]:
            if 0<=x<rows and 0<=y<cols and grid[x][y] == 1:
                self.nums +=1
                self.dfs(grid,x,y)

    def maxAreaOfIsland(self, grid) -> int:
        res = 0
        rows = len(grid)
        if rows == 0:
            return res
        cols = len(grid[0])



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.nums =1
                    self.dfs(grid,i,j)
                    if self.nums > res:
                        res = self.nums

        return res

test = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

print(Solution().maxAreaOfIsland(test))