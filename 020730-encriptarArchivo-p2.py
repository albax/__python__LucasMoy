######## pRev #################################################################

def encriptar(texto):
    # print('\n' + 'El texto a encriptar es: ' + texto )    
    textoFinal = ''
    for letra in texto:
        textoFinal += letra + 'x'
    return textoFinal

def desencriptar(texto):
    print('\n' + 'El texto a desencriptar es: ' + texto )
    textoFinal = ''
    contador = 0    
    for letra in texto:
        if contador % 2 == 0: # uno si o otro x no
            textoFinal += letra
        contador +=1    
    return textoFinal
    # print(type(textoFinal))
        

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)
    
    archivo.open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print("El archivo se ENCRIPTO correctamente")

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r') 
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)
    
    archivo.open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print("El archivo se DESENCRIPTO correctamente")

respuestaEoD = input('Presione "E" para encriptar, "D" para desencriptar >> ')
rutaArchivo = input('Ingrese la ruta de archivo >> ')

if respuestaEoD == 'E':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)