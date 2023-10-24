def mostrarPrecioFinal(producto,precio,descuento):
    precioFinal = precio - descuento * precio / 100
    print("El precio del " + producto + "es: $" + str(precioFinal))

mostrarPrecioFinal("Audifono", 1400, 20)
mostrarPrecioFinal("parlante Boss", 640, 12)