from operaciones import *

ejecutar = True
usuarios = [
    {'Nombre': 'Arturo', 'Apellido': 'Pastrana', 'Dni': '23433454', 'Pais': 'Peru'},
    {'Nombre': 'Jose', 'Apellido': 'Perez', 'Dni': '45544554', 'Pais': 'Chile'},
    {'Nombre': 'Pedro', 'Apellido': 'Munoz', 'Dni': '87667665', 'Pais': 'Colombia'}
]


def principal():
    opciones = ""

    while ejecutar:
        print("\n****** MENU DE OPCIONES *******\n")
        print("===============================")
        print("1) AGREGAR USUARIO")
        print("2) ELIMINAR USUARIO POR DNI")
        print("3) BUSCAR USUARIO")
        print("4) ACTUALIZAR USUARIO")
        print("5) LISTAR USUARIOS")
        print("6) SALIR")
        print("===============================\n")
        opciones = input("Ingrese una opcion: ")

        if opciones in ("1", "2", "3", "4", "5"):
            if opciones == "1":
                agregar_usuarios(usuarios)
            elif opciones == "2":
                eliminar_usuario_dni(usuarios)
            elif opciones == "3":
                buscar_dni(usuarios)
            elif opciones == "4":
                actualizar_usuario(usuarios)
            elif opciones == "5":
                listar_usuarios(usuarios)

        else:
            break


if __name__ == '__main__':
    principal()
