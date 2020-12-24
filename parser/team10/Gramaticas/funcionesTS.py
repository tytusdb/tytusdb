from ReporteTS import *

class objTabla():
    def __init__(self):
        print('creacion OBj tabla')
        
        
    def agregaraTS(self,identificador, nombre, tipo, declarada_en, ambito, atributos):
        global tsgen
        global baseActual
        global tablaActual
        tsgen[identificador] = {'nombre': nombre, 'tipo': tipo, 'declarada_en': declarada_en,
                                'ambito': ambito, 'atibutos': atributos}


    def modificarTS_Base(self, base, nuevoNombre):
        for i in tsgen:
            if str(tsgen[i]['tipo']) == str("base") and str(tsgen[i]['nombre']) == str(base):
                tsgen[i]['nombre'] = str(nuevoNombre)
                
            if str(tsgen[i]['ambito']) == str(base):
                tsgen[i]['ambito'] = str(nuevoNombre)

            if str(tsgen[i]['declarada_en']) == str(base):
                tsgen[i]['declarada_en'] = str(nuevoNombre)
            


    def modificarNombreTabla_TS(self, base, tabla, nombre):

        for i in tsgen:
            if str(tsgen[i]['declarada_en']) == str(base) and str(tsgen[i]['nombre']) == str(tabla):
                tsgen[i]['nombre'] = str(nombre)
            
            if str(tsgen[i]['declarada_en']) == str(tabla):
                tsgen[i]['declarada_en'] = str(nombre)


    def modificarTipoCampo_TS(self, base, tabla, campo, tipo):
        for i in tsgen:
            if str(tsgen[i]['ambito']) == str(base) and str(tsgen[i]['declarada_en']) == str(tabla) and str(
                    tsgen[i]['nombre']) == str(campo):
                tsgen[i]['tipo'] = str(tipo)


    def eliminarCampo_TS(self, base, tabla, campo):
        for i in tsgen:
            if str(tsgen[i]['ambito']) == str(base) and str(tsgen[i]['declarada_en']) == str(tabla) and str(
                    tsgen[i]['nombre']) == str(campo):
                del tsgen[i]
                break


    def eliminarTS_Base(self, base):
        for i in tsgen:
            if str(tsgen[i]['tipo']) == str("base") and str(tsgen[i]['nombre']) == str(base):
                print("Dentro de eliminar")
                print(tsgen.pop('nombre', base))
                del tsgen[i]
                self.recorrerEliminarBase(base)
                break


    def recorrerEliminarBase(self, base):
        for i in tsgen:
            if str(tsgen[i]['ambito']) == str(base) or str(tsgen[i]['declarada_en']) == str(base):
                del tsgen[i]
                self.recorrerEliminarBase(base)
                break

    

    def eliminarTS_Tabla(self, base, tabla):
        for i in tsgen:
            if str(tsgen[i]['declarada_en']) == str(base) and str(tsgen[i]['nombre']) == str(tabla):
                del tsgen[i]
                self.recorrerEliminarTabla(base, tabla)
                break


    def recorrerEliminarTabla(self, base, tabla):
        for i in tsgen:
            if str(tsgen[i]['ambito']) == str(base) and str(tsgen[i]['declarada_en']) == str(tabla):
                del tsgen[i]
                self.recorrerEliminarTabla(base, tabla)
                break


    def devolverCampos(self, base, tabla):
        campos = []
        for i in tsgen:
            if str(tsgen[i]['ambito']) == str(base) or str(tsgen[i]['declarada_en']) == str(base):
                if str(tsgen[i]['declarada_en']) == str(tabla):
                    # print("Encontrado campo " + str(tsgen[i]['nombre']))
                    campos.append(str(tsgen[i]['nombre']))

        return campos

    def devolverCampo(self, base, tabla, ids):
        campos = []
        for i in tsgen:
            if str(tsgen[i]['ambito']) == str(base) or str(tsgen[i]['declarada_en']) == str(base):
                if str(tsgen[i]['declarada_en']) == str(tabla):
                    if str(tsgen[i]['nombre'])==ids:
                        campos.append(tsgen[i])
                    

        return campos


    def devolverPosicionCampos(self, base, tabla, campo):
        campos = self.devolverCampos(base, tabla)
        #print(len(campos))
        validacion = 0

        contador = 0
        for i in campos:
            if str(i) == str(campo):
                return contador
            else:
                contador += 1
                validacion = 1

        if validacion == 1:
            return -1
