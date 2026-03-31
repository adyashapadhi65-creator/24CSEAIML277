#generate fibonacci between 0 to 100,then find the sum of even valued terms in python
def solve_fibonacci_even_sum(limit):
    a, b = 0, 1
    even_sum = 0
    sequence = []

    while a <= limit:
        sequence.append(a)
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b

    print(f"Fibonacci sequence up to {limit}: {sequence}")
    print(f"Sum of even-valued terms: {even_sum}")

solve_fibonacci_even_sum(100)
