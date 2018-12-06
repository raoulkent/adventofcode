from collections import defaultdict as dd

# Data input
lines = open('input', 'r')

# --- Part One ---
fabric = dd(int)

for line in lines:
    _, _, coords, size = line.strip().split()
    x, y = map(int, coords[:-1].split(','))
    x_size, y_size = map(int, size.split('x'))
    for x_curr in range(x, x + x_size):
        for y_curr in range(y, y + y_size):
            fabric[(x_curr, y_curr)] += 1
output = len([x for x in fabric.values() if x > 1])
print(output)


