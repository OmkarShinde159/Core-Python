# maximum value - max()
# minimum value - min()

l = [2,1,0,-1,4]

def minimum(l):
    min = l[0]      # 2 1 0 -1
    for i in l:
        if i < min:   # 2 1 0 4 -1
            min = i
    return min

print(minimum(l))

def maximum(l):
    max = l[0]  2 4
    for i in l:
        if i > max: 2 1 0 -1 4
            max = i
    return max

print(maximum(l))


