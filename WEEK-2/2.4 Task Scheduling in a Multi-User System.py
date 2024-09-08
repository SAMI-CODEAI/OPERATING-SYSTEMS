from queue import Queue


def calculate_total_time(high_priority_tasks, low_priority_tasks):
    system_queue = Queue()
    user_queue = Queue()

    for task, time in high_priority_tasks.items():
        system_queue.put(time)

    for task, time in low_priority_tasks.items():
        user_queue.put(time)

    current_time = 0
    total_time = 0

    while not system_queue.empty():
        time = system_queue.get()
        current_time += time
        total_time += current_time

    while not user_queue.empty():
        time = user_queue.get()
        current_time += time
        total_time += current_time

    return total_time


# Taking user input
high_priority_tasks = {}
low_priority_tasks = {}

num_high_priority_tasks = int(input("Enter the number of high priority (system) tasks: "))
for _ in range(num_high_priority_tasks):
    task_name = input("Enter the name of the high priority task: ")
    task_time = int(input(f"Enter the processing time for {task_name} (in units): "))
    high_priority_tasks[task_name] = task_time

num_low_priority_tasks = int(input("Enter the number of low priority (user) tasks: "))
for _ in range(num_low_priority_tasks):
    task_name = input("Enter the name of the low priority task: ")
    task_time = int(input(f"Enter the processing time for {task_name} (in units): "))
    low_priority_tasks[task_name] = task_time

total_time = calculate_total_time(high_priority_tasks, low_priority_tasks)
print(f"The total time required to complete all tasks is: {total_time} units")
