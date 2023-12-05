# from conexion import Conexion
from cursor_pool import CursorDelPool
from user_dev import User_dev
from logger_base import log
from check import check

class DevDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM profile ORDER BY id_dev'
    _INSERTAR = ('INSERT INTO profile(name, email, years_experience, level_experience, skills, request) VALUES(%s, '
                 '%s, %s, %s, %s, %s)')
    _ACTUALIZAR = ('UPDATE profile SET name=%s, email=%s, years_experience=%s, level_experience=%s, skills=%s, '
                   'request=%s WHERE id_dev=%s')
    _ELIMINAR = 'DELETE FROM profile WHERE id_dev=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registers = cursor.fetchall()
            developers = []
            for register in registers:
                dev = User_dev(register[0], register[1], register[2], register[3], register[4], register[5], register[6])
                developers.append(dev)
            return developers

    @classmethod
    def insertar(cls, developer):
        with CursorDelPool() as cursor:
            years = developer.years_experience
            resultado = check.check_year(years)
            level, skill, req = resultado
            valores = (developer.name, developer.email, developer.years_experience, level, skill, req)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {developer}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, developer):
        with CursorDelPool() as cursor:
            years = developer.years_experience
            resultado = check.check_year(years)
            level, skill, req = resultado
            valores = (developer.name, developer.email, developer.years_experience, level, skill, req, developer.id_dev)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {developer}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, developer):
        with CursorDelPool() as cursor:
            valores = (developer.id_dev,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {developer}')
            return cursor.rowcount


if __name__ == '__main__':
    # # Insertar un registro
    # persona1 = User_dev(name='Caro Bernal', email='cbernal@mail.com', years_experience=3, level_experience=())
    # personas_insertadas = DevDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')

    # # Actualizar un registro
    # persona1 = User_dev(6, 'Caro Bernal', 'cbernal@mail.com', 4)
    # personas_actualizadas = DevDAO.actualizar(persona1)
    # log.debug(f'Personas insertadas: {personas_actualizadas}')
    #
    # # Eliminar un registro
    # persona1 = User_dev(id_dev=3)
    # personas_eliminadas = DevDAO.eliminar(persona1)
    # log.debug(f'Personas eliminadas: {personas_eliminadas}')
    #
    # Seleccionar objetos
    personas = DevDAO.seleccionar()
    for persona in personas:
        log.debug(persona)