class Restaurant:
    
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio # Default: public, Protected, private

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')

    # GETTERS Y SETTERS - Get = Obtiene un valor, SET = agrega un valor
    def get_precio(self):
        return self.__precio
    def set_precio(self,precio):
        self.__precio = precio
restaurant = Restaurant('Pizzeria', 'Comida italiana',50)

# restaurant.__precio = 100 # No será posible modificarlo con __ Private
restaurant.mostrar_informacion()
restaurant.set_precio(10)
precio = restaurant.get_precio()
print(precio)

restaurant2 = Restaurant('Hamburguesería', 'Comida USA', 20)
restaurant2.mostrar_informacion()
restaurant2.set_precio(1000)
precio2 = restaurant2.get_precio()
print(precio2)
