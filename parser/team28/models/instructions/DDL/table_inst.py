from models.instructions.shared import Instruction
from controllers.type_checker import TypeChecker
from controllers.error_controller import ErrorController


class CreateTB(Instruction):

    def __init__(self, table_name, column_list, inherits_from):
        self._table_name = table_name
        self._column_list = column_list
        self._inherits_from = inherits_from

    def __repr__(self):
        return str(vars(self))

    def execute(self):
        pass


class DropTB(Instruction):

    def __init__(self, table_name, noLine, noColumn):
        self._table_name = table_name
        self._noLine = noLine
        self._noColumn = noColumn

    def __repr__(self):
        return str(vars(self))

    def process(self, instrucction):
        typeChecker = TypeChecker()
        database = None  # TODO Obtener desde la tabla de simbolos

        if not database:
            desc = f": Database not selected"
            ErrorController().addExecutionError(4, 'Execution', desc,
                                                self._noLine, self._noColumn)
            return

        typeChecker.deleteTable(database, self._table_name,
                                self._noLine, self._noColumn)


class AlterTable(Instruction):
    '''
        ALTER TABLE cambia una tabla con diversas opciones de alterar
    '''

    def __init__(self, tablaAModificar, listaCambios):
        self._tablaAModificar = tablaAModificar
        self._listaCambios = listaCambios

    def execute(self):
        pass

    def __repr__(self):
        return str(vars(self))


class AlterTableAdd(AlterTable):
    '''
        puedo agregar una columna
        puedo agregar un check
        puedo agregar  un constraint
        puedo agregar un foreing
    '''

    def __init__(self, changeContent):
        self._changeContent = changeContent

    def __repr__(self):
        return str(vars(self))


class AlterTableAlter(AlterTable):
    '''
        puedo alterar una columna colocandole not null
        puedo alterar una columna asignandole otro tipo     
    '''

    def __init__(self, changeContent):
        self._changeContent = changeContent

    def __repr__(self):
        return str(vars(self))


class AlterTableDrop(AlterTable):
    '''
        puedo eliminar una columna
        puedo eliminar un constraint   
    '''

    def __init__(self, changeContent):
        self._changeContent = changeContent

    def __repr__(self):
        return str(vars(self))


class AlterTableRename(AlterTable):
    '''
        puedo cambiarle el nombre a una tabla  
    '''

    def __init__(self, oldName, newName):
        self._oldName = oldName
        self._newName = newName

    def __repr__(self):
        return str(vars(self))
