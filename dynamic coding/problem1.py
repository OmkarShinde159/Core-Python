'''
color n boxes using m colors such that k boxes have different
color from the box on its left
'''

M = 1001
MOD = 998244353

dp = [[-1]*M]*M
# print(dp)
def solve(idx, diff, N,M,K):
    # base case
    if idx > N:
        if(diff==K):
            return 1
        return 0
    
    if (dp[idx][diff] != -1):
        return dp[idx]
    # paint with same color as previous one
    ans = solve(idx+1, diff,N,M,K)
    # orpaint with remaining m-1 colors
    ans += (M-1)*solve(idx+1,diff+1,N,M,K)
    
    dp[idx][diff]= ans % MOD
    return dp[idx][diff]

# Driver code
if __name__=='__main__':
    N = 3
    M = 3
    K = 0

    print(M*solve(2,0,N,M,K))


        
        