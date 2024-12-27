import random
numero_secreto= random.randint(1,10)
cant_intentos=0
cant_deintentos_max=5
adivinado= False# empieza siendo negativo
print("Adivinanzas :c")
while not adivinado and cant_intentos < cant_deintentos_max:

    entrada= input("introducir un numero del 1 al 9: ")
    numero=int(entrada)
    if numero== numero_secreto:
        print("Felicitaciones ganaste")
        adivinado= True
    elif numero <numero_secreto:
        print("el numero ingresado es mayor")
    else:
        print("el numero es menor al ingresado")
    cant_intentos +=1
if not cant_intentos < cant_deintentos_max:
    print("perdiste el juego en 5 intentos")