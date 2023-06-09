#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    #To check if length is valid
    if length < 0:
        print("Invalid length. Please provide a positive integer.")
        return
    elif length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    #We need to initialize the first two numbers of the sequence
    #The first number is always 0
    #The second number is always 1
    
    fibonacci_sequence = [0, 1]
    
    #To generate our Fibonacci sequence
    
    while len(fibonacci_sequence) < length:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
        
    print(fibonacci_sequence)
    
    