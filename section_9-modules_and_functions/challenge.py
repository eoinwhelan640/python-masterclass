## Write a small program to display informtion
# on the four clocks for functions we just lookjed at
# use get_clock_info() to see how to call it for each clock
import time

for clock in ['time','perf_counter','monotonic','process_time']:
    info = time.get_clock_info(clock)
    print(f"{clock+':':<15} {info}")
