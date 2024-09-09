# def calculate_total_time(execution_times):
#     # Sort the execution times in ascending order
#     execution_times.sort()
#     current_time = 0
#     total_time = 0
#
#     for time in execution_times:
#         current_time += time
#         total_time += current_time
#
#     return total_time
#
# # Taking user input
# execution_times = list(map(int, input("Enter the execution times for each task (space-separated): ").split()))
#
# total_time = calculate_total_time(execution_times)
#
# print(f"The total time required to complete all tasks is: {total_time} hours")




class Task:
    def __init__(self, name, execution_time):
        self.name = name
        self.execution_time = execution_time

def simulate_sjf(tasks):
    # Sort tasks by their execution times (Shortest Job First)
    tasks.sort(key=lambda task: task.execution_time)

    # Variables to track the time
    current_time = 0
    completion_times = []

    for task in tasks:
        start_time = current_time
        end_time = start_time + task.execution_time
        completion_times.append((task.name, start_time, end_time))

        # Update current time
        current_time = end_time

    return completion_times

def main():
    # Define the tasks
    tasks = [
        Task('A', 3),
        Task('B', 5),
        Task('C', 7),
        Task('D', 4)
    ]

    # Simulate SJF scheduling
    completion_times = simulate_sjf(tasks)

    # Output results
    print("Task Completion Times:")
    for task_name, start_time, end_time in completion_times:
        print(f"Task {task_name}: Start Time = {start_time} hours, End Time = {end_time} hours")

    # Total time to complete all tasks
    total_time = completion_times[-1][2]  # End time of the last task
    print(f"Total time to complete all tasks: {total_time} hours")

if __name__ == "__main__":
    main()
