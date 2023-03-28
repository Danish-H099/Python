import time
seconds = time.time()
print("Time in seconds since the epoch:", seconds)
local_time = time.ctime(seconds)
print("Local time:", local_time)
print("This is the start of the program.")
time.sleep(5)
print("This prints five seconds later.")