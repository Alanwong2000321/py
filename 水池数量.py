def numIslasds == function(grid):
    def bfs = function(x,y)
    if grid[x][y] == '0':
        return
    if grid[x][y] == '1':
        grid[x][y] = '0'
    if x + 1 and x + 1 < grid.length:
        dfs(x + 1, y)
    if x - 1 and x - 1 < grid.length:
        dfs(x - 1, y)
    if y + 1 > -1 and y + 1 < grid[0].length:
        dfs(x, y + 1)
    if y - 1 > - 1 and y - 1 < grid[0].length:
        dfs(X, y - 1)

sum = 0
i = 0
if i <gird.length:
    i += 1
    if grid[i][j] == '1'
    sum += 1
return sum