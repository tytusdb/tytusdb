from analizer.abstract import instruction
import analizer.symbol.c3dSymbols as SymbolTable
from datetime import datetime

class Declaration(instruction.Instruction):
    def __init__(self,nombre,tipo,valor,row,column):
        instruction.Instruction.__init__(self,row,column)
        self.nombre=nombre
        self.tipo=tipo
        self.valor=valor
        self.row=row
        self.column=column
        self.classType=str(self.valor.__class__.__name__).casefold()
    def execute(self,environment):
        pass
    def generate3d(self,environment,instanciaAux):
        self.tipo=self.tipo[0].casefold()
        try:
            self.valor=self.valor.value
        except:
            pass
        
        if 'primitive'==self.classType:
            if self.valor == None:
                if 'integer' in self.tipo or 'bigint' in self.tipo:
                    self.valor=0
                elif 'numeric' in self.tipo or 'double precision' in self.tipo or 'money' in self.tipo or 'decimal' in self.tipo:
                    self.valor=0.0
                elif 'text' in self.tipo or 'varchar' in self.tipo or 'char' in self.tipo or 'varying' in self.tipo:
                    self.valor='\'\''
                elif 'boolean' in self.tipo:
                    self.valor=False
                elif 'timestamp' in self.tipo:
                    self.valor=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                elif 'date' in self.tipo:
                    self.valor=datetime.now().strftime("%Y-%m-%d")
                elif 'time' in self.tipo:
                    self.valor=datetime.now().strftime("%H:%M:%S")
                else:
                    pass
            else:
                if 'text' in self.tipo or 'varchar' in self.tipo or 'char' in self.tipo or 'varying' in self.tipo:
                    self.valor='\''+self.valor+'\''
                elif 'timestamp' in self.tipo:
                    self.valor='\''+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\''
                elif 'date' in self.tipo:
                    self.valor='\''+datetime.now().strftime("%Y-%m-%d")+'\''
                elif 'time' in self.tipo:
                    self.valor='\''+datetime.now().strftime("%H:%M:%S")+'\''
                else:
                    pass
            SymbolTable.add_symbol(self.nombre,self.tipo,self.valor,self.row,self.column,None)
            instanciaAux.addToCode(f'\t{self.nombre} =  {self.valor}')
        
        elif not self.classType == None:
            newTemp=self.valor.generate3d(environment,instanciaAux)
            SymbolTable.add_symbol(self.nombre,self.tipo,self.valor,self.row,self.column,None)
            instanciaAux.addToCode(f'\t{self.nombre} =  {newTemp}')
        