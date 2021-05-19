
from parserT28.utils.decorators import singleton


@singleton
class OptimizationController(object):
    def __init__(self):
        self._idOptimization = 0
        self._optimizationList = []

    def getList(self):
        return self._optimizationList

    def destroy(self):
        self._idOptimization = 0
        self._optimizationList = []

    def add(self, no_optimizado, optimizado, regla):
        self._idOptimization += 1
        self._optimizationList.append(Optimization(
            self._idOptimization, no_optimizado, optimizado, regla))


class Optimization(object):
    def __init__(self, id, no_optimizado, optimizado, regla):
        self.__id = id
        self.__no_optimizado = no_optimizado
        self.__optimizado = optimizado
        self.__regla = regla

    def __repr__(self):
        return f'ID: {self.get_id()} No Optimizado: {self.get_no_optimizado()} ID Error: {self.get_id_error()} Description: {self.get_description()} Row: {self.get_row()} Column: {self.get_column()}'

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_no_optimizado(self):
        return self.__no_optimizado

    def set_no_optimizado(self, no_optimizado):
        self.__no_optimizado = no_optimizado

    def get_optimizado(self):
        return self.__optimizado

    def set_optimizado(self, optimizado):
        self.__optimizado = optimizado

    def get_regla(self):
        return self.__regla

    def set_regla(self, regla):
        self.__regla = regla
