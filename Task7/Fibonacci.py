#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    
    def get_nth_term(self, n):
        """
        1. Returns the N-th term Fibonacci number.
        Assuming 0-based indexing: 0th term is 0, 1st is 1, 2nd is 1, 3rd is 2...
        """
        if n < 0:
            return "N must be a non-negative integer."
        if n == 0:
            return 0
            
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b

    def get_divisible_less_than_nth(self, n, m):
        """
        2. Returns all Fibonacci numbers less than the N-th term 
        that can be divided by M.
        """
        nth_term_value = self.get_nth_term(n)
        divisible_numbers = []
        
        a, b = 0, 1
        # Generate the sequence up until we hit the N-th term
        while a < nth_term_value:
            # Check if the current number a is evenly divisible by m
            if a % m == 0:
                divisible_numbers.append(a)
            # Move to the next sequence numbers
            a, b = b, a + b
            
        return divisible_numbers

# Test for N=100, M=7 

# Instantiate the object
fib_calculator = Fibonacci()

N = 100
M = 7

# 1. Get the 100th term
nth_term = fib_calculator.get_nth_term(N)
print(f"The {N}-th Fibonacci term is:\n{nth_term}\n")

# 2. Get the divisible numbers
divisible_list = fib_calculator.get_divisible_less_than_nth(N, M)
print(f"Fibonacci numbers less than the {N}-th term that are divisible by {M}:")
print(divisible_list)

