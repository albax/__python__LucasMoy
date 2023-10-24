arreglo_frutas = ['banana', 'manzana', 'pera', 'mango']
# i = len(arreglo_frutas)
# print(i)

## metodos
arreglo_frutas.reverse()    ## reverse la lista
arreglo_frutas.remove("mango") ## elimina mango
arreglo_frutas.append("kiwi")   ## add kiwi

######  funciona ######
# for fruta in arreglo_frutas[::-1]: ## voltea la lectura
#     print("fruta es: " + fruta)

######  funciona ######
# for index, fruta in enumerate(arreglo_frutas[::-1]): 
#     # print(index, fruta)
#     print(f"fruta #{index} es: " + fruta)
# ### fruta #1 es: mango

######  funciona ######
# for fruta in arreglo_frutas:
#     ## selecionar solo las que terminan en una "o"
#     if fruta.endswith('a'):
#         print("La fruta es: " + fruta)

print("Lista actual es: " + str(arreglo_frutas))

fruta1 = arreglo_frutas[2]
for fruta in fruta1:
    print("Letra: " + fruta)