def calculate_total_time(execution_times):
    # Sort the execution times in ascending order
    execution_times.sort()
    current_time = 0
    total_time = 0

    for time in execution_times:
        current_time += time
        total_time += current_time

    return total_time

# Taking user input
execution_times = list(map(int, input("Enter the execution times for each task (space-separated): ").split()))

total_time = calculate_total_time(execution_times)

print(f"The total time required to complete all tasks is: {total_time} hours")
