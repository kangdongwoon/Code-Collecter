def fib(n, lookup):
    if n<=1:
        return n
    if lookup[n] is None:
        lookup[n] =fib(n-2, lookup) + fib(n-1, lookup)
    return lookup[n]

n=10
lookup = [None] *  (n+1)
print ("Fibonacci Value(", n, ") : " , fib(n,lookup))
