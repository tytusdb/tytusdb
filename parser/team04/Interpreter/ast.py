import math

from Interpreter.environment import Environment


class Ast:
    def __init__(self, root):
        self.root = root

    def execute(self):
        print("Ejecutando el AST...")
        e = Environment(functions=self.getNativeFuncs())

        for inst in self.root:
            inst.execute(e)

        '''
        try:
            for inst in self.root:
                inst.execute(e)
            print("AST ejecutado exitosamente!")
        except:
            print("Error al ejecutar el AST!")
        '''

    def getGraph(self):
        print("Generando el grafo")

    def getNativeFuncs(self):
        functions = {
            # Mathematical Functions
            'ABS': lambda z: math.fabs(z),
            'CBRT': '',
            'CEIL': lambda z: math.ceil(z),
            'CEILING': '',
            'DEGREES': lambda z: math.degrees(z),
            'DIV': '',
            'EXP': lambda z: math.frexp(z),
            'FACTORIAL': lambda z: math.factorial(z),
            'FLOOR': lambda z: math.floor(z),
            'GCD': lambda x, y: math.gcd(x, y),
            'LCM': '',
            'LN': '',
            'LOG': lambda z: math.log(z),
            'LOG10': lambda z: math.log10(z),
            'MIN_SCALE': '',

            'MOD': lambda x, y: math.fmod(x, y),
            'PI': math.pi,
            'POWER': lambda x, y: math.pow(x, y),
            'RADIANS': lambda z: math.radians(z),
            'ROUND': lambda x, y: round(x, y),

            'SCALE': '',
            'SIGN': '',
            'SQRT': lambda z: math.sqrt(z),
            'TRIM_SCALE': '',
            'TRUC': '',
            'WIDTH_BUCKET': '',
            'RANDOM': '',
            'SETSEED': '',
            # Trigonometric Functions
            'ACOS': lambda z: math.cosh(z),
            'ACOSD': '',
            'ASIN': '',
            'ASIND': '',
            'ATAN': '',
            'ATAND': '',
            'ATAN2': '',
            'ATAN2D': '',
            'COS': '',
            'COSD': '',
            'COT': '',
            'COTD': '',
            'SIN': '',
            'SIND': '',
            'TAN': '',
            'TAND': '',
            'SINH': '',
            'COSH': '',
            'TANH': '',
            'ASINH': '',
            'ACOSH': '',
            'ATANH': '',
            # Binary String Functions
            '||': '',
            'LENGTH': '',
            'SUBSTRING': '',
            'TRIM': '',
            'GET_BYTE': '',
            'MD5': '',
            'SET_BYTE': '',
            'SHA256': '',
            'SUBSTR': '',
            'CONVERT': '',
            'ENCODE': '',
            'DECODE': '',

            'FSUM': lambda z: math.fsum(z),
            'FMOD': lambda x, y: math.fmod(x, y),
            'COPYSIGN': lambda x, y: math.copysign(x, y)
        }
        return functions
