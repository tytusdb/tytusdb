

class Aritmetica():
    def __init__(self, literal, expresion, linea):
        self.literal = literal
        self.expresion = expresion
        self.linea = linea

    def optimizacion(self, reglas, pendiente):
        #print('Ejecutando optimización de operaciones aritmeticas')
        codigo = ""

        if self.expresion[1] != None:
            valor1 = self.expresion[0]
            valor2 = self.expresion[2]
            op = self.expresion[1]
            
            #********************
            #******* SUMA *******
            #********************
            if op == '+':
                #Determina si el valor 2 es igual a 0
                if valor2 == 0:

                    #Verifica si la literal es igual al valor1
                    if self.literal == valor1:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' + ' + str(valor2)
                        nuevo = 'Se elimina la instrucción'
                        regla = '8,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '\'\'\'Se cumple la regla 8 \n' + anterior + '\nCodigo eliminado\'\'\''
                        pendiente.append(code)

                    elif self.literal != valor1:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' + ' + str(valor2)
                        nuevo = str(self.literal) + ' = ' + str(valor1)
                        regla = '12,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '#Se cumple la regla 12 \n' + nuevo 
                        pendiente.append(code)

                #Compara si el valor1 es igual a 0
                elif valor1 == 0:

                    #Verifica si la literal es igual al valor2
                    if self.literal == valor2:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' + ' + str(valor2)
                        nuevo = 'Se elimina la instrucción'
                        regla = '8,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '\'\'\'Se cumple la regla 8 \n' + anterior + '\nCodigo eliminado\'\'\''
                        pendiente.append(code)

                    elif self.literal != valor2:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' + ' + str(valor2)
                        nuevo = str(self.literal) + ' = ' + str(valor2)
                        regla = '12,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '#Se cumple la regla 12 \n' + nuevo 
                        pendiente.append(code)

                #Ninguno de los valores es 0
                else:
                    print('No hay cambios')
                    nuevo = str(self.literal) + ' = ' + str(valor1) + ' + ' + str(valor2) 
                    pendiente.append(nuevo)

            #********************
            #****** RESTA *******
            #********************
            elif op == '-':

                #Determina si el valor 2 es igual a 0
                if valor2 == 0:

                    #Verifica si la literal es igual al valor1
                    if self.literal == valor1:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' - ' + str(valor2)
                        nuevo = 'Se elimina la instrucción'
                        regla = '9,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '\'\'\'Se cumple la regla 9 \n' + anterior + '\nCodigo eliminado\'\'\''
                        pendiente.append(code)

                    elif self.literal != valor1:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' - ' + str(valor2)
                        nuevo = str(self.literal) + ' = ' + str(valor1)
                        regla = '13,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '#Se cumple la regla 13 \n' + nuevo 
                        pendiente.append(code)

                #Compara si el valor1 es igual a 0
                elif valor1 == 0:

                    #Verifica si la literal es igual al valor2
                    if self.literal == valor2:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' - ' + str(valor2)
                        nuevo = 'Se elimina la instrucción'
                        regla = '9,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '\'\'\'Se cumple la regla 9 \n' + anterior + '\nCodigo eliminado\'\'\''
                        pendiente.append(code)

                    elif self.literal != valor2:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' - ' + str(valor2)
                        nuevo = str(self.literal) + ' = ' + str(valor2)
                        regla = '13,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '#Se cumple la regla 13 \n' + nuevo 
                        pendiente.append(code)

                #Ninguno de los valores es 0
                else:
                    print('No hay cambios')
                    nuevo = str(self.literal) + ' = ' + str(valor1) + ' - ' + str(valor2) 
                    pendiente.append(nuevo)

            #********************
            #******* POR ********
            #********************
            elif op == '*':

                #Determina si el valor 2 es igual a 1
                if valor2 == 1:
                    #Verifica si la literal es igual al valor1
                    if self.literal == valor1:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' * ' + str(valor2)
                        nuevo = 'Se elimina la instrucción'
                        regla = '10,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '\'\'\'Se cumple la regla 10 \n' + anterior + '\nCodigo eliminado\'\'\''
                        pendiente.append(code)

                    elif self.literal != valor1:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' * ' + str(valor2)
                        nuevo = str(self.literal) + ' = ' + str(valor1)
                        regla = '14,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '#Se cumple la regla 14 \n' + nuevo 
                        pendiente.append(code)

                #Compara si el valor1 es igual a 1
                elif valor1 == 1:

                    #Verifica si la literal es igual al valor2
                    if self.literal == valor2:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' * ' + str(valor2)
                        nuevo = 'Se elimina la instrucción'
                        regla = '10,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '\'\'\'Se cumple la regla 10 \n' + anterior + '\nCodigo eliminado\'\'\''
                        pendiente.append(code)

                    elif self.literal != valor2:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' * ' + str(valor2)
                        nuevo = str(self.literal) + ' = ' + str(valor2)
                        regla = '14,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '#Se cumple la regla 14 \n' + nuevo 
                        pendiente.append(code)

                #Verifica si el valor2 es igual a 0
                elif valor2 == 0:
                    anterior = str(self.literal) + ' = ' + str(valor1) + ' * ' + str(valor2)
                    nuevo = str(self.literal) + ' = 0'
                    regla = '17,'+anterior+','+nuevo+','+str(self.linea)
                    reglas.append(regla)
                    code = '#Se cumple la regla 17 \n' + nuevo 
                    pendiente.append(code)

                #Verifica si el valor1 es igual a 0
                elif valor1 == 0:
                    anterior = str(self.literal) + ' = ' + str(valor1) + ' * ' + str(valor2)
                    nuevo = str(self.literal) + ' = 0'
                    regla = '17,'+anterior+','+nuevo+','+str(self.linea)
                    reglas.append(regla)
                    code = '#Se cumple la regla 17 \n' + nuevo
                    pendiente.append(code)
                    
                #Verifica si el valor1 es igual a 2
                elif valor1 == 2:
                    anterior = str(self.literal) + ' = ' + str(valor1) + ' * ' + str(valor2)
                    nuevo = str(self.literal) + ' = ' + str(valor2) + ' + ' + str(valor2)
                    regla = '16,'+anterior+','+nuevo+','+str(self.linea)
                    reglas.append(regla)
                    code = '#Se cumple la regla 16 \n' + nuevo
                    pendiente.append(code)

                #Verifica si el valor2 es igual a 2
                elif valor2 == 2:
                    anterior = str(self.literal) + ' = ' + str(valor1) + ' * ' + str(valor2)
                    nuevo = str(self.literal) + ' = ' + str(valor1) + ' + ' + str(valor1)
                    regla = '16,'+anterior+','+nuevo+','+str(self.linea)
                    reglas.append(regla)
                    code = '#Se cumple la regla 16 \n' + nuevo
                    pendiente.append(code)

                #Ninguno de los casos anteriores
                else:
                    nuevo = str(self.literal) + ' = ' + str(valor1) + ' * ' + str(valor2)
                    pendiente.append(nuevo)
            
            #********************
            #******* DIV ********
            #********************
            elif op == '/':

                #Determina si el valor 2 es igual a 1
                if valor2 == 1:
                    #Verifica si la literal es igual al valor1
                    if self.literal == valor1:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' / ' + str(valor2)
                        nuevo = 'Se elimina la instrucción'
                        regla = '11,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '\'\'\'Se cumple la regla 11 \n' + anterior + '\nCodigo eliminado\'\'\''
                        pendiente.append(code)

                    elif self.literal != valor1:
                        anterior = str(self.literal) + ' = ' + str(valor1) + ' / ' + str(valor2)
                        nuevo = str(self.literal) + ' = ' + str(valor1)
                        regla = '15,'+anterior+','+nuevo+','+str(self.linea)
                        reglas.append(regla)
                        code = '#Se cumple la regla 15 \n' + nuevo 
                        pendiente.append(code)

                #Verifica si el valor1 es igual a 0
                elif valor1 == 0:
                    anterior = str(self.literal) + ' = ' + str(valor1) + ' / ' + str(valor2)
                    nuevo = str(self.literal) + ' = 0'
                    regla = '18,'+anterior+','+nuevo+','+str(self.linea)
                    reglas.append(regla)
                    code = '#Se cumple la regla 18 \n' + nuevo
                    pendiente.append(code)
                    
                #Ninguno de los casos anteriores
                else:
                    nuevo = str(self.literal) + ' = ' + str(valor1) + ' / ' + str(valor2)
                    pendiente.append(nuevo)

            elif op == '%':
                nuevo = str(self.literal) + ' = ' + str(valor1) + ' % ' + str(valor2)
                pendiente.append(nuevo)