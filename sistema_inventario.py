# sistema_inventario.py

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.validar_nombre(nombre)
        self.validar_precio(precio)
        self.validar_cantidad(cantidad)

        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    # Validaciones
    def validar_nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío y debe ser texto.")

    def validar_precio(self, precio):
        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

    def validar_cantidad(self, cantidad):
        if not isinstance(cantidad, (int, float)):
            raise TypeError("La cantidad debe ser un número entero.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

    # Métodos requeridos
    def actualizar_precio(self, nuevo_precio):
        self.validar_precio(nuevo_precio)
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        self.validar_cantidad(nueva_cantidad)
        self.cantidad = int(nueva_cantidad)

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return (f"Producto: {self.nombre} | "
                f"Precio: ${self.precio:.2f} | "
                f"Cantidad: {self.cantidad} | "
                f"Valor total: ${self.calcular_valor_total():.2f}")


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")
        self.productos.append(producto)

    def buscar_producto(self, nombre: str):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def calcular_valor_inventario(self):
        return sum(p.calcular_valor_total() for p in self.productos)

    def listar_productos(self):
        if not self.productos:
            print("\nEl inventario está vacío.\n")
            return

        print("\n--- LISTA DE PRODUCTOS ---")
        for producto in self.productos:
            print(producto)
        print("--------------------------\n")


# MENÚ INTERACTIVO
def menu_principal(inventario: Inventario):
    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))

                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("Producto agregado correctamente.")

            elif opcion == "2":
                nombre = input("Nombre a buscar: ")
                producto = inventario.buscar_producto(nombre)

                if producto:
                    print("\nProducto encontrado:")
                    print(producto)
                else:
                    print("Producto no encontrado.")

            elif opcion == "3":
                inventario.listar_productos()

            elif opcion == "4":
                total = inventario.calcular_valor_inventario()
                print(f"\nValor total del inventario: ${total:.2f}\n")

            elif opcion == "5":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

        except ValueError as ve:
            print(f"Error de valor: {ve}")
        except TypeError as te:
            print(f"Error de tipo: {te}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)