def fib(n: int) -> int:
    yield 0
    if n >= 2: yield 1
    a, b = 0, 1
    for i in range(n-2):
        a, b = b, a+b
    yield b
for x in fib(50):
    print(x)