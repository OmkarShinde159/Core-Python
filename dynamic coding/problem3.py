'''
ways to arrange balls such that adjacent balls are of 
diff types
balls p q r
input p=1, q=1, r=0
output 2
ways : pq qp

input p=1, q=1,r=1
output 6
ways  pqr prq qpr qrp rpq rqp

input: p=2, q=1, r=1
output : 6
ways   : PQRP QPRP PRQP RPQP PRPQ PQPR

RETURN THE count of arrangements
last placed ball is 'last'
last is 0 for p
1 for q
2 for r
'''

def countWays(p,q,r,last):
    # if no of balls of any color becomes less than 0
    # then the no of ways is 0
    if (p<0 or q<0 or r<0):
        return 0

    # if one ball type is given and rest is 0 then ways is 1
    if (p==1 and q==0 and r==0 and last==0):
        return 1
    if (p==0 and q==1 and r==0 and last==1):
        return 1
    if (p==0 and q==0 and r==1 and last==2):
        return 1

    # if last ball req is P and number of ways is the sum
    # of number of ways to form sequence with p-1

    if (last==0):
        return(countWays(p-1,q,r,1)+ countWays(p-1,q,r,2))
    if (last==1):
        return(countWays(p,q-1,r,0)+countWays(p,q-1,r,2))
    if (last==2):
        return(countWays(p,q,r-1,0)+countWays(p,q,r-1,1))


def countUtil(p,q,r):
    # three cases arises
    # last ball require is either P Q R
    return (countWays(p,q,r,0)+
            countWays(p,q,r,1)+
            countWays(p,q,r,2))

# driver code
p = 1
q = 1
r = 1
# print(countUtil(p,q,r))





