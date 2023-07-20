nombre_love = input("Cuál es tu nombre amo?: ")
nombre = input("Hola humana, cuál es tu nombre? ")
print(" ")
print("Hola", nombre, ", yo soy la IA de", nombre_love)
print("Te puedo hacer una pregunta?")

respuesta = int(input("Presiona 1 para CONFIRMAR o presiona 2 para RECHAZAR :( : "))
print(" ")
print(" ")
if respuesta == 1:
    print(nombre_love, "Te quiere preguntar lo siguiente: ")
    print("Él está enamorado de ti, y quiere saber si quieres ser su  novia? ")
    aceptacion = int(input("Presiona 1 para CONFIRMAR o presiona 2 para RECHAZAR :(: "))
    print(" ")
    print(" ")
    if aceptacion == 1:
        print("FELICIDADES, hacen una hermosa pareja, ahora también soy tu IA ", nombre)
    elif aceptacion == 2:
        print("Hiciste trizas el corazón de mi humano ", nombre)
        print("No sabes de lo que te pierdes ")
elif respuesta == 2:
    print("Bueno, esta ocasión ya no volverá a ocurrir jamas. \n Adiós humana.")
else:
    print("No hagas renegar a una IA, esto es en serio")
    

    

