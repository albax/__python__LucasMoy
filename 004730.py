nombre = input('¿Como te llamas? ')
print('Hola  '+nombre)

edad = int(input('¿Ctos años tienes? '))

masDe12 = edad >= 15
respHijoDelDueno = input('¿Eres hijo del dueño? ')
esHijoDelDueno = respHijoDelDueno =='si'
puedePasar = masDe12 or esHijoDelDueno

if puedePasar:
    print('Puedes pasar')
else:
    print('NO puedes pasar porque "Eres menor de edad"')