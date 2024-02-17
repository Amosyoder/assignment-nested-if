
# Task 1: Code Correction

import random

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0, 100)
disk_space = random.randint(0, 100)

# Task 3: Alert System: If any of the system parameters exceed these thresholds print an alert message
cpu_threshold = 90
memory_threshold = 90
disk_threshold = 10

if cpu_usage > cpu_threshold:
    print("High CPU usage! Value:", cpu_usage)
elif cpu_usage > 80:
    pass

# Task 2: Enhance the program to also monitor memory usage, and disk space
if memory_usage > memory_threshold:
    print("High Memory usage! Value:", memory_usage)
elif memory_usage > 80:
    pass
if disk_space < disk_threshold:
    print("Low Disk space! Value:", disk_space)
elif disk_space < 20:
    pass