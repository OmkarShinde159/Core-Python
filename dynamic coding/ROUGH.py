
lst = [1,2,2,3,3,3]
count = 0
num = lst[0]

for i in lst:
    init = lst.count(i)
    if init > count:
        count = init
        num = i
print(num)

def find_max_count(lst):
    return max(set(lst), key = lst.count)

lst = [1,2,2,3,3,3]
print(find_max_count(lst))

from collections import Counter
def most_frequent(lst):
    occurance_count = Counter(lst)
    print(occurance_count)
    return occurance_count.most_common(1)[0][0]

lst = [1,2,2,3,3,3,5,4]
print(most_frequent(lst))

import statistics
from statistics import mode

def most_common(lst):
    return(mode(lst))

lst = [1,2,2,3,3,3,5,4]
print(most_common(lst))

def most_avl(lst):
    dict = {}
    count, itm = 0,''
    for item in reversed(lst):
        # print(item)
        dict[item] = dict.get(item,0)+1
        # print(dict[item])
        if dict[item] >= count:
            count,itm = dict[item], item
    return(itm)

lst = [1,2,2,3,3,3,5,4]
print(most_avl(lst))



