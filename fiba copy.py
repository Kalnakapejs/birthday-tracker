from functools import lru_cache
@lru_cache(maxsize = None)
def fib(n: int) -> int:
  if n <= 1:
    return 0
  if n == 2:
    return 1
  return fib(n-1)+fib(n-2)

for i in range(1,50):
  print(fib(i), end = " ")