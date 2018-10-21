# Uses python3
# return index of key in search_list
# get midpoint compare search left or right - repeat
def binary_search_recursive(search_list, low, high, key):
    if low > high:
        # if number not found and lower than highest in the list
        if search_list[low-1] == key:
            return low - 1
        return -1
    mid = low + ((high - low) // 2)
    # if number not found and higher than any number in the list
    if mid > (len(search_list) - 1):
        return -1;
    if key == search_list[mid]:
        return mid
    if key < search_list[mid]:
        # search "to left" of middle
        return binary_search(search_list, low, mid - 1, key)
    # else search "to right" of middle
    return binary_search(search_list, mid + 1, high, key)

# non - recursive solution
def binary_search(search_list, key):
    low, high = 0, len(search_list) - 1 
    while(low <= high):
        mid = low + ((high - low) // 2)
        if (key == search_list[mid]):
            return mid
        #  if key is less than middle - search left by setting high to middle - 1
        if (key < search_list[mid]):
            high = mid - 1
        else:
        #  if key is higher than middle - search right by setting low to middle + 1    
            low = mid + 1
    return -1


if __name__ == '__main__':
    search_list = [int(x) for x in input().split()][1:]
    find_list = [int(x) for x in input().split()][1:]
    results = []
    for i in find_list:
        results.append(binary_search(search_list,i))
    print(" ".join(str(x) for x in results))
    


