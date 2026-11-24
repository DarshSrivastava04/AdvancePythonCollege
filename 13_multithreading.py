# Create multiple threads to perform tasks concurrently
import threading
import time

def task(name, delay):
    print(f"{name} started")
    time.sleep(delay)
    print(f"{name} completed")

threads = [
    threading.Thread(target=task, args=("Task 1", 2)),
    threading.Thread(target=task, args=("Task 2", 3)),
    threading.Thread(target=task, args=("Task 3", 1))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All tasks completed.")
