def encriptar(texto):
    print('\n' + 'El texto a encriptar es: ' + texto )
    
    textoFinal = ''

    for letra in texto:
        textoFinal += letra + 'x'
    print("texto encriptado es: " +textoFinal)



def desencriptar(textoFinal):
    print('\n' + 'El texto a desencriptar es: ' + textoFinal )
    
    textoFinalOK = ''
    contador = 0
    
    for letra in textoFinal:
        if contador % 2 == 0: # uno si o otro x no
            textoFinalOK += letra
        contador +=1
    
    print("texto desincriptado es: " + textoFinalOK)
    print(type(textoFinal))
    

encriptar('Todo Rusia ataca Ucrania')
desencriptar('Txoxdxox xRxuxsxixax xaxtxaxcxax xUxcxrxaxnxixax')