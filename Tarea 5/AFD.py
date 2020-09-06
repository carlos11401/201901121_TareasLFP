import re
cadena1 = "__servidor1"
cadena2 = "3servidor"

def automata(entrada):
    estado = 0
    contadorGuion = 0
    contadorNum = 0
    good = True
    i = 0
    for i in range(len(entrada)):
        if estado == 0:
            if entrada[i]=="_":
                contadorGuion = contadorGuion + 1           #contar guiones para saber por que estado ir 
            else:
                if contadorGuion == 1:                  
                    estado = 1                 #el primer camino
                else:
                    estado = 3               #el otro camino
                    i = i-1
        elif estado == 1:

            if entrada[i].isalpha() == True:       #si no es letra que entre en la condicion
                estado = 1

            elif entrada[i].isdigit():            #si es numero es por que la cadena es valida
                    estado = 2
                    contadorNum = contadorNum + 1

                    if contadorNum == 1: good = True      #si contador de numeros es igual a 1 es por que la palabra cumple sino No
                    else: good = False    

            else: good = False

        elif estado == 2:   #aqui llegan los caracteres que se pasen despues del estado final
            good = False
 
        elif estado == 3:
            if entrada[i].isalpha:
                estado = 4
            else:
                good = False

        elif estado == 4:
            if entrada[i].isdigit: 
                good = True
                estado = 2
            else: good = False

    if good:  print("Cadena Valida")
    elif good == False:
        print("Error")


print("Cadena 1 :")
automata(cadena1)
print("Cadena 2 :")
automata(cadena2)
print("Otra Cadena:")
automata("_holamundo5")
