class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

    def __repr__(self):
        return f"{self.job_id}: (Deadline: {self.deadline}, Profit: {self.profit})"


def job_sequencing(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = max(job.deadline for job in jobs)  
    slots = [False] * n 
    job_sequence = [None] * n

    total_profit = 0

    for job in jobs:
        for i in range(min(n, job.deadline) - 1, -1, -1):
            if not slots[i]:
                slots[i] = True
                job_sequence[i] = job.job_id
                total_profit += job.profit
                break

    result_sequence = [job_id for job_id in job_sequence if job_id]

    return result_sequence, total_profit


if __name__ == "__main__":
    jobs = [
        Job('J1', 2, 100),
        Job('J2', 1, 19),
        Job('J3', 2, 27),
        Job('J4', 1, 25),
        Job('J5', 3, 15)
    ]

    sequence, profit = job_sequencing(jobs)
    print(f"Selected job sequence: {sequence}")
    print(f"Total profit: {profit}")
