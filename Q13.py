import threading
import time

# Step 1: Define the tasks
def print_numbers():
    for i in range(1, 6):
        print("Numbers:", i)
        time.sleep(1)

def print_letters():
    for ch in "ABCDE":
        print("Letters:", ch)
        time.sleep(1)

def print_squares():
    for i in range(1, 6):
        print("Square of", i, "is", i * i)
        time.sleep(1)

# Step 2: Create the threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t3 = threading.Thread(target=print_squares)

# Step 3: Start the threads
start = time.time()
t1.start()
t2.start()
t3.start()

# Step 4: Wait for all threads to finish
t1.join()
t2.join()
t3.join()

end = time.time()

print("\nAll tasks completed.")
print("Total time: {:.2f} seconds".format(end - start))