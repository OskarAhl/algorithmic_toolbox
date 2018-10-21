
def largestNumber(number_arr):
    # sort based on first digit
    answer = ''
    while len(number_arr) > 0:
        max_digit = 0
        for idx, digit in enumerate(number_arr):
            if isGreaterOrEqual(digit, max_digit): 
                max_digit = digit
        answer += str(max_digit)
        number_arr.remove(max_digit)
    return answer

def isGreaterOrEqual(a, b): 
  num_one_arr = list(map(int, str(a)))
  num_two_arr = list(map(int, str(b)))
  print(num_one_arr, num_two_arr)
  while (len(num_one_arr) > 0) and (len(num_two_arr) > 0):
    if (num_one_arr[0] < num_two_arr[0]):
      return False
    if (num_one_arr[0] > num_two_arr[0]):
        return True
    if (num_one_arr[0] == num_two_arr[0]):
      del num_one_arr[0]
      del num_two_arr[0]

  if len(num_one_arr) == 0:
    return True
  return False


if __name__ == '__main__':
    # discard = input()
    numbers = [int(x) for x in input().split()]
    print(largestNumber(numbers))