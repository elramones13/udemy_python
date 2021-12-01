class Restaurant:
    

    def agregar_restaurant(self, nombre):
        self.nombre = nombre
        print('Agregando...')

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')


restaurant = Restaurant()
restaurant.agregar_restaurant('Pizzeria')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Hamburguesería')
restaurant2.mostrar_informacion()



print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')
