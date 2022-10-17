# Python3 program to count number of ways to
# arrange three types of balls such that no
# two balls of same color are adjacent to each other

max = 100 # assume
# table to store the result of subproblem
dp = [[[[-1]*4 for i in range(max)] 
                for j in range(max)]
                for k in range(max)]
# print(dp)

def countways(p,q,r,last):
    # base case
    if (p<0 or q<0 or r<0):
        return 0
    
    if (p==1 and q==0 and r==0 and last==0):
        return 1
    if (p==0 and q==1 and r==0 and last==1):
        return 1
    if (p==0 and q==0 and r==1 and last==2):
        return 1

    if (dp[p][q][r][last] != -1):
        return dp[p][q][r][last]

    if (last==0):
        dp[p][q][r][last] = (countways(p-1,q,r,1) + 
                             countways(p-1,q,r,2))
    elif (last==1):
        dp[p][q][r][last] = (countways(p,q-1,r,0)+
                             countways(p,q-1,r,2))
    else:
        # last==2
        dp[p][q][r][last] = (countways(p,q,r-1,0)+
                             countways(p,q,r-1,1))

    # print(dp[p][q][r][last], end=",")
    return dp[p][q][r][last]

# returns count of required arrangements
def countUtil(p,q,r):
    return(countways(p,q,r,0)+countways(p,q,r,1)+countways(p,q,r,2))


# Driver code
p,q,r = 1,1,1
print(countUtil(p,q,r))

    
# l = [[[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]]]
# print(l[0])
# print(l[0][0])
# print(l[0][0][0])
# print(l[0][0][1][0:2])

