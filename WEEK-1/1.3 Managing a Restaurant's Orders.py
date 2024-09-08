from collections import deque

def calculate_total_time(orders, time_quantum):
    queue = deque(orders)
    current_time = 0

    while queue:
        order = queue.popleft()
        if order <= time_quantum:
            current_time += order
        else:
            current_time += time_quantum
            queue.append(order - time_quantum)

    return current_time

# Taking user input
orders = list(map(int, input("Enter the processing times for each order (space-separated): ").split()))
time_quantum = int(input("Enter the time quantum: "))

total_time = calculate_total_time(orders, time_quantum)

print(f"The total time required to complete all orders is: {total_time} minutes")
