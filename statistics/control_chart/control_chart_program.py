# Drawing a Shewhart Control Chart
# Coded by Shyam Sunder S.

# Import the required modules
import time
import random
import statistics
import matplotlib.pyplot as plt
from datetime import datetime

# Generate a random list of 50 numbers according to the Gaussian distribution with mean 50 and standard deviation 10
S = int(time.time())
random.seed(S)
some_list = []
for i in range(50): # Assume that this is time-series data generated over 50 time steps
    value = random.gauss(mu = 50, sigma = 10)
    round_value = round(value, 2)
    some_list.append(round_value)

# Calculate their mean and stdev
Mu = statistics.fmean(some_list)
Sigma = statistics.stdev(some_list)
(Mu, Sigma) = (round(Mu, 2), round(Sigma, 2))

# Now compute the control limits
ucl = Mu + 2 * Sigma # Upper control limit
lcl = Mu - 2 * Sigma # Lower control limit
ucl, lcl = round(ucl, 2), round(lcl, 2)

# Log the results
print("Logging results...")
some_str = ''
anomalies = 0
for i in range(len(some_list)):
    if (some_list[i] > ucl or some_list[i] < lcl):
        anomalies += 1
    some_str = some_str + f"{some_list[i]:.2f}"
    some_str = some_str + ' '
    if (i % 10 == 9):
        some_str = some_str + '\n'
with open("control_chart_log.txt", 'a') as fp:
    fp.write(f"Seed: {S}\n")
    fp.write(f"Time of testing: {datetime.now().strftime("%Y:%m:%d:%H:%M:%S")}\n\n")
    fp.write(f"Data:\n{some_str}\n")
    fp.write(f"Mean: {Mu}\n")
    fp.write(f"Standard deviation: {Sigma}\n")
    fp.write(f"Control limits: (Upper, Lower) = ({ucl}, {lcl})\n")
    fp.write(f"Number of anomalies: {anomalies}\n\n")
print("Finished logging results!")

# Plot the results
plt.plot(range(50), some_list, color = 'b', marker = 'o', linestyle = '-')
plt.axhline(y = Mu, color = 'k')
plt.axhline(y = ucl, color = 'r')
plt.axhline(y = lcl, color = 'r')
plt.xlabel('Observation Sequence')
plt.ylabel('Value')
plt.title('Shewhart Control Chart')
plt.savefig("control_chart.jpg", dpi = 300, bbox_inches = "tight")
plt.show()
