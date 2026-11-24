# Calculate the nth Fibonacci number efficiently

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = int(input("Enter n: "))
print(f"Fibonacci number at position {n} is {fibonacci(n)}")
