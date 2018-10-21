# Uses python3
# naive algo: 
def naive_calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

# improved algo: 
def calc_fib(n):
    arr = [0, 1];
    for num in range(2, (n + 1)):
        arr.append(arr[num-1] + arr[num-2])

    return arr[n]

n = int(input())
print(calc_fib(n))
