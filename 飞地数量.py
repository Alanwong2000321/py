class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        # [0, 0, 0, 0]
        # [1, 0, 1, 0]
        # [0, 1, 1, 0]
        # [0, 0, 0, 0]
        if not A:
            return 0
        self.m = len(A)#m = len(A)
        self.n = len(A[0])#n = len(A)
        self.A = A
        for i in range(self.m):
            self.move(i, 0)
            self.move(i, self.n - 1)
        for i in range(self.n):
            self.move(0, i)
            self.move(self.m - 1, i)

        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.A[i][j] == 1:
                    count += 1
        return count

    def move(self, x, y):
        if x < 0 or x >= self.m or y < 0 or y >= self.n or self.A[x][y] == 0:
            return False
        else:
            self.A[x][y] = 0
            self.move(x + 1, y)
            self.move(x - 1, y)
            self.move(x, y + 1)
            self.move(x, y - 1)