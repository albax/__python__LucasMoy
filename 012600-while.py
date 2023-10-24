contador = 1
while contador <=5:
    contador += 1
    # formas para que saltee 3
    # if contador != 3:
    if contador == 3:
        continue        
    print("El valor de contador es: " + str(contador))