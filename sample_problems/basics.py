########### Basics Warmup #1 ###########
# Warmup #1
x = 7
y = 5.0
z = 10.0
w = x % 2 + y / z + z + y / (z + z)
print("Warmup #1")
print(w)
print()

# Warmup #2
c = True
d = False
c = c and d
c = not c or d

# Warmup #3
d = 0
for p in range(0, 5):
    if p % 4 == 0:
        d = d + (p-1) * 25;
    else:
        d = d + 100;
print("Warmup #2")
print("$" + str(d//100) + "." + str(d % 100))
print()

