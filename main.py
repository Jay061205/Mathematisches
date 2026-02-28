import turtle
import math

def generate_commands(limit: int) -> list[str]:
    commands = []
    for n in range(limit):
        ones = bin(n).count("1")
        command = "F" if ones % 2 == 0 else "T"
        commands.append(command)
    return commands

def compute_bounds(commands):
    x, y, angle = 0, 0, 0
    xs, ys = [0], [0]
    for cmd in commands:
        if cmd == "F":
            x += math.cos(math.radians(angle))
            y += math.sin(math.radians(angle))
            xs.append(x)
            ys.append(y)
        elif cmd == "T":
            angle += 60
    return min(xs), max(xs), min(ys), max(ys)

def get_primes(limit: int) -> list[int]:
    primes = []
    for n in range(2, limit):
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break 
        if is_prime:
            primes.append(n)
    return primes

def get_fibonacci(limit: int) -> list[int]:
    fibs = []
    a, b = 0, 1
    while a < limit:
        fibs.append(a) 
        a, b = a + b, a
    return fibs

def get_evens(limit: int) -> list[int]:
    return [n for n in range(0, limit, 2)]

def get_odds(limit: int) -> list[int]:
    return [n for n in range(1, limit, 2)]

def get_binary_palindromes(limit: int) -> list[int]:
    palindromes = []
    for n in range(limit):
        b = bin(n)[2:]  # strip the '0b' prefix
        if b == b[::-1]: # check if b is a palindrome
            palindromes.append(n)
    return palindromes

def draw(commands):
    width_margin = 1100
    height_margin = 700

    min_x, max_x, min_y, max_y = compute_bounds(commands)  # step=1 always
    bounds_w = max(max_x - min_x, 0.0001)
    bounds_h = max(max_y - min_y, 0.0001)

    step = min(width_margin / bounds_w, height_margin / bounds_h)  # now step is defined

    start_x = -(min_x + max_x) / 2 * step
    start_y = -(min_y + max_y) / 2 * step

    turtle.setup(width=1200, height=800)
    turtle.bgcolor("black")

    t = turtle.Turtle()
    t.color("white")
    t.speed(0)
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(0)
    t.pendown()

    for cmd in commands:
        if cmd == "F":
            t.forward(step)
        elif cmd == "T":
            t.left(60)

    turtle.done()
def generate_commands_from_sequence(numbers: list[int]) -> list[str]:
    commands = []
    for n in numbers:
        ones = bin(n).count("1")
        command = "F" if ones % 2 == 0 else "T"
        commands.append(command)
    return commands

pri = get_primes(4096)
fib = get_fibonacci(10**18)
even = get_evens(1000)
odds = get_odds(4096)
pali = get_binary_palindromes(10**6)
cmds = generate_commands_from_sequence(pali)
draw(cmds)
