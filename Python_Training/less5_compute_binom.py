# объявление функции
def compute_binom(n, k):
    return int(compute_factorial(n) / compute_factorial(k) / compute_factorial(n - k))


# рекурсивный расчет факториала числа
def compute_factorial(n):
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))