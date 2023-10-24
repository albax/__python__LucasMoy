from Empleado import Empleado
from Cliente import Cliente

emp = Empleado('Lucas', 'Mooco', '1234343', '2323098800', 2000)
cli = Cliente('Antuanette', 'Babbu', '2344556', '34345675770', 'VIP')

# print(emp.nombre + ' ' + emp.apellido)
# print(cli.nombre + ' ' + cli.apellido + ' ' + cli.categoria)
# print (emp.nombre + ' ' + cli.nombre)

print(emp)  # <Empleado.Empleado object at 0x0000026637F6F610> ## __str__ como default
print(cli)  # <Empleado.Empleado object at 0x00xxxxxxxxxxxxxx> ## __str__ como default

# print(emp.salario) # 2000
# print(cli.telefono) #


## carga data
## creamos al EMPLEADO

def cargar():
    respuesta = input('¿Va a agregar un empleado?: ')
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    dni = input('Ingrese el DNI: ')
    telefono = input('Ingrese el telefono: ')
    
    if (respuesta == 'si'):
        salario = input('Ingrese el salario: ')
        emp = Empleado(nombre, apellido, dni, telefono, int(salario))
        print(emp)

cargar()