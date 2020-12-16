# Initialize x
x=1.0
print("x*x", x*x)

# first iteration
delta = (1/x)-x/2
x = x+delta
print("x*x", x*x)

# second iteration
delta = (1/x)-x/2
x = x+delta
print("x*x", x*x)

# add a third iteration to determine the new delta
delta = (1/x)-x/2
x = x+delta
print("x*x", x*x)


