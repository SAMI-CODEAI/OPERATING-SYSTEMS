# from collections import deque
#
# def calculate_total_time(orders, time_quantum):
#     queue = deque(orders)
#     current_time = 0
#
#     while queue:
#         order = queue.popleft()
#         if order <= time_quantum:
#             current_time += order
#         else:
#             current_time += time_quantum
#             queue.append(order - time_quantum)
#
#     return current_time
#
# # Taking user input
# orders = list(map(int, input("Enter the processing times for each order (space-separated): ").split()))
# time_quantum = int(input("Enter the time quantum: "))
#
# total_time = calculate_total_time(orders, time_quantum)
#
# print(f"The total time required to complete all orders is: {total_time} minutes")




from collections import deque

def round_robin_scheduling(order_times, time_quantum):
    # Initialize the queue with (order_index, remaining_time)
    queue = deque((i, time) for i, time in enumerate(order_times))

    current_time = 0
    while queue:
        # Get the next order in the queue
        order_index, remaining_time = queue.popleft()

        # Process the order for the minimum of time quantum or remaining time
        processing_time = min(time_quantum, remaining_time)

        # Update the remaining time
        remaining_time -= processing_time

        # Increase the total time elapsed
        current_time += processing_time

        # If the order is not yet complete, put it back in the queue
        if remaining_time > 0:
            queue.append((order_index, remaining_time))

    return current_time

# Input: Processing times for each order
order_times = [5, 3, 8, 6]
time_quantum = 4

# Calculate total time required using Round Robin scheduling
total_time = round_robin_scheduling(order_times, time_quantum)
print(f"Total time required to complete all orders: {total_time} minutes")
