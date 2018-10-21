# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def get_fibonacci_sum_last_digit(n):
    kPisanoSize = 60;
    rest = n % kPisanoSize;
    #
    preparedNumbers = [0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 
        2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 
        6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 
        4, 6, 1, 8, 0, 9, 0];
    return preparedNumbers[rest];

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_naive(n))
    print(get_fibonacci_sum_last_digit(n))