'''
export class Function extends Instruction{

    constructor(private id: string, public statment: Instruction, public parametros : Array<Instruction>, public tipo: string,line : number, column : number){
        super(line, column);
    }

    public execute(environment : Environment) {
        environment.guardarFuncion(this.id, this);
    }
}
'''
from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
form Instrucciones.TablaSimbolos.Tabla import Tabla

class Funcion(Instruccion):
    def __init__(self, id, tipo, campos, ids, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = id
        self.campos = campos
        self.ids = ids

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)