# Uses python3

# Formula: lcm = (a * b) / gcd(a, b)
def lcm(a, b):
    gcd_ab = gcd(a, b)
    lcm = (a * b) // gcd_ab
    return lcm

def gcd(a, b):
    while True:
        temp = a % b;
        if (temp == 0):
            return b
        a, b = b, temp

if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm(a, b))

