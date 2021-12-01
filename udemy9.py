class Restaurant:
    
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio  # Default: public, Protected, private

    def mostrar_informacion(self):
        print(
            f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

    # GETTERS Y SETTERS - Get = Obtiene un valor, SET = agrega un valor
    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


# Crear un clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, perros):
        super().__init__(nombre, categoria, precio)
        self.perros = perros

    # Reescribir metodo debe llamarse igual
    def mostrar_informacion(self):
        print(
            f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Perros: {self.perros}')

    # Agregar metodo que solo exista en hotel
    def get_perros(self):
        return self.perros
    

hotel = Hotel('Hotel POO', '5 Estrellas', 200, 'Si')
hotel.mostrar_informacion()
