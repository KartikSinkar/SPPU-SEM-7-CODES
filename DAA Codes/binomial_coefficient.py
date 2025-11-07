def binomial_coefficient(n, k):
    # Create a 2D DP table to store intermediate results
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Calculate values using bottom-up dynamic programming
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base cases: C(i, 0) = 1 and C(i, i) = 1
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]


if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    k = int(input("Enter the value of k: "))

    print(f"\nBinomial Coefficient C({n}, {k}) =", binomial_coefficient(n, k))
