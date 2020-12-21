lisa = [1,2,3,4,5]
li = ['a','ad','v']
lisa.extend(li)
print(lisa)


def ejecutar(self):
        gro = False
        #Obtener la lista de tablas
        tables = {}
        for tabla in self.table_expression:
            tables[tabla.id]  = tabla.alias
        
        results = []
        for col in self.select_list:
            
            
            
            res = col.ejecutar(tables)
            
            results.append(res)
        #return results

        conditions = ejecutar_conditions(tables,self.condition)
        
        for column in results:

            if isinstance(column,dict) and isinstance(column['valores'],list):
                
                column['valores'] = filtrar(column['valores'],conditions)
        
        #return results
            
        consulta = []
        fila = []
        for col in self.select_list:
            fila.append(col.alias)
        
        contador = 0
        for column in results:
            
            if fila[contador] == None:
                if isinstance(column,dict):
                    fila[contador]=column['columna'][0]['nombre']
                else:
                    fila[contador]="Funcion"
                
                
            
            contador = contador +1 

        consulta.append(fila)
        if gro:
            pass
        else:
            cantidad = 0
            for column in results:
                if isinstance(column,dict):
                    cantidad = len(column['valores'])
                    break
            
            for i in range(0,cantidad):
                fila = []
                
                for column in results:
                    if isinstance(column,dict):
                        if isinstance(column['valores'],list):
                            
                            fila.append(column['valores'][i])
                        else:
                            fila.append(column['valores'])
                    else:

                        fila.append(column)
                
                consulta.append(fila)
            
            print(consulta)
        return consulta

        
        