# Uses python3
def get_change(m):
    if (m < 1):
        return m
    change = 0;
    change_types = [10, 5, 1]
    # safe move: 1. return as many 10s as possible -> then move to 5s, 1s
    # step 2: update m
    for ct in change_types:
        # rounds down to nearest whole nr
        remain = int(m / ct)
        change += remain
        # step 2: update m
        m = m - (remain * ct)
    return change

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
