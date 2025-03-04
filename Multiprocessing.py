
import multiprocessing
import time


def print_forwards(name, return_dict):
    print(f"\n{name} - Printing forwards:")
    count = 0
    for num in range (1,101):
        print(num)
        count += 1
    return_dict[name] = count

def print_backwards(name, return_dict):
    print(f"\n{name} - Printing backwards:")
    count = 0
    for num in range (100,0,-1):
        print(num)
        count += 1
    return_dict[name] = count

def multi_process_count():
    start_time = time.time()

    manager = multiprocessing.Manager()
    return_dict = manager.dict()


    process1 = multiprocessing.Process(
        target=print_forwards,
        args=("Process 1", return_dict))

    process2 = multiprocessing.Process(
        target=print_backwards,
        args=("Process 2", return_dict))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Two processes time: {elapsed:.4f} seconds")

    total_count = sum(return_dict.values())
    print(f"Total count from multiprocessing: {total_count}")

    print(return_dict)

    return f"Two processes finished after {elapsed} seconds"


if __name__ =="__main__":
    print(multi_process_count())
