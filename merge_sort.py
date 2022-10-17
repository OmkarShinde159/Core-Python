from turtle import left, right


def merge_sort(list):
    '''
    sorts a list in ascending order
    returns a new sorted list
    
    devide: find the midpoint of the list and devide into sublist
    conquer: recursively sort the sublists created in previous step
    combine: merge the sorted sublists created in previous step
    '''

    # base case : single element list or empty list
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return  merge(left,right)

def split(list):
    '''
    devide the unsorted list at midpoint into sublists
    returns two sublists - left and right
    '''
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left,right):
    '''
    merges two list(arrays), sorting them in process
    returns a new merged list
    '''
    l = []
    i = 0
    j = 0
    while i <len(left) and j<len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return l

def verify_sorted(list):
    n = len(list)

    if n==0 or n==1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54,23,62,92,17,77,31,44,55,20]
l = merge_sort(alist)
print(l)
print(verify_sorted(alist))
print(verify_sorted(l))




