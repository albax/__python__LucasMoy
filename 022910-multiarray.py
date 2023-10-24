lat = 34.5
lon = 45.6
posicion = [lat, lon]

historial = [
    [34.5, 42.6, "2022/02/02 17:20:24"],
    [36.3, 48.9, "2022/02/02 17:20:34"],
    [32.1, 46.8, "2022/02/02 17:20:44"],
    [37.2, 43.2, "2022/02/02 17:20:54"],
    [31.6, 41.5, "2022/02/02 17:21:04"],
    [33.5, 42.4, "2022/02/02 17:21:14"],
    [34.2, 43.6, "2022/02/02 17:21:24"]
]

print(historial[0])  #[34.5, 45.6, '2022/02/02 17:20:24'] #trae lista
print(historial[0][1])  #45.6

## por bprac
indiceLongitud = 0
indiceLatitud = 1
indiceFecha = 2

print(id(historial)) # 2715631733248 --id [lista] mutable

print(historial[2][indiceLongitud]) # 32.1

for coordenada in historial:
    print(coordenada[indiceLongitud], coordenada[indiceLatitud])