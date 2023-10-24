diccionario = {
    "Programar": "Programar es transformar el cafe en codigo",
    "POO": "Programacion Orientada a Objetos",
    "MVC": "Modelo Vista Controlador"
}

print(diccionario["POO"])

diccionario_nros = {
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "Cinco",
    "6": "Seis",
    "7": "Siete",
    "8": "Ocho",
    "9": "Nueve",
}

txt = input('Ingrese un NRO: ')

juntaTxt = ''

for i in txt: ## recorre el txt del input
    juntaTxt += diccionario_nros[i] + ' ' ## los junta
print(juntaTxt)