# объявление функции
def compute_binom(n, k):
    return int(compute_factorial(n) / compute_factorial(k) / compute_factorial(n - k))

# рекурсивный расчет факториала числа
def compute_factorial(n):
    if n == 1:
        return 1
    else:
        return compute_factorial(n - 1) * n


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))