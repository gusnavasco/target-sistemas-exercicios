nums = list(range(10)) # Lista de numeros para teste


def num_in_fib(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a+b
    if a == num:
        print(f"O numero {num} pertence a sequencia de Fibonacci")
    else:
        print(f"O numero {num} nao pertence a sequencia de Fibonacci")


for num in nums:
    num_in_fib(num)
