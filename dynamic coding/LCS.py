# find the longest common subsequence
# input : x = 'AGGTAB'
#       : y = 'GXTXAYB'
# OUTPUT: 4

# dp = [[-1 for i in range(n+1)]for j in range(m+1)]
dp = [[-1 for i in range(10)]for j in range(10)]
# print(dp)
# memoization

def lcs(X,Y,m,n):
    if (m==0 or n==0):
        return 0

    if X[m-1] == Y[n-1]:
        dp[m][n] = 1+lcs(X,Y,m-1,n-1)
        return dp[m][n]

    dp[m][n] = max(lcs(X,Y,m,n-1),lcs(X,Y,m-1,n))
    return dp[m][n]

# driver code

X = "AGGTAB"
Y = "GXTXAYB"
 
m = len(X)
n = len(Y)
# dp = [[-1 for i in range(n+1)]for j in range(m+1)]
print("LCS", lcs(X,Y,m,n))
