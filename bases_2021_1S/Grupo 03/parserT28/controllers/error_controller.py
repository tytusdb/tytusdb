from parserT28.utils.decorators import singleton
from parserT28.models.error import Error
from parserT28.models.type_error import get_type_error
from parserT28.views.data_window import DataWindow


@singleton
class ErrorController(object):
    def __init__(self):
        self._idError = 0
        self._errorsList = []

    def getList(self):
        return self._errorsList

    def destroy(self):
        self._idError = 0
        self._errorsList = []

    def add(self, noType, errorType, desc, line, column):
        numberError, description = get_type_error(noType)
        self._idError += 1
        description += f": {desc}"
        description = ' '.join(description.split())
        description = description.replace(': :', ':')

        self._errorsList.append(Error(self._idError, errorType, numberError,
                                      description, line, column))
        DataWindow().consoleTable(['Code', 'Description'],
                                  [[numberError, description]])
