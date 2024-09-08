from queue import Queue


def calculate_total_time(high_priority_jobs, medium_priority_jobs, low_priority_jobs):
    high_priority_queue = Queue()
    medium_priority_queue = Queue()
    low_priority_queue = Queue()

    for job, time in high_priority_jobs.items():
        high_priority_queue.put(time)

    for job, time in medium_priority_jobs.items():
        medium_priority_queue.put(time)

    for job, time in low_priority_jobs.items():
        low_priority_queue.put(time)

    current_time = 0
    total_time = 0

    while not high_priority_queue.empty():
        time = high_priority_queue.get()
        current_time += time
        total_time += current_time

    while not medium_priority_queue.empty():
        time = medium_priority_queue.get()
        current_time += time
        total_time += current_time

    while not low_priority_queue.empty():
        time = low_priority_queue.get()
        current_time += time
        total_time += current_time

    return total_time


# Taking user input
high_priority_jobs = {}
medium_priority_jobs = {}
low_priority_jobs = {}

num_high_priority_jobs = int(input("Enter the number of high priority (critical) jobs: "))
for _ in range(num_high_priority_jobs):
    job_name = input("Enter the name of the high priority job: ")
    job_time = int(input(f"Enter the processing time for {job_name} (in units): "))
    high_priority_jobs[job_name] = job_time

num_medium_priority_jobs = int(input("Enter the number of medium priority (standard) jobs: "))
for _ in range(num_medium_priority_jobs):
    job_name = input("Enter the name of the medium priority job: ")
    job_time = int(input(f"Enter the processing time for {job_name} (in units): "))
    medium_priority_jobs[job_name] = job_time

num_low_priority_jobs = int(input("Enter the number of low priority (background) jobs: "))
for _ in range(num_low_priority_jobs):
    job_name = input("Enter the name of the low priority job: ")
    job_time = int(input(f"Enter the processing time for {job_name} (in units): "))
    low_priority_jobs[job_name] = job_time

total_time = calculate_total_time(high_priority_jobs, medium_priority_jobs, low_priority_jobs)
print(f"The total time required to complete all jobs is: {total_time} units")
