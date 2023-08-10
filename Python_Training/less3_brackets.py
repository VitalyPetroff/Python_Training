# объявление функции
def is_correct_bracket(text):
    total = 0
    for ch in text:
        if ch == '(':
            total += 1
        elif ch == ')':
            total -= 1
            if total < 0:
                return False
    if total == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))