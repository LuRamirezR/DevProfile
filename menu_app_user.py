from user_dev import User_dev
from dev_dao import DevDAO
from logger_base import log

choice = None
while choice != 5:
    print('Opciones')
    print('1. Listar perfiles de desarrolladores')
    print('2. Agregar perfil del desarrollador')
    print('3. Modificar perfil del desarrollador')
    print('4. Eliminar perfil del desarrollador')
    print('5. Salir')
    choice = int(input('Escribe tu opcion (1-5): '))
    if choice == 1:
        users = DevDAO.seleccionar()
        for user in users:
            log.info(user)
    elif choice == 2:
        name_var = input('Escribe tu nombre y apellido: ')
        email_var = input('Escribe tu correo: ')
        years_var = int(input('Escribe los años que tienes de experiencia: '))
        usuario = User_dev(name=name_var, email=email_var, years_experience=years_var)
        usuarios_insertados = DevDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif choice == 3:
        id_dev_var = int(input('Escribe el id_dev a modificar: '))
        name_var = input('Escribe tu nombre y apellido: ')
        email_var = input('Escribe tu nuevo correo: ')
        years_var = int(input('Escribe los años que tienes de experiencia: '))
        usuario = User_dev(id_dev_var, name_var, email_var, years_var)
        usuario_actualizado = DevDAO.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuario_actualizado}')
    elif choice == 4:
        id_dev_var = int(input('Escribe el id_dev a eliminar: '))
        usuario = User_dev(id_dev=id_dev_var)
        usuario_eliminado = DevDAO.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuario_eliminado}')
else:
    log.info('Salimos de la aplicacion...')