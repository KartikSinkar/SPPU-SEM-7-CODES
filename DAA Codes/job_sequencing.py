# Job Sequencing with Deadlines using Greedy Method

# Structure to store job details
class Job:
    def __init__(self, job_id, profit, deadline):
        self.job_id = job_id
        self.profit = profit
        self.deadline = deadline


def job_sequencing(jobs):
    # Sort jobs in decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    n = max(job.deadline for job in jobs)
    slots = [-1] * (n + 1)  # Time slots
    total_profit = 0
    sequence = []

    # Schedule each job
    for job in jobs:
        for t in range(job.deadline, 0, -1):
            if slots[t] == -1:  # If slot available
                slots[t] = job.job_id
                total_profit += job.profit
                sequence.append(job.job_id)
                break

    print("\nSelected Jobs:", sequence)
    print("Total Profit:", total_profit)


# --- Main Program ---
jobs = []

num_jobs = int(input("Enter number of jobs: "))

for i in range(num_jobs):
    job_id = input(f"\nEnter Job ID for Job {i + 1}: ")
    profit = int(input("Enter Profit: "))
    deadline = int(input("Enter Deadline: "))
    jobs.append(Job(job_id, profit, deadline))

job_sequencing(jobs)
