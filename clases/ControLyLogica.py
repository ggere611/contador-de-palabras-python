#que es un operador?
#simbolos especiales, q realizan una operacion especficia
#TIPO
#Aritmeticos
#>>>operaciones matematicas(tener cuidado con la division, en un float y un entero
#con // se puede sacar el entero floor division)
#resto o modulo
#** exponenciacion
#operador += suma de pasos tambien -= , *=, /=.´
# try except finally

a= 11
b=2
resultado=0
try:
    resultado=a/b
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    resultado=0
print(resultado)

#c= a//b
#a *= b
#a *= b