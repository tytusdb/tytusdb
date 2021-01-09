from Optimizacion._def import Def
from Optimizacion.asignacion import Asignacion
from Optimizacion.operacion import Operacion
from Optimizacion.literal import Literal

def optimizacion_uno(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            if len(def_instructions) >= 2:
                index = 0
                while index < len(def_instructions) - 1:
                    first_inst = def_instructions[index]
                    second_inst = def_instructions[index + 1]
                    if isinstance(first_inst, Asignacion) and isinstance(second_inst, Asignacion):
                        if first_inst.izquierda.toString() == second_inst.derecha.toString() and first_inst.derecha.toString() == second_inst.izquierda.toString():
                            dic = {
                                'type': 'Tipo 1',
                                'before': f"{first_inst.toString()}<BR>{second_inst.toString()}",
                                'opt': f"{first_inst.toString()}",
                                'line': f"{first_inst.linea}",
                            }
                            arbol.addOpt(dic)
                            def_instructions.remove(second_inst)
                            continue
                    index += 1
                            
def optimizacion_ocho(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            for def_inst in def_instructions:
                if isinstance(def_inst, Asignacion) and isinstance(def_inst.derecha, Operacion):
                    operacion = def_inst.derecha
                    if def_inst.izquierda.toString() == operacion.izquierda.toString() and operacion.operador == '+' and operacion.derecha and operacion.derecha.toString() == '0':
                        dic = {
                            'type': 'Tipo 8',
                            'before': f"{def_inst.toString()}",
                            'opt': f"#Se elimimo la instruccion",
                            'line': f"{def_inst.linea}",
                        }
                        arbol.addOpt(dic)
                        def_instructions.remove(def_inst)
                        
def optimizacion_nueve(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            for def_inst in def_instructions:
                if isinstance(def_inst, Asignacion) and isinstance(def_inst.derecha, Operacion):
                    operacion = def_inst.derecha
                    if def_inst.izquierda.toString() == operacion.izquierda.toString() and operacion.operador == '-' and operacion.derecha and operacion.derecha.toString() == '0':
                        dic = {
                            'type': 'Tipo 9',
                            'before': f"{def_inst.toString()}",
                            'opt': f"#Se elimimo la instruccion",
                            'line': f"{def_inst.linea}",
                        }
                        arbol.addOpt(dic)
                        def_instructions.remove(def_inst)

def optimizacion_diez(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            for def_inst in def_instructions:
                if isinstance(def_inst, Asignacion) and isinstance(def_inst.derecha, Operacion):
                    operacion = def_inst.derecha
                    if def_inst.izquierda.toString() == operacion.izquierda.toString() and operacion.operador == '*' and operacion.derecha and operacion.derecha.toString() == '1':
                        dic = {
                            'type': 'Tipo 10',
                            'before': f"{def_inst.toString()}",
                            'opt': f"#Se elimimo la instruccion",
                            'line': f"{def_inst.linea}",
                        }
                        arbol.addOpt(dic)
                        def_instructions.remove(def_inst)
                        
def optimizacion_once(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            for def_inst in def_instructions:
                if isinstance(def_inst, Asignacion) and isinstance(def_inst.derecha, Operacion):
                    operacion = def_inst.derecha
                    if def_inst.izquierda.toString() == operacion.izquierda.toString() and operacion.operador == '/' and operacion.derecha and operacion.derecha.toString() == '1':
                        dic = {
                            'type': 'Tipo 11',
                            'before': f"{def_inst.toString()}",
                            'opt': f"#Se elimimo la instruccion",
                            'line': f"{def_inst.linea}",
                        }
                        arbol.addOpt(dic)
                        def_instructions.remove(def_inst)
                        
def optimizacion_doce(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            for def_inst in def_instructions:
                if isinstance(def_inst, Asignacion) and isinstance(def_inst.derecha, Operacion):
                    operacion = def_inst.derecha
                    if def_inst.izquierda.toString() != operacion.izquierda.toString() and operacion.operador == '+' and operacion.derecha and operacion.derecha.toString() == '0':
                        dic = {
                            'type': 'Tipo 12',
                            'before': f"{def_inst.toString()}",
                            'opt': f"{def_inst.izquierda.toString()} = {operacion.izquierda.toString()}",
                            'line': f"{def_inst.linea}",
                        }
                        arbol.addOpt(dic)
                        literal = Literal(operacion.izquierda.toString(), operacion.linea)
                        def_inst.derecha = literal
                        
def optimizacion_trece(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            for def_inst in def_instructions:
                if isinstance(def_inst, Asignacion) and isinstance(def_inst.derecha, Operacion):
                    operacion = def_inst.derecha
                    if def_inst.izquierda.toString() != operacion.izquierda.toString() and operacion.operador == '-' and operacion.derecha and operacion.derecha.toString() == '0':
                        dic = {
                            'type': 'Tipo 13',
                            'before': f"{def_inst.toString()}",
                            'opt': f"{def_inst.izquierda.toString()} = {operacion.izquierda.toString()}",
                            'line': f"{def_inst.linea}",
                        }
                        arbol.addOpt(dic)
                        literal = Literal(operacion.izquierda.toString(), operacion.linea)
                        def_inst.derecha = literal

def optimizacion_catorce(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            for def_inst in def_instructions:
                if isinstance(def_inst, Asignacion) and isinstance(def_inst.derecha, Operacion):
                    operacion = def_inst.derecha
                    if def_inst.izquierda.toString() != operacion.izquierda.toString() and operacion.operador == '*' and operacion.derecha and operacion.derecha.toString() == '1':
                        dic = {
                            'type': 'Tipo 14',
                            'before': f"{def_inst.toString()}",
                            'opt': f"{def_inst.izquierda.toString()} = {operacion.izquierda.toString()}",
                            'line': f"{def_inst.linea}",
                        }
                        arbol.addOpt(dic)
                        literal = Literal(operacion.izquierda.toString(), operacion.linea)
                        def_inst.derecha = literal
                        
def optimizacion_quince(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            for def_inst in def_instructions:
                if isinstance(def_inst, Asignacion) and isinstance(def_inst.derecha, Operacion):
                    operacion = def_inst.derecha
                    if def_inst.izquierda.toString() != operacion.izquierda.toString() and operacion.operador == '/' and operacion.derecha and operacion.derecha.toString() == '1':
                        dic = {
                            'type': 'Tipo 15',
                            'before': f"{def_inst.toString()}",
                            'opt': f"{def_inst.izquierda.toString()} = {operacion.izquierda.toString()}",
                            'line': f"{def_inst.linea}",
                        }
                        arbol.addOpt(dic)
                        literal = Literal(operacion.izquierda.toString(), operacion.linea)
                        def_inst.derecha = literal
                        
def optimizacion_dieciseis(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            for def_inst in def_instructions:
                if isinstance(def_inst, Asignacion) and isinstance(def_inst.derecha, Operacion):
                    operacion = def_inst.derecha
                    if def_inst.izquierda.toString() != operacion.izquierda.toString() and operacion.operador == '*' and operacion.derecha and operacion.derecha.toString() == '2':
                        dic = {
                            'type': 'Tipo 16',
                            'before': f"{def_inst.toString()}",
                            'opt': f"{def_inst.izquierda.toString()} = {operacion.izquierda.toString()} + {operacion.izquierda.toString()}",
                            'line': f"{def_inst.linea}",
                        }
                        arbol.addOpt(dic)
                        literal = Literal(operacion.izquierda.toString(), operacion.linea)
                        nueva_operacion = Operacion(literal, '+', literal, operacion.linea)
                        index = def_instructions.index(def_inst)
                        def_instructions[index] = nueva_operacion
                        
def optimizacion_diecisiete(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            for def_inst in def_instructions:
                if isinstance(def_inst, Asignacion) and isinstance(def_inst.derecha, Operacion):
                    operacion = def_inst.derecha
                    if def_inst.izquierda.toString() != operacion.izquierda.toString() and operacion.operador == '*' and operacion.derecha and operacion.derecha.toString() == '0':
                        dic = {
                            'type': 'Tipo 17',
                            'before': f"{def_inst.toString()}",
                            'opt': f"{def_inst.izquierda.toString()} = {operacion.derecha.toString()}",
                            'line': f"{def_inst.linea}",
                        }
                        arbol.addOpt(dic)
                        literal = Literal(0, operacion.linea)
                        def_inst.derecha = literal
                        
def optimizacion_dieciocho(instrucciones, arbol):
    for inst in instrucciones:
        if isinstance(inst, Def):
            def_instructions = inst.instrucciones
            for def_inst in def_instructions:
                if isinstance(def_inst, Asignacion) and isinstance(def_inst.derecha, Operacion):
                    operacion = def_inst.derecha
                    if def_inst.izquierda.toString() != operacion.derecha.toString() and operacion.operador == '/' and operacion.derecha and operacion.izquierda.toString() == '0':
                        dic = {
                            'type': 'Tipo 18',
                            'before': f"{def_inst.toString()}",
                            'opt': f"{def_inst.izquierda.toString()} = {operacion.izquierda.toString()}",
                            'line': f"{def_inst.linea}",
                        }
                        arbol.addOpt(dic)
                        literal = Literal(0, operacion.linea)
                        def_inst.derecha = literal