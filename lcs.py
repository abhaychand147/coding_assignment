def lcs(string1, string2):
    n = len(string1) + 1
    m = len(string2) + 1
    dp = [[0]*(m) for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if string1[i-1]==string2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
    return dp[n-1][m-1] - 1
    