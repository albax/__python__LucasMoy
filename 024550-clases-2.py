class Persona:
    def __init__(self, nombre, apellido, dni, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono

class Empleado(Persona):
    def __init__(self, nombre, apellido, dni, telefono, salario):
        super().__init__(nombre, apellido, dni, telefono)
        self.salario = salario

class Cliente(Persona):
    def __init__(self, nombre, apellido, dni, telefono, categoria):
        super().__init__(nombre, apellido, dni, telefono)
        self.categoria = categoria

emp = Empleado('Lucas', 'Mooco', '1234343', '2323098800', 2000)
cli = Cliente('Antuanette', 'Babbu', '2344556', '34345675770', 'VIP')

print(emp.nombre + ' ' + emp.apellido)
print(cli.nombre + ' ' + cli.apellido + ' ' + cli.categoria)

print (emp.nombre + ' ' + cli.nombre)