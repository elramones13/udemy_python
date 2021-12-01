class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')


restaurant = Restaurant('Pizzeria', 'Comida italiana',50)
restaurant.mostrar_informacion()


restaurant2 = Restaurant('Hamburguesería', 'Comida USA', 20)
restaurant2.mostrar_informacion()
