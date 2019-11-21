class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        x,y,time = len(grid),len(grid[0]),0
        locs = [[-1,0],[0,-1],[0,1],[1,0]]
        stack = []
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 2:
                    stack.append((i,j,0))
        while stack:  
            i,j,time = stack.pop(0)
            for loc in locs:
                loc_i,loc_j = i+loc[0],j+loc[1]
                if 0 <=loc_i<x and 0<=loc_j<y and grid[loc_i][loc_j]==1:
                    grid[loc_i][loc_j] = 2
                    stack.append((loc_i,loc_j,time+1))
        for g in grid:
            if 1 in g:
                return -1
        return time