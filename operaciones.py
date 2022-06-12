def agregar_usuarios(list_temp):
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese apellido: ')
    dni = input('Ingrese dni: ')
    pais = input('Ingrese pais:')

    dict_temp = {
        'Nombre': nombre,
        'Apellido': apellido,
        'Dni': dni,
        'Pais': pais,
    }
    list_temp.append(dict_temp)


def eliminar_usuario_dni(list_temp):
    if not list_temp:  # linea para comrpobar si la lista esta vacia o no
        print('Lista vacia por favor agregar usuarios...')
    else:
        dni_temp = input('Ingrese dni: ')
        for i in range(len(list_temp)):
            if list_temp[i]['Dni'] == dni_temp:
                del list_temp[i]
                print('Usuario eliminado')
            else:
                opcion = input('Dni no registrado desea agregarlo ? (S/N)')
                if opcion.upper() == 'S':
                    nombre_temp = input('Ingrese nombre: ')
                    apellido_temp = input('Ingrese apellido: ')
                    pais_temp = input('Ingrese pais:')
                    dict_temp = {
                        'Nombre': nombre_temp,
                        'Apellido': apellido_temp,
                        'Dni': dni_temp,
                        'Pais': pais_temp,
                    }
                    list_temp.append(dict_temp)
                    print('Usuario registrado correctamente')
                    break

    print(list_temp)


def buscar_dni(list_temp):
    if not list_temp:
        print("Lista vacia porfavor agregar usuarios...")
    else:
        dni_temp = input("Ingrese dni: ")
        for i in range(len(list_temp)):
            if list_temp[i]['Dni'] == dni_temp:
                print(list_temp[i])
            else:
                print("Usuario no registrado")
                opcion = input('Dni no registrado desea agregarlo ? (S/N)')
                if opcion.upper() == 'S':
                    nombre_temp = input('Ingrese nombre: ')
                    apellido_temp = input('Ingrese apellido: ')
                    pais_temp = input('Ingrese pais:')
                    dict_temp = {
                        'Nombre': nombre_temp,
                        'Apellido': apellido_temp,
                        'Dni': dni_temp,
                        'Pais': pais_temp,
                    }
                    list_temp.append(dict_temp)
                    print('Usuario registrado correctamente')
                    break


def actualizar_usuario(list_temp):
    if not list_temp:  # linea para comrpobar si la lista esta vacia o no
        print('Lista vacia por favor agregar usuarios...')
    else:
        dni_temp = input('Ingrese dni: ')
        for i in range(len(list_temp)):
            if list_temp[i]['Dni'] == dni_temp:
                nombre_temp = input('Ingrese nuevo nombre: ')
                apellido_temp = input('Ingrese apellido nuevo: ')
                pais_temp = input('Ingrese nuevo pais: ')
                list_temp[i]['Nombre'] = nombre_temp
                list_temp[i]['Apellido'] = apellido_temp
                list_temp[i]['Dni'] = dni_temp
                list_temp[i]['Pais'] = pais_temp
                print('Usuario actualizado correctamente')
                print(list_temp)
                break
            else:
                opcion = input('Usuario no registrado desea agregarlo? (S/N)')
                if opcion.upper() == 'S':
                    nombre_temp = input('Ingrese nombre: ')
                    apellido_temp = input('Ingrese apellido: ')
                    pais_temp = input('Ingrese pais:')
                    dict_temp = {
                        'Nombre': nombre_temp,
                        'Apellido': apellido_temp,
                        'Dni': dni_temp,
                        'Pais': pais_temp,
                    }
                    list_temp.append(dict_temp)
                    print('Usuario registrado correctamente')
                    break


def listar_usuarios(list_temp):
    for i in list_temp:
        print(i)
