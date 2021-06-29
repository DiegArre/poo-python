class Tienda:
    def __init__ (self,nombre):
        self.nombre = nombre
        self.lista_productos = []


    def añadir_producto(self,producto):
        self.lista_productos.append(producto)
        return self

    def vender_producto(self,id):
       p = self.lista_productos[id].pop
       print(f"Se vendio : {p}")
       return self

    def inflacion(self,porcentaje_cambio):
        for producto in self.lista_productos:
            producto.actualizar_precio(porcentaje_cambio,True)
        return self
    
    def precio_categoria(self,categoria,porcentaje_cambio):
        for producto in self.lista_productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(porcentaje_cambio,False)
        return self
    




class Producto: 
    def __init__(self,nombre,precio,categoria):
        self.id = None
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def actualizar_precio(self,porcentaje_cambio,aumenta):
        if aumenta:
            self.precio += self.precio*porcentaje_cambio
            return self
        self.precio -= self.precio*porcentaje_cambio
        return self

    def print_info(self):
        print(f"Nombre: {self.nombre} Categoria: {self.categoria} Precio: {self.precio}")
        return self

    

    