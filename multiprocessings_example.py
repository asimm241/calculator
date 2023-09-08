"""implement multiprocessing"""
import multiprocessing as mp
import time

# Function to process a job


def job(job_data, current_process):
    # Simulate some processing time
    print(f"Job {job_data} is processing... in {current_process.name}\n")
    time.sleep(2)
    print(f"Job {job_data} is completed by {current_process.name}\n")


def worker_process(mpQueue):
    while True:
        job_data = mpQueue.get()  # Wait for a job to be available
        if job_data == "end":
            # Exit the process if None is received (a signal to terminate)
            break
        job(job_data, mp.current_process())


if __name__ == "__main__":
    print('number of cpu:', mp.cpu_count())
    pool = mp.Pool(processes=2)
    mpQueue = mp.Queue()
    # print("hello")
    # worker_process()

    process_1 = mp.Process(target=worker_process, args=[mpQueue])
    process_2 = mp.Process(target=worker_process, args=[mpQueue])

    process_1.start()
    process_2.start()

    # Push jobs to the worker processes
    jobs = [1, 2, 3, 4, 5]
    for job_data in jobs:
        mpQueue.put(job_data)

    # Signal the worker processes to terminate
    mpQueue.put("end")
    mpQueue.put("end")

    process_1.join()
    process_2.join()

    pool.close()
    pool.join()
