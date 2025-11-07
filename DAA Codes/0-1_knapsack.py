from tabulate import tabulate

def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp, dp[n][capacity]


def find_selected_items(dp, weights, values, capacity):
    n = len(weights)
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()
    return selected_items


# ---- Main Program ----
weights = []
values = []

n = int(input("Enter number of items: "))

for i in range(n):
    w = int(input(f"Enter weight of item {i + 1}: "))
    v = int(input(f"Enter value of item {i + 1}: "))
    weights.append(w)
    values.append(v)

capacity = int(input("Enter maximum capacity of knapsack: "))

# Solve knapsack
dp_table, max_value = knapsack_01(weights, values, capacity)
selected_items = find_selected_items(dp_table, weights, values, capacity)

# Print DP Table
headers = [f"W={w}" for w in range(capacity + 1)]
dp_table_for_print = [row for row in dp_table]

print("\n📘 Dynamic Programming Table:")
print(tabulate(dp_table_for_print, headers=headers, showindex="always", tablefmt="grid"))

# Print results
print("\n✅ Maximum Value in Knapsack:", max_value)
print("🎒 Selected item indices (0-based):", selected_items)
print("📦 Selected item weights and values:")
for idx in selected_items:
    print(f" - Item {idx}: Weight = {weights[idx]}, Value = {values[idx]}")
