

class Registros:
    ListaRegistros=[]
    ListaRegistro=[]

    def insert(self, registro):
       
        try:
            self.ListaRegistro= []
            for x in registro.split(','):
                print("Dato a almacenar:" + x)
                self.ListaRegistro.append(x)
                print("dato almacenado:" )
                print(self.ListaRegistro)
                if self.ListaRegistros:
                                    
                    #for i in range(len(self.ListaRegistros)):
                        for j in range(len(self.ListaRegistros)):
                                        
                            llaveprimaria = self.ListaRegistro[0]
                            VerificarLlavePrimaria = self.ListaRegistros[j][0]
                            if llaveprimaria == VerificarLlavePrimaria:
                                self.ListaRegistro= []
                                print("llave primaria repetida" )
                                return 4 #llave primaria duplicada
                            else:
                                verificando = 1
                        if verificando == 1:
                                self.ListaRegistros.append(self.ListaRegistro)
                                print("registro guardado:")
                                print(self.ListaRegistros)
                                return 0 
                                                 
                else:
                    self.ListaRegistros.append(self.ListaRegistro)
                    print("registro guardado:" )
                    print(self.ListaRegistros)
                    return 0 #operacion exitosa
        except:
            
            return 1 #Error en la operacion

    def search(self,llave):
        try:
            
            for j in range(len(self.ListaRegistros)):
                                        
                llaveprimaria = self.ListaRegistro[0]
                if llaveprimaria == llave:
                    print(self.ListaRegistros[j])
                    return self.ListaRegistros[j]
                                                 
                else:
                    return False
        except:
            
            return 1 #Error en la operacion

    def delete(self, llave):
        try:
            
            for j in range(len(self.ListaRegistros)):
                                        
                llaveprimaria = self.ListaRegistro[0]
                if llaveprimaria == llave:
                    self.ListaRegistro.pop(j)
                    return 0 
                                                 
                else:
                    return False
        except:
            
            return 1 #Error en la operacion
    
    
    





