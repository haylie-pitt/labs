import time

def memoize(f):
    """A decorator to cache results of the function."""
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    
    return wrapper

@memoize
def recur_fibo(n):
    """Standard recursive Fibonacci function with memoization."""
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

def original_recur_fibo(n):
    """Original recursive Fibonacci function without memoization."""
    if n <= 1:
        return n
    else:
        return original_recur_fibo(n-1) + original_recur_fibo(n-2)

# Testing
if __name__ == "__main__":
    n = 35
    
    # Testing original function
    start = time.time()
    original_result = original_recur_fibo(n)
    end = time.time()
    print(f"Original Fibonacci({n}): {original_result} (Time: {end - start:.4f} seconds)")

    # Testing memoized function
    start = time.time()
    memoized_result = recur_fibo(n)
    end = time.time()
    print(f"Memoized Fibonacci({n}): {memoized_result} (Time: {end - start:.4f} seconds)")
