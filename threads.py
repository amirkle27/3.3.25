import threading


def enter_numbers(first_num, last_num):
    numbers = [num for num in range(first_num, last_num+1)]
    return numbers

def print_forwards(numbers):
    print("\nThread 1 - Printing forwards:")
    for num in numbers:
        print(num)

def print_backwards(numbers):
    print("\nThread 2 - Printing backwards:")
    for num in numbers[::-1]:
        print(num)


numbers = enter_numbers(1, 100)

thread1 = threading.Thread(target=print_forwards, args=(numbers,))
thread2 = threading.Thread(target=print_backwards, args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
