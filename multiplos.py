"""
Múltiplos
"""

# Entradas
numero1 = int(input("Introduzca un número: "))
numero2 = int(input("Introduzca otro número: "))

# Proceso
if numero1 == numero2 == 0:
    resultado = "El número 0 es múltiplo del 0"
elif numero2 != 0 and numero1 % numero2 == 0:
    resultado = f"El número {numero1} es múltiplo del {numero2}"
elif numero1 != 0 and numero2 % numero1 == 0:
    resultado = f"El número {numero2} es múltiplo del {numero1}"
else:
    resultado = "Ninguno de los números es múltiplo del otro"

# Salidas
print(resultado)
