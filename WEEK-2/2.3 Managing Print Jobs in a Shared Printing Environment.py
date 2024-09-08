from queue import Queue


def calculate_total_time(high_priority_jobs, low_priority_jobs):
    system_queue = Queue()
    user_queue = Queue()

    for job, time in high_priority_jobs.items():
        system_queue.put(time)

    for job, time in low_priority_jobs.items():
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
high_priority_jobs = {}
low_priority_jobs = {}

num_high_priority_jobs = int(input("Enter the number of high priority (system) print jobs: "))
for _ in range(num_high_priority_jobs):
    job_name = input("Enter the name of the high priority job: ")
    job_time = int(input(f"Enter the printing time for {job_name} (in units): "))
    high_priority_jobs[job_name] = job_time

num_low_priority_jobs = int(input("Enter the number of low priority (user) print jobs: "))
for _ in range(num_low_priority_jobs):
    job_name = input("Enter the name of the low priority job: ")
    job_time = int(input(f"Enter the printing time for {job_name} (in units): "))
    low_priority_jobs[job_name] = job_time

total_time = calculate_total_time(high_priority_jobs, low_priority_jobs)
print(f"The total time required to complete all print jobs is: {total_time} units")
