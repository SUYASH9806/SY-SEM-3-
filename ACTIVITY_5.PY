# Program to find Longest Common Subsequence (LCS)
# using Dynamic Programming

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS
    i = m
    j = n
    result = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            result.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the result
    result.reverse()

    return ''.join(result), dp[m][n]


# Input two sequences
X = input("Enter first sequence: ")
Y = input("Enter second sequence: ")

# Find LCS
sequence, length = lcs(X, Y)

print("Longest Common Subsequence:", sequence)
print("Length of LCS:", length)
