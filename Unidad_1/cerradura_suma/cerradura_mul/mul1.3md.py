print("Cerradura: La multiplicacion de dos numeros reales siempre da como resultado un numero real ")
print("A + B pertenece R  ")
print(" ")
print("El siguiente programa realiza la propiedad de cerradura")
print(" ")

#solicita los numeros
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

#Calcula la multiplicacion de los numeros
multiplicacion = num1 * num2

if multiplicacion.is_integer():
    resultado = "entero"
else:
    resultado = "racional"
print()
print("El resultado de la multiplicacion es:",multiplicacion)
print("El resultado es un numero:",resultado)