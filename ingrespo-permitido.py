# Paso 1: Solicitar al usuario que ingrese la edad del cliente

edad = int(input("¿Cuántos años tiene el cliente? "))

# Paso 2: Verificar si el cliente cumple o no con la edad permitida para ingresar a la discoteca 

permitido = True if edad >= 18 else False #ternario

# Paso 3: Comunicar usuario si el cliente puede o no ingresar a la discoteca

if permitido:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho :(, no pueden ingresar a la discoteca los menores de edad")
