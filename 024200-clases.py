class Cuadrado:
    def __init__(self, anchoo, altoo): ## CONSTRUCTOR
        self.ancho = anchoo
        self.alto = altoo
    
    def calcularArea(self): ## metodo
        area = self.ancho * self.alto
        return area

## instanciando el objeto "cuadrado"
figura = Cuadrado(10, 142)
print(figura.alto)

## objeto figura puede usar el metodo .calcularArea()
figura.calcularArea()