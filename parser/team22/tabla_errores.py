class Error():
    'Esta clase representa un error dentro de nuestra tabla de errores'

    def __init__(self, tipo, descripcion, linea):
        self.tipo = tipo
        self.descripcion = descripcion
        self.linea = linea

    def imprimir(self):
        return [self.tipo, self.descripcion, self.linea]

class TablaDeErrores():
    'Esta clase representa la tabla de errores'

    def __init__(self, errores = []):
        self.errores = errores

    def agregar(self, error) :
        self.errores.append(error)

class Codigos():
    'Esta clase representa una alerta con código dentro de nuestra consola'

    def database_successful_completion(self, name: str):
        return 'CREATE DATABASE «' + name + '» \nConsulta devuelta correctamente \nSQL state: 00000\n'

    def database_duplicate_database(self, name: str):
        return 'ERROR: La base de datos «' + name + '» ya existe\n' + 'SQL state: 42P04\n'

    def database_internal_error(self, name: str):
        return 'ERROR INTERNO: «' + name + '»\nSQL state: XX000\n'

    def database_undefined_object(self, name: str):
        return 'ERROR: La base de datos «' + name + '» no existe\n' + 'SQL state: 42704\n'

    def table_successful(self, name: str):
        return 'CREATE TABLE «' + name + '»\nConsulta devuelta correctamente \nSQL state: 00000\n'

    def table_duplicate_table(self, name: str):
        return 'ERROR: La tabla «' + name + '» ya existe\n' + 'SQL state: 42P07\n'

    def table_undefined_table(self, name: str):
        return 'ERROR: La tabla «' + name + '» no existe\n' + 'SQL state: 42P01\n'

    def successful_completion(self, consulta: str):
        return consulta + '\nConsulta devuelta correctamente \nSQL state: 00000\n'

    def trigonometric_function_out_of_range(self, name: str, value: str, limit: str):
        return 'ERROR: La función «' + name + '» permite un rango de [' + limit +'] y se ingresó: '+value +'. \n' + 'SQL state: 22003\n'
    