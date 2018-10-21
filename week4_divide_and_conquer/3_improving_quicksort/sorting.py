# Uses python3
import random

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

# implement 3 way partition: 
def partition3(arr, left, right):
    # 1. choose pivot as first el 
    # 2. greater than to right
    #        less than to left
    #        equal keep
    # return arr with [less, greater]
    pivot = arr[left]
    lt = left
    gt = right
    border = left
    while(border <= gt):
        if (arr[border] < pivot):
            arr[border], arr[lt] = arr[lt], arr[border]
            lt += 1
            border += 1
        elif (arr[border] > pivot): 
            arr[border], arr[gt] = arr[gt], arr[border]
            gt -= 1
        else:
            border += 1
    m = [lt, gt]
    return m

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m[0] - 1)
    randomized_quick_sort(a, m[1] + 1, r)


if __name__ == '__main__':
    discard = input()
    arr = [int(x) for x in input().split()]
    randomized_quick_sort(arr, 0, len(arr) - 1)
    print(' '.join(map(str, arr)))
