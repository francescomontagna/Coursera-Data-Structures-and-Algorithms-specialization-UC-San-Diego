# python3
import random
import time
import numpy as np

def max_pairwise_product(numbers):
    # First, I try to update the max: 
    # if I fail
    #    I try to update the 2nd larger
    # else
    #    Take the larger, make it the 2nd larger, and then update the largest
    # 
    # This algorithm is O(n)
    
    first = second = 0
    for el in numbers:
        if el > first:
            second = first
            first = el
        elif el > second:
            second = el

    return second*first


def naive(numbers):
    n = len(numbers)
    product = 0
    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, numbers[i] * numbers[j])
        
    return product


if __name__ == '__main__':
    
    # Stress test
    fast_sol_time = 0
    naive_sol_time = 0
    for _ in range(1000):
        input_n = random.choice(range(100)) # kength of the sequence randomly selected
        input_numbers = [np.random.choice(range(1000)) for _ in range(input_n)]
        start = time.time()
        fast_sol = max_pairwise_product(input_numbers)
        fast_sol_time += time.time() - start
        
        start = time.time()
        naive_sol = naive(input_numbers)
        naive_sol_time += time.time() - start
        assert fast_sol == naive_sol, "The 2 algorithms gave different results!" +\
                         f"fast: {fast_sol}, naive: {naive_sol}"
        
    print(f"Success! The 2 algorithms work the same. Fast sol time {fast_sol_time}s, naive sol time {naive_sol_time}s")
