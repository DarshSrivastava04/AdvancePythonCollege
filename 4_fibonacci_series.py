def fib_memo(n, memo={}):
    """Top-down approach using memoization"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tab(n):
    """Bottom-up approach using tabulation"""
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


if __name__ == "__main__":
    n = int(input("Enter n: "))

    if n < 0:
        print("Please enter a non-negative number.")
    else:
        print(f"\nFibonacci({n}) using Memoization: {fib_memo(n)}")
        print(f"Fibonacci({n}) using Tabulation:  {fib_tab(n)}")