def fibonacci_recursive(n):
    if n == 1:
        return 0
    if n == 2 :
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci(n):
    fib = []
    fib.append(0)
    fib.append(1)
    while len(fib) != n :
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


if __name__=="__main__":
    result = fibonacci(12)
    print(result)
