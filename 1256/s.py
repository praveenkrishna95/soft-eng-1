import math

def read_single_set(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        a, b, c = map(float, line.split())
    return a, b, c

def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None  # No real roots
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        sqrt_disc = math.sqrt(discriminant)
        root1 = (-b + sqrt_disc) / (2 * a)
        root2 = (-b - sqrt_disc) / (2 * a)
        return root1, root2

a, b, c = read_single_set('input.txt')
r1, r2 = solve_quadratic(a, b, c)

if r1 is None:
    print("No real roots")
else:
    print(f"Roots: {r1}, {r2}")