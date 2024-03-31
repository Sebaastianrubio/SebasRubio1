# Solicitar al usuario la cantidad de temperaturas a ingresar por Ciudad
n = int(input("Ingresa la cantidad de temperaturas que desea calcular de las Ciudades: "))

# Inicializar una lista para almacenar las temperaturas de las Ciudades
temperaturas = []
temperaturas1 = []
temperaturas2 = []

# Solicitar al usuario que ingrese las temperaturas de las Ciudades
print("UNIVERSSIDAD ESTATAL AMAZONICA")
for i in range(n):
    temperatura = float(input(f"Ingresa la temperatura Ciudad Quito: {i + 1}: "))
    temperaturas.append(temperatura)
for i in range(n):
    temperatura = float(input(f"Ingresa la temperatura Ciudad Riobamba:{i + 1}: "))
    temperaturas1.append(temperatura)
for i in range(n):
    temperatura = float(input(f"Ingresa la temperatura Ciudad Tena:{i + 1}: "))
    temperaturas2.append(temperatura)

# Calcular la media de las temperaturas
media = sum(temperaturas) / n
print(f"La media de la temperatura de la Ciudad de Quito es: {media}")
media1 = sum(temperaturas1) / n
print(f"La media de la temperatura de la Ciudad de Riobamba es:{media1}" )
media2 = sum(temperaturas2) / n
print(f"La media de la temperatura de la Ciudad de Tena es:{media2}" )