def calcIMC(peso,alturaEnM):   
    imc = peso / (alturaEnM * alturaEnM)
    return imc

def pedirIMC():
    peso = float(input ("ingrese su peso: "))
    altura = int(input ("ingrese su altura (cm): "))
    alturaEnM = altura / 100
    # type(alturaEnM)
    imc = calcIMC(peso, alturaEnM)

    print ("Su IMC es de: " + str(imc))

    if imc < 20:  
        print("estas: DELGADO")
    if imc >= 20 and imc < 26 :
        print("estas: NORMAL")
    if imc >= 26 and imc < 30 :
        print("estas: SOBREPESO")
    if imc >= 30 : 
        print("estas: OBESO")

print(":::::: 1era persona")        
pedirIMC()

print(":::::: 2da persona")        
pedirIMC()

print(":::::: 3ra persona")        
pedirIMC()