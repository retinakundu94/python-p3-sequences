#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  # Updated to print an empty list for non-positive length
    elif length == 1:
        print([0])
    else:
        fibonacci_list = [0, 1]
        for i in range(2, length):
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_number)
        print(fibonacci_list)