def knapsack(weights, values, n, capacity, memo):
    if n == 0 or capacity == 0:
        return 0

    if memo[n][capacity] != -1:
        return memo[n][capacity]

    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack(weights, values, n - 1, capacity, memo)
    else:
        include = values[n - 1] + knapsack(
            weights, values, n - 1, capacity - weights[n - 1], memo
        )
        exclude = knapsack(weights, values, n - 1, capacity, memo)
        memo[n][capacity] = max(include, exclude)

    return memo[n][capacity]


weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5
n = len(weights)

memo = [[-1] * (capacity + 1) for _ in range(n + 1)]

print("Maximum value using Top-Down:", knapsack(
    weights, values, n, capacity, memo
))
