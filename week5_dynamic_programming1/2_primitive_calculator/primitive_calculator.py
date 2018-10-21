# Uses python3
import sys
# 1. multiply by 2, multiply by 3, or add 1
# given number n - find minimum nr of operations needed - starting from 1

# input:  5
# output: 
# 3 operations
# 1 2 4 5 - multiply 1 by 2 two times add 1 

# step 1: find recurrence of this problem
# e.g. for n = 1 - occurence is 1 
#... for n = 2 - occurrence is 1
#... for n = 4 - occurrence is: 4 = (4 / 2) * 2 or 4 = (4 - 1) + 1
# General recurrence: opt(n) = 
# min { 
#   1. if n % 3 --> opt(n / 3) + 1 
#   2. if n % 2 --> opt(n / 2) + 1
#   else --> opt(n - 1) + 1

def get_min_ops(n):
    min_results = []
    for i in range(0, n+1):
        min_results.append(0)
    for i in range(2, n+1):
        min_1 = min_results[i-1]
        min_2 = n
        min_3 = n
        if i % 2 == 0:
            min_2 = min_results[int(i/2)]
        if i % 3 == 0:
            min_3 = min_results[int(i/3)]
        min_op = min(min_1, min_2, min_3)

        min_results[i] = min_op + 1

    return min_results

def make_list(n, min_ops):
    seq = []
    while n > 0:
        seq.append(n)
        if n % 2 != 0 and n % 3 != 0:
            n = n - 1
        elif n % 2 == 0 and n % 3 == 0: 
            n = n // 3
        elif n % 2 == 0:
            if min_ops[n-1] < min_ops[n//2]:
                n = n-1
            else:
                n = n // 2
        elif n % 3 == 0: 
            if min_ops[n-1] < min_ops[n//3]:
                n = n-1
            else:
                n = n // 3
    return seq[::-1]

if __name__ == '__main__':
    n = int(input())
    min_operations = get_min_ops(n)
    min_list = make_list(n, min_operations)
    print(len(min_list) - 1)
    print(' '.join(map(str, min_list)))