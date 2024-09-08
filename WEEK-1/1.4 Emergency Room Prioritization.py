from queue import PriorityQueue


def calculate_total_time(patients):
    pq = PriorityQueue()
    for patient in patients:
        pq.put(patient)

    current_time = 0
    total_time = 0

    while not pq.empty():
        priority, treatment_time = pq.get()
        current_time += treatment_time
        total_time += current_time

    return total_time


# Taking user input
patients = []
num_patients = int(input("Enter the number of patients: "))
for _ in range(num_patients):
    priority = int(input("Enter the priority level of the patient: "))
    treatment_time = int(input("Enter the treatment time for the patient (in minutes): "))
    patients.append((priority, treatment_time))

total_time = calculate_total_time(patients)
print(f"The total time required to treat all patients is: {total_time} minutes")
