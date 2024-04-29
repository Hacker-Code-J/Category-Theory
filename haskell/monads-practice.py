# Reference:
# https://nikgrozev.com/2013/12/10/monads-in-15-minutes/

import timeit
import matplotlib.pyplot as plt

def f1(x):
    return (x + 1, str(x) + "+1")

def f2(x):
    return (x + 2, str(x) + "+2")

def f3(x):
    return (x + 3, str(x) + "+3")

def unit(x):
    return (x, "Ops:")

def bind(t, f):
    res = f(t[0])
    return (res[0], t[1] + res[1] + ";")

# Direct calls setup
def direct_calls():
    x = 0
    log = "Ops:"
    res, log1 = f1(x)
    log += log1 + ";"
    res, log2 = f2(res)
    log += log2 + ";"
    res, log3 = f3(res)
    log += log3 + ";"
    return res, log

# Functional approach setup
def functional_approach():
    x = 0
    return bind(bind(bind(unit(x), f1), f2), f3)

# Number of iterations
num_runs = [100, 1000, 10000, 100000, 1000000, 10000000]

# Timing data storage
direct_times = []
functional_times = []

'''
This code will measure the execution time of each approach
by running each 'n' times and return the total time taken for all runs.
You can adjust the number of iterations
based on how precise you want the measurements to be or
based on your system's performance characteristics.
'''
# Measurement loop
for n in num_runs:
    direct_time = timeit.timeit(direct_calls, number=n) / n
    functional_time = timeit.timeit(functional_approach, number=n) / n
    direct_times.append(direct_time)
    functional_times.append(functional_time)

# Calculating speed differences
# speed_differences = [direct - functional for direct, functional in zip(direct_times, functional_times)]

# Plotting execution times
plt.figure(figsize=(10, 5))
plt.plot(num_runs, direct_times, label='Direct Calls', marker='o')
plt.plot(num_runs, functional_times, label='Functional Approach', marker='x')

# Adding text annotations for Direct Calls
for i, txt in enumerate(direct_times):
    plt.annotate(f'{txt:.1e}', (num_runs[i], direct_times[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Adding text annotations for Functional Approach
for i, txt in enumerate(functional_times):
    plt.annotate(f'{txt:.1e}', (num_runs[i], functional_times[i]), textcoords="offset points", xytext=(0,-15), ha='center')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of Runs')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Times Comparison')
plt.legend()
plt.grid(True)
plt.show()

# # Plotting speed difference
# plt.figure(figsize=(10, 5))
# plt.bar(range(len(num_runs)), speed_differences, tick_label=num_runs)
# plt.xlabel('Number of Runs')
# plt.ylabel('Speed Difference (seconds)')
# plt.title('Speed Difference Between Direct Calls and Functional Approach')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.show()