#!/usr/bin/env python3

def print_fibonacci(lenght):
    fibonacci_sequence = [0, 1]  # Starting elements of the Fibonacci sequence
    while len(fibonacci_sequence) < lenght:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence[:lenght]

# Example usage:
result = print_fibonacci(9)
print(result)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]
