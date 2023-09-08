"""implement multiprocessing"""
from multiprocessing import Queue, Process, current_process, Pool, cpu_count
import time

# Function to process a job


def job(job_data):
    # Simulate some processing time
    print(f"Job {job_data} is processing in {current_process().name}\n")
    time.sleep(2)
    print(f"Job {job_data} is completed by {current_process().name}\n")


def worker_process(mpQueue):
    while True:
        job_data = mpQueue.get()  # Wait for a job to be available
        if job_data == "end":
            # Exit the process if None is received (a signal to terminate)
            break
        job(job_data)


if __name__ == "__main__":
    print('number of cpu:', cpu_count())
    number_of_processes = int(input("Enter number of processes "))
    processing_time_start = time.perf_counter()
    pool = Pool(processes=number_of_processes)
    mpQueue = Queue()

    processes = []

    for i in range(number_of_processes):
        processes.append(Process(target=worker_process, args=[mpQueue]))

    for process in processes:
        process.start()
    
    jobs = ["Data 1", "Data 2", "Data 3", "Data 4", "Data 5"]
    for job_data in jobs:
        mpQueue.put(job_data)

    for i in range(number_of_processes):
        mpQueue.put("end")

    for process in processes:
        process.join()

    pool.close()
    pool.join()
    print(f"Processing time with {number_of_processes} processes: {time.perf_counter() - processing_time_start}")
