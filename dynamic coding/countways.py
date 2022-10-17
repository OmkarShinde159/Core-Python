'''
input 3 integers n,m,k
where
n = positons
m = colors
k = adjacent color pairs
'''
# input : n = 3,m=2, k=1
# output : 4
# colours are 1,2
# ways are 112,122,221,211
'''
n n n
1 1 2
1 2 2
2 2 1
2 1 1
'''

max = 4
def countWays(index, cnt, dp, n, m, k):
    if (index == n):
        if (cnt==k):
            return 1
        else:
            return 0

    if (dp[index][cnt] != -1):
        return dp[index][cnt]

    ans = 0
    # next position filled with the same color
    ans += countWays(index + 1, cnt,dp,n,m,k)

    # next position filled with different color
    # so there can be m-1 different colors
    ans += (m-1)*countWays(index + 1, cnt+1,dp,n,m,k)
    dp[index][cnt] = ans
    return dp[index][cnt]

# Driver code
if __name__=='__main__':
    n=3
    m=3
    k=2
    dp = [[-1 for x in range(n+1)]
            for y in range(max)]
    print(m*countWays(1,0,dp,n,m,k))






