
def check(grid):
    left = len(grid) #m matrix
    right = len(grid[0]) #n matrix
    dp = [[0] * right for _ in range(left)] #dp - dynamic programming concept
    
    if grid[0][0] == 0 : #initilly 0 means return 1 else 0
        dp[0][0] = 1
    else:
        return 0
    
    for val1 in range(left):  
        for val2 in range(right):
            if grid[val1][val2] == 1: # if m*n is 1 return 0 else check m>0 then return m-1*n else return m*n-1
                dp[val1][val2] = 0
            else:
                if val1 > 0:
                    dp[val1][val2] += dp[val1 - 1][val2]
                if val2 > 0:
                    dp[val1][val2] += dp[val1][val2 - 1]

    return dp[left-1][right-1] #return m-1*n-1 to find the unique path

grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
answer = check(grid)
print(f"Result for unique path : " ,answer)
