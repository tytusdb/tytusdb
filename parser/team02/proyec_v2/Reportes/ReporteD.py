import webbrowser
class ReporteD():
    def Mostrar(self,entorno,tree):
        input = '\n' + "</center>" + '\n' 

        input =  input +'\n' +"</body>" + '\n' + "</html>"
        f = open ('Tabla_Reporte.html', "a+")
        f.write(input)
        f.close()
        webbrowser.open_new_tab('Tabla_Reporte.html')

    def Abrir(self):
        f = open ('Tabla_Reporte.html', "w")

        input = "<html>" + '\n' + "<head>" + '\n' + "<title>Reporte Gramatical</title>" + '\n' + "</head>" + '\n'
        input = input + "<body bgcolor=\"white\">" + '\n' + "<center><Font size=12 >" + "DATABASE CONSOLE " + "</Font></center>" + '\n'
        input = input + " <center>" + '\n'
      
       # input = input + "<TH  style=\"font-size: 14px; width:15%; \"\" align=center>Tipo de Dato</TH>" + '\n'
        
        print("table: ")
        f.write(input)
        f.close()
  

    def sentencia_titulo(self,sentencia):
        input =  "<TR bgcolor=silver>" + "\n"
       
        input = input + "<TR>"
        input = input + "<TD style=\"font-size: 15px; color:black;\"  align=center> " + sentencia + "</TD>" + '\n'
        input = input + "</TR>" + '\n'
        input = input + "<TR>"    
        input = input + "</TR>"    

        f = open ('Tabla_Reporte.html', "a+")
        f.write(input)
        f.close()


    def write(self,idtabla,entorno,tree):
     
        print("table: ")      
        
        input =  "<table " + '\n'

        input = input + "<TR bgcolor=silver>" + "\n"
        try:
                for Expres in tree.nodos:
                    print("112e "+Expres.id)      
                    if Expres.id==idtabla : 
                                    print("114z "+idtabla)     
                
                            #if(sent.) Expres2 in sent:
                                
                                    input = input + "<TR>" 
                                    for key in Expres.sentencias:
                                        print("g7 ")     

                                        try:
                                            y= {} 
                                            y = key.getValor(entorno,tree) 
                                            print(" salio de obtener datos y= ",str(y))
                                            input = input + "<TD style=\"font-size: 15px; border: 1px solid black;color:black;\"  align=center>" +str(y) + "</TD>" + '\n'
                                
                                        except:
                                            input = input + "<TD style=\"font-size: 15px; color:black;\"  align=center></TD>" + '\n'
                                            print(" salio de obtener hh")

                                            pass
                                    input = input + "</TR>" + '\n'

        except:
                                 print(" salio con eeror en for")
         
        print("112ello")          
        print("salio de tree")  
        input = input + "</TR>" + "\n"
        input = input + '\n' +  "</table>" 

        f = open ('Tabla_Reporte.html', "a+")
        f.write(input)
        f.close()




    def write1(self,node,nodel,sentencia,entorno,tree):
            input =  "<table " + '\n'
            input = input + "<TR bgcolor=silver>" + "\n"
        # input = input + "<TH  style=\"font-size: 14px; width:15%; \"\" align=center>Tipo de Dato</TH>" + '\n'
            
            print("table: ")      

        
                    #if(sent.) Expres2 in sent:
            input = input + "<TR>"
            input = input + "<TD style=\"font-size: 15px; color:black;\"  align=center> " + sentencia + "</TD>" + '\n'
            
            input = input + "<TR>"
            k=0
            for key28 in nodel:                
                    input = input + "</TR>" + '\n'
                    for key2 in node:
                            
                            
                            print("g7 ",key2)     

                            try:
                                input = input +"<TD style=\"font-size: 15px; border: 1px solid black;color:black;\"  align=center>" +key2[k] + "</TD>" + '\n'
                            
                    
                            except:
                                input = input + "<TD style=\"font-size: 15px; color:black;\"  align=center></TD>" + '\n'
                    
                                pass
                    input = input + "</TR>" + '\n'         
                    k=k+1    
                    
            
            input = input + "</TR>" + "\n"

            input = input + '\n' +  "</table>" 

            print("112ello")          
            print("salio de tree")      

            f = open ('Tabla_Reporte.html', "a+")
            f.write(input)
            f.close()
