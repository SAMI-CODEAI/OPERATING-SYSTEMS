def calculate_total_time(arrival_times, pages):
    current_time = 0
    total_time = 0

    for i in range(len(arrival_times)):
        if current_time < arrival_times[i]:
            current_time = arrival_times[i]
        current_time += pages[i]
        total_time = current_time

    return total_time

# Taking user input
arrival_times = list(map(int, input("Enter the arrival times (space-separated): ").split()))
pages = list(map(int, input("Enter the number of pages for each job (space-separated): ").split()))

total_time = calculate_total_time(arrival_times, pages)

print(f"The total time taken to complete all printing tasks is: {total_time} seconds")
