from queue import Queue


def calculate_total_time(system_processes, user_processes):
    system_queue = Queue()
    user_queue = Queue()

    for process, time in system_processes.items():
        system_queue.put(time)

    for process, time in user_processes.items():
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
system_processes = {}
user_processes = {}

num_system_processes = int(input("Enter the number of system processes: "))
for _ in range(num_system_processes):
    process_name = input("Enter the name of the system process: ")
    process_time = int(input(f"Enter the processing time for {process_name} (in units): "))
    system_processes[process_name] = process_time

num_user_processes = int(input("Enter the number of user processes: "))
for _ in range(num_user_processes):
    process_name = input("Enter the name of the user process: ")
    process_time = int(input(f"Enter the processing time for {process_name} (in units): "))
    user_processes[process_name] = process_time

total_time = calculate_total_time(system_processes, user_processes)
print(f"The total time required to complete all processes is: {total_time} units")
