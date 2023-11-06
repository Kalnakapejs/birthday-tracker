cache = dict()

def fib(n: int) -> int:
  if n in cache:
    return cache[n]
  if n <= 1:
    return 0
  if n == 2:
    return 1
  cache[n] = fib(n-1)+fib(n-2)
  return cache[n]

for i in range(1,50):
  print(fib(i), end = " ")