from Vehiculo import Vehiculo
from FlotaVehiculos import FlotaVehiculos


def solicitar_datos_vehiculo():
    print("\nIngresando nuevo vehiculo:")
    print("El número de placa debe cumplir con el formato: 3 letras mayúsculas seguidas de 2 números.")

    placa = input("Ingrese la placa del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    anio = int(input("Ingrese el año: "))
    kilometraje = int(input("Ingrese el kilometraje: "))

    try:
        Vehiculo(placa, marca, modelo, anio, kilometraje)
    except Exception as e:
        print(f"\n{e}")
    else:
        return Vehiculo(placa, marca, modelo, anio, kilometraje)



def vehiculo_seleccionado(vehiculo):
    while True:
        print("\n¿Qué desea hacer con el vehículo?")
        print("1. Mostrar información")
        print("2. Agregar mantenimiento")
        print("3. Consultar historial de mantenimientos")
        print("4. Calcular costos de mantenimiento")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                print(
                    f"\nPlaca: {vehiculo.placa} | Marca: {vehiculo.marca} | Modelo: {vehiculo.modelo} | Kilometraje: {vehiculo.kilometraje}")
            case "2":
                vehiculo.agregar_mantenimiento()
            case "3":
                vehiculo.consultar_matenimientos()
            case "4":
                vehiculo.consultar_costos_mantenimiento()
            case "5":
                break
            case _:
                print(" Opción no válida, intente de nuevo.")


def menu():
    nueva_flota = FlotaVehiculos()

    while True:
        print("\nMenú Principal")
        print("1. Registrar un nuevo vehículo")
        print("2. Eliminar un vehículo por su placa")
        print("3. Buscar un vehículo por su placa")
        print("4. Listar todos los vehículos registrados")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                nuevo_vehiculo = solicitar_datos_vehiculo()
                if nuevo_vehiculo:
                    nueva_flota.insertar_vehiculo(nuevo_vehiculo)

            case "2":
                if nueva_flota.esta_vacia():
                    print("\nNo existen vehículos en la flota.")
                else:
                    placa = input("\nIngrese la placa del vehículo a eliminar: ")
                    nueva_flota.eliminar_vehiculo(placa)

            case "3":
                if nueva_flota.esta_vacia():
                    print("\n️No existen vehículos en la flota.")
                else:
                    placa = input("Ingrese la placa del vehículo a buscar: ")
                    vehiculo = nueva_flota.buscar_vehiculo(placa)
                    if vehiculo:
                        vehiculo_seleccionado(vehiculo)

            case "4":
                if nueva_flota.esta_vacia():
                    print("\n️No existen vehículos en la flota.")
                else:
                    nueva_flota.mostrar_vehiculos()

            case "5":
                print("\nSaliendo del programa...")
                break

            case _:
                print("️ Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()
