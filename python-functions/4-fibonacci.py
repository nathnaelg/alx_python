def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_nums = [0, 1]
        while len(fib_nums) < n:
            fib_nums.append(fib_nums[-1] + fib_nums[-2])
        return fib_nums