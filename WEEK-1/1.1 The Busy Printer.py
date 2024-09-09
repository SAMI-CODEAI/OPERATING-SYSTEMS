# def calculate_total_time(arrival_times, pages):
#     current_time = 0
#     total_time = 0
#
#     for i in range(len(arrival_times)):
#         if current_time < arrival_times[i]:
#             current_time = arrival_times[i]
#         current_time += pages[i]
#         total_time = current_time
#
#     return total_time
#
# # Taking user input
# arrival_times = list(map(int, input("Enter the arrival times (space-separated): ").split()))
# pages = list(map(int, input("Enter the number of pages for each job (space-separated): ").split()))
#
# total_time = calculate_total_time(arrival_times, pages)
#
# print(f"The total time taken to complete all printing tasks is: {total_time} seconds")
from tkinter.font import names
from turtledemo.penrose import start


class PrintJob:
    def __init__(self, name, arrival_time, pages):
        self.name = name
        self.arrival_time = arrival_time
        self.pages = pages

def simulate_fcs(jobs):
    jobs.sort(key=lambda job: job.arrival_time)
    current_time = 0
    completion_times = []
    for job in jobs:
        if current_time < job.arrival_time:
            current_time = job.arrival_time
        start_time = current_time
        end_time = current_time + job.pages
        completion_times.append((job.name, start_time, end_time))
        current_time = end_time
    return completion_times

def main():
    jobs = [PrintJob('A', 0, 10), PrintJob('B', 10, 15), PrintJob('C', 3, 3), PrintJob('D', 5, 7)]
    completion_times = simulate_fcs(jobs)
    print("Job completion times:")
    for job_name, start_time, end_time in completion_times:
        print(f"Job {job_name}: start time: {start_time} s, end time: {end_time} s")
    total_time = completion_times[-1][2]
    print(f"Total time: {total_time} s")

if __name__ == "__main__":
    main()
