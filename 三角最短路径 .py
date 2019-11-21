class Solution(object):
    def minimumTotal(self, t):
        if len(t) == 0:#如果没有
            return 0
        row = len(t) - 2#len（t） 为行数   如例子就为4
        for row in range(row, -1, -1):
            for col in range(len(t[row])):
                t[row][col] += min(t[row+1][col],t[row+1][col+1])
        return t[0][0]
    
#if __name__ == "__main__":
#   triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
#    min_sum = Solution().minimumTotal(triangle)
#    print(min_sum)