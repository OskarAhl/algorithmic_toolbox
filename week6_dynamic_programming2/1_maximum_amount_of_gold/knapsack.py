# Uses python3

# No repetitions - 0/1 knapsack problem
def max_gold(bag_W, goldbar_weights):
    if bag_W == 0:
        return 0
    
    # Create matrix for max_values
    matrix_max_vals = [[0] * (bag_W + 1) for x in range(len(goldbar_weights))]
    matrix_max_vals[0] = [goldbar_weights[0] if goldbar_weights[0] <= j else 0 for j in range(bag_W + 1)]

    for goldbar in range(1, len(goldbar_weights)):
        for b_W in range(1, bag_W + 1):
            prev = matrix_max_vals[goldbar - 1][b_W]
            if goldbar_weights[goldbar] <= b_W:
                curr = (matrix_max_vals[goldbar - 1][b_W - goldbar_weights[goldbar]]) + goldbar_weights[goldbar]
                if prev < curr:
                    prev = curr
                    matrix_max_vals[goldbar][b_W] = prev
                else:
                    matrix_max_vals[goldbar][b_W] = prev
            else:
                matrix_max_vals[goldbar][b_W] = prev
    # print(matrix_max_vals)
    return matrix_max_vals[-1][-1]

if __name__ == '__main__':
    bag_weight, goldbar_weight = [], []
    bag_weight = [int(x) for x in input().split()][0]
    # bag_weight = int(input())
    goldbar_weight = [int(x) for x in input().split()]
    print(max_gold(bag_weight, goldbar_weight))
