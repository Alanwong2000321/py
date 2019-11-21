class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click[0],click[1]
        if board[x][y] == "M":#未挖出的地雷
            board[x][y] = "X"#已挖出的地雷
            return board

        m, n = len(board), len(board[0])
        vis = [[0 for _ in range(n + 1)] for j in range(m + 1)]
        

        dx = [1, 1, -1, -1, 0, 0, -1, 1]
        dy = [1, 0, -1, 0, 1, -1, 1, -1]

        def dfs(x0,y0):
            if board[x0][y0] == "M" or vis[x0][y0] == 1:
                return

            vis[x0][y0] = 1
            mine = 0
            for k in range(8):
                x = x0 + dx[k]
                y = y0 + dy[k]

                if 0 <= x < m and 0 <= y < n  and board[x][y] == "M":
                    mine += 1

            if mine > 0:
                board[x0][y0] = str(mine)
            else:
                board[x0][y0] = "B"#已挖的空白方格 且周围没有地雷

                for k in range(8):
                    x = x0 +dx[k]
                    y = y0 +dy[k]


                    if 0 <= x < m and 0 <= y < n and vis[x][y] == 0:
                        dfs(x,y)



        dfs(x,y)
        return board