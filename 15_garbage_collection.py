# Demonstrate automatic and manual garbage collection using the gc module
import gc

class Demo:
    def __init__(self, name):
        self.name = name
        self.reference = None

print("Automatic garbage collection enabled:", gc.isenabled())
print("Objects tracked before experiment:", len(gc.get_objects()))

a = Demo("Object A")
b = Demo("Object B")
a.reference = b
b.reference = a

del a
del b

print("\nGarbage collection statistics before manual collection:")
print(gc.get_stats())

collected = gc.collect()

print("\nObjects collected by gc.collect():", collected)
print("Objects tracked after collection:", len(gc.get_objects()))

# Use gc.disable() to disable automatic collection.
# Use gc.enable() to enable it again.
