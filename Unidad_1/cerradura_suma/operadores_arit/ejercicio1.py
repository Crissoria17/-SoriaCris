printf("Cadena")
#Primer Paso, Saludo Simple
print("Bienvenido al curso Lenguajes Formales y Automatas")
print("+++ +  +++")
print()

#Segundo Paso, Simular la solicitud del nombre al usuario.
nombre="Ale"
print("Bienvenido "+nombre+", te saluda BDS")
print()

#Tercer Paso, conjunto de saludos.

nombre="Oso Polar"
saludos=[
    "Bienvenido "+nombre+", te saluda BDS",
    "Hola "+nombre+", en que puedo servir?",
    "Es un placer tenerte nuevamete "+nombre
]
print(saludos[0])

print("El siguiente programa realiza la suma,resta y multiplicacion de dos numeros")
print("")
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

suma = num1 + num2
resta= num1 - num2
multiplicacion = num1 * num2
div = num1 / num2

print("La suma es: ",suma)
print("")
print("La resta es: ",resta)
print("")
print("La multiplicacion es: ",multiplicacion)
print("")
print("La division es: ",div)