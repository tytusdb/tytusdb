import webbrowser
class Tabla():

    def write(self,entorno,tree):
        input = "<html>" + '\n' + "<head>" + '\n' + "<title>Reporte Gramatical</title>" + '\n' + "</head>" + '\n'
        input = input + "<body bgcolor=\"white\">" + '\n' + "<center><Font size=12 >" + "Tabla de simbolos" + "</Font></center>" + '\n'
        input = input + "<hr >" + '\n' + "<font color=black>" + '\n' + "<center>" + '\n'
        input = input + "<table " + '\n'
        input = input + "<TR bgcolor=silver>" + "\n"
        input = input + "<TH  style=\"font-size: 14px; width:15%; \"\" align=center>Tipo de Dato</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:20%; \" align=center>ID</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:15%; \" align=center>Ambito</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:15%; \" align=center>Valor</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:10%; \" align=center>Linea</TH>" + '\n'
        input = input + "<TH  style=\"font-size: 14px; width:10%; \" align=center>Columna</TH>" + '\n'


        for key in entorno.tableofSymbols:
            try:
                    s = entorno.tableofSymbols[key]
                    print("tableofSymbols con y= "+s.value)
                    print("tableofSymbols con id= "+s.id)
                    print("tableofSymbols con  ambito= "+s.ambito)
                  #  print("tableofSymbols con linea= "+s.line)
                   # print("tableofSymbols con col= "+s.column)
                    line=""  
                    column=""   
                    type1=""   
                    ambito  =""  
                    id1     =""                                               
                    try:                                                              
                        line=s.line
                    except:
                      pass
                    try:                                                              
                        column=s.column
                    except:
                      pass
                    try:                                                              
                         value=str(s.value)
                    except:
                         pass 
                    try:                                                              
                         ambito=str(s.ambito)
                    except:
                        pass 
                    try:                                                              
                        type1=str(s.type1)
                    except:
                         pass 
                    try:                                                              
                        id1=str(s.id)
                    except:
                         pass     
                    input = input + "<TR>"
                    input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + type1+ "</TD>" + '\n'
                    input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + id1+ "</TD>" + '\n'
                    input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + ambito+ "</TD>" + '\n'
                    input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + value+ "</TD>" + '\n'
                    input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + line+ "</TD>" + '\n'
                    input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + column+ "</TD>" + '\n'
                    input = input + "</TR>" + '\n'

                    input = input + "<TR>------------------------------------------------</TR>" + '\n'
            except:
                pass



        for sent in tree.sentencias:

            line=""  
            column=""    
            id=""  
            value="" 
            ambito=""   
            type1=""                                            
            try:                                                              
                line=str(s.line)
            except:
                pass
            try:                                                              
                column=str(s.column)
            except:
                pass
            try:                                                              
                id=str(sent.id)
            except:
                pass
            try:                                                              
                value=str(sent.value)
            except:
                pass   
            try:                                                              
                ambito=str(sent.ambito)
            except:
                pass 
            try:                                                              
                type1=str(sent.type)
            except:
                pass   
            print("sentvalue con y= "+id)
          
            input = input + "<TR>"
        #    input = input + "<TD style=\"font-size: 15px; color:white;\" color:white align=center>"+sent.getTipo()+"</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; color:black;\"  align=center>" + type1 + "</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + id+ "</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + ambito+ "</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + value+ "</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + line+ "</TD>" + '\n'
            input = input + "<TD style=\"font-size: 15px; ;\"  align=center>" + column + "</TD>" + '\n'
            input = input + "</TR>" + '\n'

        input = input + '\n' + "</center>" + '\n' + "</table>" + "</body>" + '\n' + "</html>"

        f = open ('Tabla.html','w')
        f.write(input)
        f.close()
        webbrowser.open_new_tab('Tabla.html')
