import calculator

a = 5
b = 2

addition_result = calculator.add(a, b)
subtract_result  = calculator.subtract(a, b)
multiply_result = calculator.multiply(a, b)
divide_result = calculator.divide(a, b)

print(f"{a} + {b} = {addition_result}")
print(f"{a} - {b} = {subtract_result}")
print(f"{a} * {b} = {multiply_result}")
print(f"{a} / {b} = {divide_result}")
