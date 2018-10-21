# python3
import sys

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]

    print(sum_of_two_digits(input_numbers[0], input_numbers[1]))
