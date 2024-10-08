#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

#first generate the fibonacci numbers less than the given limit, limit will be what we put in 
def fib(limit):
    numbers = []
    F1 = 0 
    F2 = 1 
    
    while F1 < limit: 
        numbers.append(F1) 
        next_number = F1 + F2  # Stores the next Fibonacci number 
        F1 = F2  # Update F1 to the current F2
        F2 = next_number  # Update F2 after being calculated
    return numbers

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", type=int, help="Upper Limit for Fibonacci numbers")
    parser.add_argument("filename", help="Output File Name")
    
    args = parser.parse_args()

    with open(args.filename, 'w') as f:
        f.write(f"Fibonacci numbers less than {args.limit}:\n")
        for number in fib(args.limit):
            f.write(f"{number}\n")  # Write each number followed by a newline

    print(f"Fibonacci numbers less than {args.limit} have been written to {args.filename}.")
        
      
