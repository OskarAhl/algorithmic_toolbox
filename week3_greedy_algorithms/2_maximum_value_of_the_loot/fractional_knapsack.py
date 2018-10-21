# Uses python3

def fractional_knapsack(capacity, weights, values):    
    # List<item> --- item = [0: value/weight, 1: i, 2: value, 3: weight]
    item_arr_sorted = []
    value = 0
    for i in range(len(weights)):
        item_arr_sorted.append([values[i] / weights[i], i, values[i], weights[i]])

    # Step 1: sort according to value / weight
    item_arr_sorted.sort(reverse=True)

    # Step 2: safe choice - 1. take as many as possible of highest item 2. Update capacity
    # --> move to next item
    for item in item_arr_sorted:
        to_take = capacity if capacity <= item[3] else item[3]
        capacity -= to_take
        value += round(to_take * item[0], 4)
        if(capacity == 0):
            break
    value = format(value, '.4f')
    return value

if __name__ == "__main__":
    weights, values = [], []
    capacity_and_nr_inputs = [int(x) for x in input().split()]
    capacity = capacity_and_nr_inputs[1]
    nr_inputs = capacity_and_nr_inputs[0]
    for i in range(nr_inputs):
        weight_values = capacity_and_nr_inputs = [int(x) for x in input().split()]
        values.append(weight_values[0])
        weights.append(weight_values[1])
    opt_value = fractional_knapsack(capacity, weights, values)
    print(opt_value)