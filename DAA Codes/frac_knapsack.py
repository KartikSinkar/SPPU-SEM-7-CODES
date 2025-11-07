def fractional_knapsack():
    # Take number of items from user
    n = int(input("Enter number of items: "))

    weights = []
    values = []

    # Input item details
    for i in range(n):
        w = float(input(f"Enter weight of item {i + 1}: "))
        v = float(input(f"Enter value of item {i + 1}: "))
        weights.append(w)
        values.append(v)

    capacity = float(input("Enter maximum capacity of knapsack: "))
    res = 0

    # Sort items by value/weight ratio in decreasing order
    for pair in sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True):
        if capacity <= 0:
            break

        weight, value = pair

        if weight > capacity:
            res += capacity * (value / weight)  # Take fractional part
            capacity = 0
        else:
            res += value  # Take whole item
            capacity -= weight

    print("\nMaximum value in Knapsack:", res)


if __name__ == "__main__":
    fractional_knapsack()
