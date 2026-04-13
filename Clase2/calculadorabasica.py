num1 = float(input("Elegí el primer número: "))
num2 = float(input("Ahora el segundo: "))
operacion = input("Qué operación (+, -, *, /): ")
if operacion == '+':
 resultado = num1 + num2
elif operacion == '-':
 resultado = num1 - num2
elif operacion == '*':
 resultado = num1 * num2
elif operacion == '/':
 resultado = num1 / num2
else:
 resultado = "Operación inválida"
print(f"El resultado es: {resultado:g}") 