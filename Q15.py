import gc
import sys
import time

# Step 1: Create a class and check reference counting
class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None

a = Node("A")
print("Reference count of a:", sys.getrefcount(a) - 1)
b = a
print("Reference count after b = a:", sys.getrefcount(a) - 1)
del b

# Step 2: Create circular references
def create_cycles(n):
    for i in range(n):
        x = Node("x")
        y = Node("y")
        x.ref = y
        y.ref = x   # circular reference

# Step 3: Check GC settings
print("\nGC enabled:", gc.isenabled())
print("GC thresholds:", gc.get_threshold())
print("GC counts:", gc.get_count())

# Step 4: Experiment 1 - with automatic GC
gc.collect()
start = time.time()
create_cycles(100000)
auto_time = time.time() - start
print("\nAutomatic GC time: {:.4f} seconds".format(auto_time))

# Step 5: Experiment 2 - with GC disabled
gc.disable()
gc.collect()
start = time.time()
create_cycles(100000)
disabled_time = time.time() - start
print("GC disabled time: {:.4f} seconds".format(disabled_time))

# Step 6: Manual collection
print("Objects tracked before collect:", len(gc.get_objects()))
start = time.time()
collected = gc.collect()
manual_time = time.time() - start
print("Unreachable objects collected:", collected)
print("Manual collect time: {:.4f} seconds".format(manual_time))
print("Objects tracked after collect:", len(gc.get_objects()))

# Step 7: Re-enable GC and show statistics
gc.enable()
print("\nGC statistics:")
for i, stat in enumerate(gc.get_stats()):
    print("Generation", i, ":", stat)