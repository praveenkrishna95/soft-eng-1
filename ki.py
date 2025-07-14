import math

a = 1
b = -5
c = 6

discriminant = b**2 - 4*a*c
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots: {root1}, {root2}")
else:
    print("No real roots")
