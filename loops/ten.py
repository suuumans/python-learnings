
# Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries,
# starting from 1 second, but stops after 5 retries.

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "with a wait time of", wait_time, "seconds.")
    # time.sleep() is a function that pauses the execution of the program for a specified number of seconds
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2

print("Maximum number of retries reached. Exiting.")