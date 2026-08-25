# Fibonacci using Memoization (Top-Down DP)

def fibonacci(n, memo={}):
    # Base cases
    if n <= 1:
        return n

    # Return already calculated value
    if n in memo:
        return memo[n]

    # Calculate and store the result
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


# Input
n = int(input("Enter the value of N: "))

# Output
print("The", n, "th Fibonacci number is:", fibonacci(n))
