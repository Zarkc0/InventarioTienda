class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print("Error: El precio y la cantidad deben ser mayores que cero.")
            return

        for p in self.productos:
            if p["nombre"].lower() == nombre.lower():
                p["cantidad"] += cantidad
                p["precio"] = precio
                print(f"Stock de '{nombre}' actualizado.")
                return

        nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        self.productos.append(nuevo_producto)
        print(f"Producto '{nombre}' agregado exitosamente.")

    def vender_producto(self, nombre, cantidad):
        if cantidad <= 0:
            print("Error: La cantidad a vender debe ser mayor a cero.")
            return

        for p in self.productos:
            if p["nombre"].lower() == nombre.lower():
                if p["cantidad"] >= cantidad:
                    p["cantidad"] -= cantidad
                    print(f"Venta exitosa: {cantidad} unidad(es) de '{nombre}'.")
                    return
                else:
                    print(f"Error: Stock insuficiente. Solo hay {p['cantidad']} unidad(es) de '{nombre}'.")
                    return

        print(f"Error: El producto '{nombre}' no existe en el inventario.")

    def mostrar_inventario(self):
        print(f"\n--- Inventario de {self.nombre_tienda} ---")
        if not self.productos:
            print("El inventario está vacío.")
            return
        
        for p in self.productos:
            print(f"Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Stock: {p['cantidad']}")
        print("-" * 35)

    def producto_mas_caro(self):
        if not self.productos:
            print("El inventario esta vacio.")
            return None

        mas_caro = self.productos[0]
        for p in self.productos:
            if p["precio"] > mas_caro["precio"]:
                mas_caro = p
        
        return mas_caro["nombre"], mas_caro["precio"]

def main():
    tienda = InventarioTienda("Súper Todo")

    while True:
        print("\n" + "="*30)
        print(f"MENÚ - {tienda.nombre_tienda}")
        print("="*30)
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver el inventario")
        print("4. Consultar el producto más caro")
        print("5. Salir")
        print("="*30)

        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: $"))
                cantidad = int(input("Cantidad a agregar: "))
                tienda.agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print("Error: Ingresa números válidos para el precio y la cantidad.")

        elif opcion == '2':
            nombre = input("Nombre del producto a vender: ")
            try:
                cantidad = int(input("Cantidad a vender: "))
                tienda.vender_producto(nombre, cantidad)
            except ValueError:
                print("Error: Ingresa un número entero válido para la cantidad.")

        elif opcion == '3':
            tienda.mostrar_inventario()

        elif opcion == '4':
            resultado = tienda.producto_mas_caro()
            if resultado:
                nombre, precio = resultado
                print(f"\n El producto más caro es '{nombre}' con un precio de ${precio:.2f}")

        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")

if __name__ == "__main__":
    main()

            
