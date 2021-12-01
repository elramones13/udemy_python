import os

CARPETA = 'contacto/'
EXTENSION = '.txt'

#CREAR UNA CLASE
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

#MAIN    
def app():

    crear_directorio()
    
    mostrar_menu()


    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion:\r\n')
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo')


#CRUD APP
def eliminar_contacto():
    nombre = input('seleccione el contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA+ nombre + EXTENSION)
        print('\r\n Eliminado correctamente')
    except IOError:
        print('No existe el contacto')
        app()

def buscar_contacto():
    nombre = input('seleccione el contacto que desea buscar: \r\n')

    try:
        with open (CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        app()

def mostrar_contacto():
    archivos = os.listdir(CARPETA)
    archivos_txt = [ i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')

def editar_contacto():
    print('Escribe el nombre de contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar:\r\n')

    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre_contacto = input('Agrega el nuevo Nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo telefono: \r\n')
            categoria_contacto = input('Agrega nueva Categoria: \r\n')

            contacto = Contacto(nombre_contacto, telefono_contacto,categoria_contacto)

            archivo.write('Nombre: ' + nombre_contacto + "\r\n")
            archivo.write('Telefono: ' + telefono_contacto + "\r\n")
            archivo.write('Categoria: ' + categoria_contacto + "\r\n")
            print('Editado correctamente el Contacto')
            
        
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
    else:
        print('Ese contacto no existe')

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto')
    nombre_contacto = input('Nombre del contacto:\r\n')
    telefono_contacto = input('Agrega el telefono contacto\r\n')
    categoria_contacto = input('Categoria del contacto:\r\n')

    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # Instanciar la clase
            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)

            archivo.write('Nombre: '+ nombre_contacto + "\r\n")
            archivo.write('Telefono: '+ telefono_contacto + "\r\n")
            archivo.write('Categoria: ' + categoria_contacto + "\r\n")
            print('Creado correctamente el Contacto')
    else:
        print('Ese Contacto ya existe')

    #Reiniciar la App
    app()


#MENU
def mostrar_menu():
    print('Seleccione del menu lo que desee hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contacto')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')


#OPERACIONES UTILES
def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()
