# объявление функции
def is_valid_password(password):
    lst = password.split(':')
    if len(lst) == 3:
        if is_pailndrom(int(lst[0])) and is_prime_number(int(lst[1])) and is_even(int(lst[2])):
            return True
        else:
            return False
    else:
        return False


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_prime_number(num):
    if num == 1:
        return True
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    return True


def is_pailndrom(num):
    if 0 < num < 10:
        return True
    else:
        lst = list()
        while num > 0:
            lst.append(num % 10)
            num //= 10
        for i in range(int(len(lst) / 2)):
            if lst[i] != lst[-1 - i]:
                return False
        return True


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
