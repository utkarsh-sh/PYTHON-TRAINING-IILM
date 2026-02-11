class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"Value: {self.value}, Weight: {self.weight}"

def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0.0  
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break  

    return total_value


if __name__ == "__main__":
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]

    knapsack_capacity = 50
    max_value = fractional_knapsack(knapsack_capacity, items)
    print(f"Maximum value in the knapsack: {max_value:.2f}")
