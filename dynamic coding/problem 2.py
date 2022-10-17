'''
Ways to fill N positions using M colors such that there
are exactly K pairs of adjacent colors 

N positions
M colors
K pairs of diff adjacent colors

input : N=3 M=2 K=1
output : 4

1 1 2
1 2 2
2 2 1
2 1 1

above pairs have exactly one pair of adjacent elements with
diff colors

input : N=3 M=3 K=2
output : 12
'''

max = 5
def countWays(index,cnt,dp,n,m,k):
    # when all positions are filled
    if index == n:
        # if adjacent pairs are exactly K
        if cnt == k:
            return 1
        else:
            return 0
    # if already calculated
    if (dp[index][cnt] != 0):
        return dp[index][cnt]

    ans = 0
    # next position filled with same color
    ans += countWays(index + 1,cnt,dp,n,m,k)
    # next position filled with diff color
    # there can be m-1 diff color
    ans += (m-1)*countWays(index + 1, cnt + 1, dp,n,m,k)

    dp[index][cnt] = ans
    return dp[index][cnt]

# driver code
if __name__ == '__main__':
    n = 3
    m = 2
    k = 1
    dp = [[0 for x in range(n+1)]
              for y in range(max)]
    # print(dp)
    print(m*countWays(1,0,dp,n,m,k))







