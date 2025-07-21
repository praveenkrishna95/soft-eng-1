def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        return f'Real roots: x1 = {x1}, x2 = {x2}'
    elif d == 0:
        x = -b / (2*a)
        return f'Double root: x = {x}'
    else:
        real = -b / (2*a)
        imag = (-d)**0.5 / (2*a)
        return f'Complex roots: x1 = {real}+{imag}i, x2 = {real}-{imag}i'

with open('multiinput.txt') as f:
    for line in f:
        a, b, c = map(float, line.strip().split())
        result = solve_quadratic(a, b, c)
        print(result)
