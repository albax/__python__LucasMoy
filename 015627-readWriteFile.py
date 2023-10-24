## abrir (crear) el archivo texto.txt, y añadio el texto con write
archivo = open('texto.txt', 'a')    
archivo.write('PRUEBA txt guardado en el archivo')
archivo.close()

## leer el archivo creado
archivo = open('texto.txt', 'r')
print (archivo.read())