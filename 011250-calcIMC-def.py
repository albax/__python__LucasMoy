# INDICE DE MASA CORPORAL
# delgadez -- sobrepeso
# IMC - Peso / (altura x Altura)
# < 19: DELGADEZ
# entre 20 y 25: NORMAL
# entre 26 y 30: SOBREPESO
# > de 30: OBESIDAD

def calcularIMC(peso, alturaEnM):
    imc = peso / (alturaEnM * alturaEnM)
    print (" Su IMC es de: " + str(imc))
    return imc

def pideDatosIMC():
    peso = float(input("ingrese su peso (kg): "))
    alturaEnCm = float(input("Ingrese su altura (cm): "))
    alturaEnM = alturaEnCm / 100

    imc = calcularIMC(peso, alturaEnM)

    if imc < 20:  
        print("estas: DELGADO")
    if imc >= 20 and imc < 26 :
        print("estas: NORMAL")
    if imc >= 26 and imc < 30 :
        print("estas: SOBREPESO")
    if imc >= 30 : 
        print("estas: OBESO")


pideDatosIMC()
pideDatosIMC()