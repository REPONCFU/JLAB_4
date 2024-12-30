# Ввод двух чисел
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Вычисления
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

# Проверка деления на ноль
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (division by zero)"

# Вывод результатов
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Division: {division}")
