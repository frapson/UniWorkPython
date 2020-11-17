number = 11110000110
suma = 0
while number > 0:
    suma += number % 10
    number = number // 10
print(suma)