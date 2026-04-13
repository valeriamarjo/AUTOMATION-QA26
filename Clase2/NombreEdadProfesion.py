nombre = input('ingresa tu nombre: ')
edad = int(input('ingresa tu edad: '))
profesion = input('ingresa tu profesión: ')

print(f"hola {nombre} tenes {edad} años y trabajas como {profesion}")

if edad >= 18:
 print("Veni a trabajar en TalentoLab")
elif edad >= 16:
 print("Hacete unos mangos con esta pasantía")
else:
 print("Crecé y después vemos...bebe")