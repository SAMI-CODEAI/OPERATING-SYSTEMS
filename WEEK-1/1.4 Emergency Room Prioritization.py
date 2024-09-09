# from queue import PriorityQueue
#
#
# def calculate_total_time(patients):
#     pq = PriorityQueue()
#     for patient in patients:
#         pq.put(patient)
#
#     current_time = 0
#     total_time = 0
#
#     while not pq.empty():
#         priority, treatment_time = pq.get()
#         current_time += treatment_time
#         total_time += current_time
#
#     return total_time
#
#
# # Taking user input
# patients = []
# num_patients = int(input("Enter the number of patients: "))
# for _ in range(num_patients):
#     priority = int(input("Enter the priority level of the patient: "))
#     treatment_time = int(input("Enter the treatment time for the patient (in minutes): "))
#     patients.append((priority, treatment_time))
#
# total_time = calculate_total_time(patients)
# print(f"The total time required to treat all patients is: {total_time} minutes")




import heapq

# Define the patients with their priority levels and treatment times
patients = [
    ('Patient A', 1, 10),  # (Patient Name, Priority Level, Treatment Time)
    ('Patient B', 2, 8),
    ('Patient C', 3, 15),
    ('Patient D', 4, 5)
]

def priority_scheduling(patients):
    # Create a priority queue using heapq. The heap is ordered by priority.
    # Higher priority level should come first, so we use -priority to invert the order.
    priority_queue = []
    for patient in patients:
        name, priority, treatment_time = patient
        heapq.heappush(priority_queue, (-priority, name, treatment_time))

    current_time = 0
    order_of_treatment = []

    while priority_queue:
        _, name, treatment_time = heapq.heappop(priority_queue)
        current_time += treatment_time
        order_of_treatment.append((name, treatment_time, current_time))

    return order_of_treatment, current_time

# Run the Priority Scheduling algorithm
treatment_order, total_time = priority_scheduling(patients)

# Print the results
print("Order of treatment and completion time:")
for patient in treatment_order:
    name, treatment_time, completion_time = patient
    print(f"{name}: Treatment Time = {treatment_time} minutes, Completion Time = {completion_time} minutes")

print(f"\nTotal time required to treat all patients: {total_time} minutes")
