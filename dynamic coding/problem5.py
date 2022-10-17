'''
ways of transforming one string to other by removing 0 or 
more characters

given 2 sequences A B find out number of unique ways in 
sequence A  to form a subsequence of A 
that is identical to sequence B
Transformation is meant by converting string A to string B

A : abcccdf
B : abccdf
'''
def countTransformation(a,b):
    n = len(a)
    m = len(b)

    if m==0:
        return 1
    
    dp = [[0]*(n) for _ in range(m)]
    # print(dp)

    # fill dp[][] in bottom up manner
    # traverse all characters of b[]
    for i in range(m):
        # traverse all characters of a[] for b[i]
        for j in range(i,n):
            # filling first row of dp
            # matrix
            if i==0:
                if j==0:
                    if a[j] == b[i]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                elif a[j] == b[i]:
                    dp[i][j] = dp[i][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]
            
            # filling other rows
            else:
                if a[j] == b[i]:
                    dp[i][j] = (dp[i][j-1]+dp[i-1][j-1])
                else:
                    dp[i][j] = dp[i][j-1]

    return dp[m-1][n-1]


# driver code
if __name__ == '__main__':
    a = 'abcccdf'
    b = 'abccdf'
    print(countTransformation(a,b))

                



