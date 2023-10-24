def encriptar(texto):
    textoFinaL = ''
    for letra in texto:
        ascii = ord(letra) # valorAscii de letra
        ascii += 1  # suma 1
        textoFinaL += chr(ascii) # add letra a letra ascii movida una posicion
    return textoFinaL

def desencriptar(texto):
    print('El texto a desencriptar es: ' + texto)
    textoFinaL = ''
    for letra in texto:
        ascii = ord(letra) # valorAscii de letra
        ascii -= 1  # resta 1
        textoFinaL += chr(ascii) # add letra a letra ascii movida una posicion
    return textoFinaL

def encriptarArchivo(rutaArchivo):
    # archivo = open(rutaArchivo, 'r')
    archivo = open(rutaArchivo, 'a')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print('El archivo se ENCRIPTO correctamente')

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print('El archivo se DESENCRIPTO correctamente')
    

respuestaEoD = input('Presione "E" para encriptar, "D" para desencriptar >> ')
respuestaEoD = respuestaEoD.upper()
print(type(respuestaEoD))
rutaArchivo = input('Ingrese la ruta de archivo >> ')

if respuestaEoD == 'E':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)
