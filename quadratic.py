# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    raiz = b**2 - 4 * a * c
    if raiz == 0:
        return f"({-b / (2*a)})"
    elif raiz > 0:
        return f"({r1}, {r2})"
    else:
        return "( )"





def value_y(a, b, c, x):
    return a * x**2 + b * x + c


def to_string(a, b, c):
    if a != 0 and b != 0 and c != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a == 0 and c == 0:
        return f"f(x) = {b} * X"
    elif b == 0 and c == 0:
        return f"f(x) = {a} * X^2"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif c == 0:
        return f"f(x) = {a} * X^2 + {b} * X"


def derivation(a, b, c):
    if a != 0 and b != 0:
        return f"f'(x) = {2*a} * X + {b}"
    elif a == 0 and b == 0:
        return f"f'(x) = 0"
    elif a == 0:
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {2*a} * X"
