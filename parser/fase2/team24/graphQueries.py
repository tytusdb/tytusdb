import graphviz as gr
import classesQuerys as cq

def graphTree(queries):
    g = gr.Digraph()
    g.node('queries','Lista de Queries')
    for inst in queries:
        g.node(str(hash(inst)),'Query')
        g.edge('queries',str(hash(inst)))
        graphSelect(inst,g)

    g.render('tree.svg',view=True)

def graphSelect(query,graph):
    hashstr = str(hash(query))
    #Graficando el distinct
    graph.node(hashstr+'distinct','Distinct')
    graph.node(hashstr+'distinctTF',str(query.distinct))
    graph.edge(hashstr,hashstr+'distinct')
    graph.edge(hashstr+'distinct',hashstr+'distinctTF')
    #Graficando el Select_List
    graph.node(hashstr+'select_list','Select List')
    graph.edge(hashstr,hashstr+'select_list')
    for col in query.select_list:
        colhash = str(hash(col))
        #Si la columna es de tipo ID
        if  isinstance(col,cq.exp_id):
            graph.node(colhash,'ID column')
            graph.node(colhash+'val','Val : '+col.val)
            graph.node(colhash+'table','Table : '+str(col.table))
            graph.edge(hashstr+'select_list',colhash)
            graph.edge(colhash,colhash+'val')
            graph.edge(colhash,colhash+'table')
            graph.node(colhash+'alias','Alias: '+str(col.alias))
            graph.edge(colhash,colhash+'alias')
        #Si la columna es una funcion matemática
        # o trigonométrica
        if isinstance(col,cq.column_mathtrig):
            graph.node(colhash,'Function column: '+str(col.__class__.__name__))
            graph.edge(hashstr+'select_list',colhash)
            ##
            #Escribimos dependiendo de los atributos
            if hasattr(col,'exp'):
                graph.node(colhash+'exp','Exp : '+str(col.exp.val))
                graph.edge(colhash,colhash+'exp')

            if hasattr(col,'exp1'):
                graph.node(colhash+'exp1','Exp1 : '+str(col.exp1.val))
                graph.edge(colhash,colhash+'exp1')

            if hasattr(col,'exp2'):
                graph.node(colhash+'exp2','Exp2 : '+str(col.exp2.val))
                graph.edge(colhash,colhash+'exp2')

            if hasattr(col,'exp3'):
                graph.node(colhash+'exp3','Exp3 : '+str(col.exp3.val))
                graph.edge(colhash,colhash+'exp3')

            if hasattr(col,'exp4'):
                graph.node(colhash+'exp4','Exp4 : '+str(col.exp4.val))
                graph.edge(colhash,colhash+'exp4')

            ##
            graph.node(colhash+'alias','Alias: '+str(col.alias))
            graph.edge(colhash,colhash+'alias')
        
        #Si la columna es una funcion 
        # de utilidad
        if isinstance(col,cq.column_function):
            graph.node(colhash,'Utility column: '+str(col.__class__.__name__))
            graph.edge(hashstr+'select_list',colhash)
            ##
            #Escribimos dependiendo de los atributos
            if hasattr(col,'exp'):
                graph.node(colhash+'exp','Exp : '+str(col.exp.val))
                graph.edge(colhash,colhash+'exp')

            if hasattr(col,'min'):
                graph.node(colhash+'min','From : '+str(col.min))
                graph.edge(colhash,colhash+'min')

            if hasattr(col,'max'):
                graph.node(colhash+'max','To : '+str(col.max))
                graph.edge(colhash,colhash+'max')

            if hasattr(col,'type'):
                graph.node(colhash+'type','Type : '+str(col.type))
                graph.edge(colhash,colhash+'type')

            if hasattr(col,'lexps'):
                graph.node(colhash+'lexps','Lista de expresiones')
                graph.edge(colhash,colhash+'lexps')
                lexps = col.lexps
                graph_exps(lexps,graph,'lexps',colhash)

            if hasattr(col,'union'):
                graph.node(colhash+'union','Condición booleana: '+str(col.union))
                graph.edge(colhash,colhash+'union')        

            ##
            graph.node(colhash+'alias','Alias: '+str(col.alias))
            graph.edge(colhash,colhash+'alias')


def graph_exps(list,graph,text,hashstr):
    for col in list:
        colhash = str(hash(col))
        #Si la columna es de tipo ID
        if  isinstance(col,cq.exp_id):
            graph.node(colhash,'ID column')
            graph.node(colhash+'val','Val : '+col.val)
            graph.node(colhash+'table','Table : '+str(col.table))
            graph.edge(hashstr+text,colhash)
            graph.edge(colhash,colhash+'val')
            graph.edge(colhash,colhash+'table')
            graph.node(colhash+'alias','Alias: '+str(col.alias))
            graph.edge(colhash,colhash+'alias')
        #Si la columna es una funcion matemática
        # o trigonométrica
        if isinstance(col,cq.column_mathtrig):
            graph.node(colhash,'Function column: '+str(col.__class__.__name__))
            graph.edge(hashstr+text,colhash)
            ##
            #Escribimos dependiendo de los atributos
            if hasattr(col,'exp'):
                graph.node(colhash+'exp','Exp : '+str(col.exp.val))
                graph.edge(colhash,colhash+'exp')

            if hasattr(col,'exp1'):
                graph.node(colhash+'exp1','Exp1 : '+str(col.exp1.val))
                graph.edge(colhash,colhash+'exp1')

            if hasattr(col,'exp2'):
                graph.node(colhash+'exp2','Exp2 : '+str(col.exp2.val))
                graph.edge(colhash,colhash+'exp2')

            if hasattr(col,'exp3'):
                graph.node(colhash+'exp3','Exp3 : '+str(col.exp3.val))
                graph.edge(colhash,colhash+'exp3')

            if hasattr(col,'exp4'):
                graph.node(colhash+'exp4','Exp4 : '+str(col.exp4.val))
                graph.edge(colhash,colhash+'exp4')

            ##
            graph.node(colhash+'alias','Alias: '+str(col.alias))
            graph.edge(colhash,colhash+'alias')
        
        #Si la columna es una funcion 
        # de utilidad
        if isinstance(col,cq.column_mathtrig):
            graph.node(colhash,'Utility column: '+str(col.__class__.__name__))
            graph.edge(hashstr+text,colhash)
            ##
            #Escribimos dependiendo de los atributos
            if hasattr(col,'exp'):
                graph.node(colhash+'exp','Exp : '+str(col.exp.val))
                graph.edge(colhash,colhash+'exp')

            if hasattr(col,'min'):
                graph.node(colhash+'min','From : '+str(col.min))
                graph.edge(colhash,colhash+'min')

            if hasattr(col,'max'):
                graph.node(colhash+'max','To : '+str(col.max))
                graph.edge(colhash,colhash+'max')

            if hasattr(col,'type'):
                graph.node(colhash+'type','Type : '+str(col.type))
                graph.edge(colhash,colhash+'type')

            if hasattr(col,'lexps'):
                graph.node(colhash+'lexps','Lista de exp')
                graph.edge(colhash,colhash+'lexps')
                lexps = col.lexps
                graph_exps(lexps,graph,'lexps',hashstr)

            if hasattr(col,'union'):
                graph.node(colhash+'union','Condición booleana: '+str(col.union))
                graph.edge(colhash,colhash+'union')
            ##
        if isinstance(col,cq.exp_num):
            #Si es una expresión numérica
            graph.node(colhash,'Number: '+str(col.val))
            graph.edge(hashstr+text,colhash)

        if isinstance(col,cq.exp_text):
            #Si es una expresión numérica
            graph.node(colhash,'Number: '+str(col.val))
            graph.edge(hashstr+text,colhash)

