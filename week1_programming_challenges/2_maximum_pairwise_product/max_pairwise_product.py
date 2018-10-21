# python3

def max_pairwise_product(numbers):
    if len(numbers) == 1:
        return numbers[0];
    sorted_arr = sorted(numbers, reverse=True)
    return sorted_arr[0] * sorted_arr[1]

# def max_pairwise_product(numbers):
#     if len(numbers) == 1:
#         return numbers[0];
#     num_one = 0
#     num_two = 0
#     for idx, num in enumerate(numbers):
#         if num > numbers[num_one]:
#             num_one = idx

#     for idx, num in enumerate(numbers):
#         if num > numbers[num_two] and idx != num_one:
#             num_two = idx
    
#     return numbers[num_one] * numbers[num_two]

if __name__ == '__main__':
    discard = int(input())
    nums = input().strip().split()
    nums = [ int(i) for i in nums ]
    print(max_pairwise_product(nums))
