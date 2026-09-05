# Calculating Mean, Median and Standard Deviation
# Coded by Shyam Sunder S.

# Import modules
import time
import random
import statistics
from datetime import datetime

# Generate a random list of 100 numbers
S = int(time.time())
random.seed(S)
some_list = []
for i in range(100):
    some_list.append(random.randrange(10, 100))

# Calculate the basic statistics
m = statistics.mean(some_list)
M = statistics.median(some_list)
sd = statistics.stdev(some_list)

# Log the results
print("Logging results...")
some_str = ""
for i in range(100):
    some_str = some_str + str(some_list[i])
    some_str = some_str + ' '
    if (i % 10 == 9):
        some_str = some_str + '\n'
with open("basic_stats_log.txt", 'a') as fp:
    fp.write(f"Seed: {S}\n")
    fp.write(f"Time of testing: {datetime.now().strftime("%Y:%m:%d:%H:%M:%S")}\n\n") 
    fp.write(f"Data:\n{some_str}\n")
    fp.write(f"Mean: {m:.2f}\n")
    fp.write(f"Median: {M:.2f}\n")
    fp.write(f"Standard deviation: {sd:.2f}\n\n")
print("Finished logging results!")
