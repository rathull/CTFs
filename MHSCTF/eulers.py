n = int(input())
for _ in range(n):
    # Take in input and initialize variables
    values = input().split(' ')
    step_size = float(values[0])
    x_target = float(values[1])
    x_current = 5
    y_current = 2
    # Size of each jump in x direction
    x_gap = abs(x_current - x_target)
    # Use this if we want to use Euler's method in reverse
    m = 1 if x_target > x_current else -1
    
    for i in range(int(round( x_gap / step_size ))):
        y_current += (x_current**2 - 6*y_current**2) * x_gap * m
        x_current += step_size
    
    print(round(y_current, 1))


