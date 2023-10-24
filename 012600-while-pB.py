
## no pinta el 3 
## forma 1

# nroContador = 0
# while nroContador <= 5:
#     if nroContador != 3: ## distinto de 3
#         print ("nro: " + str(nroContador))
#     nroContador += 1
    

## no pinta el 3 
## forma 2

nroContador = 0
while nroContador <= 5:
    nroContador += 1
    if nroContador == 3: ## igual de 3
        continue 
    print("nro: " + str(nroContador))
    
