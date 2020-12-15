class Inicio: 
     def __init__(self,instrucciones):
	     self.instrucciones = instrucciones
     
class Instrucciones: 
     def __init__(self,instrucciones, newline, instrucciones2):
	     self.instrucciones = instrucciones
	     self.newline = newline
	     self.instrucciones2 = instrucciones2


class Instruccion: 
       def __init__(self,ddlx):
	          self.ddlx = ddlx
     
class Instruccion2: 
          def __init__(self,dml):
	           self.dml = dml

class Dll: 
     def __init__(self,sentencia_create):
	     self.sentencia_create = sentencia_create

class Dll2: 
     def __init__(self,sentencia_alter):
	     self.sentencia_alter = sentencia_alter
     
class Dll3: 
     def __init__(self,sentencia_drop):
	     self.sentencia_drop = sentencia_drop
     
class Dll4: 
     def __init__(self,sentencia_truncate):
	     self.sentencia_truncate = sentencia_truncate
     

class Dml: 
     def __init__(self,sentencia_insert):
	     self.sentencia_insert = sentencia_insert
     
class Dml2: 
     def __init__(self,sentencia_update):
	     self.sentencia_update = sentencia_update
     
class Dml3: 
     def __init__(self,sentencia_delete):
	     self.sentencia_delete = sentencia_delete
     
class Dml4: 
     def __init__(self,sentencia_select):
	     self.sentencia_select = sentencia_select
     
class Dml5: 
     def __init__(self,sentencia_show):
	     self.sentencia_show = sentencia_show
     
class Sentencia:
     ' Clase implementada para poderla utilizarla como interfaz'



#------------------- Sentencias DDL ---------------------
#CREAR
class Create(Sentencia):
     'Clase implementa sentencia Create'
     def __init__(self,create,create_count):
          self.create=create
          self.create_count=create_count

class Create2(Sentencia):
     'Clase implementa sentencia Create'
     def __init__(self,replace,create_count):
          self.replace=replace
          self.create_count=create_count
          

class CreateCount(Sentencia):
     def __init__(self,database,if_not,pyc):
          self.database=database
          self.if_not=if_not
          self.pyc=pyc

class CreateCount2(Sentencia):
     def __init__(self,table,if_not,part1,col_tabla, part2,fin_tabla):
          self.table=table
          self.if_not=if_not
          self.part1 =part1
          self.col_tabla =col_tabla
          self.part2=part2
          self.fin_tabla=fin_tabla
class CreateCount3(Sentencia):
     def __init__ (self, type, valor, _as, _enum, par1, lista_insertar, par2 ,pyc):
          self.type=type
          self.valor=valor
          self._as=_as
          self._enum=_enum
          self.par1=par1
          self.lista_insertar=lista_insertar
          self.par2=par2
          self.pyc=pyc
class FinTabla(Sentencia):
     def __init__(self,inherits, par1, identificador, par2, pyc):
          self.inherits=inherits
          self.par1=par1
          self.identificador=identificador
          self.par2=par2
          self.pyc=pyc
class FinTabla2(Sentencia):
     def __init__(self,py):
          self.py=py
class IfNot(Sentencia):
     def __init__(self,_if, _not,_exists, identificador):
          self._if=_if
          self._not=_not
          self._exists=_exists
          self.identificador=identificador
    
class IfNot2(Sentencia):
     def __init__(self,identificador):
          self.identificador=identificador

class IfNot3(Sentencia):
     def __init__(self,_if, _not, _exists , identificador , _owner , igual , valor):
          self._if=_if
          self._not=_not
          self._exists=_exists
          self.identificador=identificador
          self._owner=_owner
          self.igual=igual
          self.valor=valor
class IfNot4(Sentencia):
     def __init__(self,identificador, _owner, valor):
           self.identificador=identificador
           self._owner=_owner
           self.valor=valor
class IfNot5(Sentencia):
     def __init__(self,_if, _not ,  _exists, identificador, _mode ,  igual, valor):
          self._if=_if
          self._not=_not
          self._exists=_exists
          self.identificador=identificador
          self._mode=_mode
          self.igual=igual
          self.valor=valor
class IfNot6(Sentencia):
     def __init__(self,dentificador, _mode, igual, valor):
          self.dentificador=dentificador
          self._mode=_mode
          self.igual=igual
          self.valor=valor
class ColTabla(Sentencia):
     def __init__(self, col_tabla , coma ,  identificador , tipo , propiedades):
          self.col_tabla=col_tabla
          self.coma=coma
          self.identificador=identificador
          self.tipo=tipo
          self.propiedades=propiedades
class ColTabla2(Sentencia):
     def __init__(self,col_tabla , coma , identificador , tipo):
          self.col_tabla=col_tabla
          self.coma=coma
          self.identificador=identificador
          self.tipo =tipo
class ColTabla3(Sentencia):
     def __init__(self,dentificador, tipo, propiedades):
          self.dentificador=dentificador
          self.tipo=tipo
          self.propiedades=propiedades

class ColTabla4(Sentencia):
     def __init__(self,identificador , tipo):
          self.identificador=identificador
          self.tipo=tipo


class ColTabla5(Sentencia):
     def __init__(self,_foreing, _key, lista_id, _references, identificador):
          self._foreing=_foreing
          self._key=_key
          self.lista_id=lista_id
          self._references=_references
          self.identificador=identificador

class ColTabla6(Sentencia):
     def __init__(self,col_tabla, coma, _primary, _key, lista_id):
          self.col_tabla=col_tabla
          self.coma=coma
          self._primary=_primary
          self._key=_key
          self.lista_id=lista_id

class Propiedades(Sentencia): 
     def __init__(self,_null  , propiedades  ):
	     self._null = _null
	     self.propiedades = propiedades
     
class Propiedades2(Sentencia): 
     def __init__(self,_not  , _null  , propiedades  ):
	     self._not = _not
	     self._null = _null
	     self.propiedades = propiedades
     
class Propieades3(Sentencia): 
     def __init__(self,_identity  , propiedades  ):
	     self._identity = _identity
	     self.propiedades = propiedades
     

class Propieades4(Sentencia): 
     def __init__(self,_primary , _key , propiedades ):
	     self._primary = _primary
	     self._key = _key
	     self.propiedades = propiedades

class Propiedades5(Sentencia): 
     def __init__(self,_null ):
	     self._null = _null
     
class Propiedades6(Sentencia): 
     def __init__(self,_not , _null ):
	     self._not = _not
	     self._null = _null
     
class Propiedades7(Sentencia): 
     def __init__(self,_identity ):
	     self._identity = _identity
     
class Propiedades8(Sentencia): 
     def __init__(self,_primary , _key ):
	     self._primary = _primary
	     self._key = _key
     
class Tipo(Sentencia): 
     def __init__(self,_smallint ):
	     self._smallint = _smallint
     
class Tipo2(Sentencia): 
     def __init__(self,_integer ):
	     self._integer = _integer
     
class Tipo3(Sentencia): 
     def __init__(self,_bigint ):
	     self._bigint = _bigint
     
class Tipo4(Sentencia): 
     def __init__(self,_decimal ):
	     self._decimal = _decimal
     
class Tipo5(Sentencia): 
     def __init__(self,_numeric ):
	     self._numeric = _numeric
     
class Tipo6(Sentencia): 
     def __init__(self,_real ):
	     self._real = _real

class Tipo7(Sentencia): 
     def __init__(self,_double ):
	     self._double = _double
     
class Tipo8(Sentencia): 
     def __init__(self,_money ):
	     self._money = _money
     
class Tipo9(Sentencia): 
     def __init__(self,_character ):
	     self._character = _character

class Tipo10(Sentencia): 
     def __init__(self,_varaying , par1 , _num , par2 ):
	     self._varaying = _varaying
	     self.par1 = par1
	     self._num = _num
	     self.par2 = par2
     
class Tipo11(Sentencia): 
     def __init__(self,__varchar , _par1 , _num , par2 ):
	     self.__varchar = __varchar
	     self._par1 = _par1
	     self._num = _num
	     self.par2 = par2
     
class Tipo12(Sentencia): 
     def __init__(self,_character , par1 , _num , _par2 ):
	     self._character = _character
	     self.par1 = par1
	     self._num = _num
	     self._par2 = _par2

class Tipo13(Sentencia): 
     def __init__(self,_char , par1 , _num , par2 ):
	     self._char = _char
	     self.par1 = par1
	     self._num = _num
	     self.par2 = par2
     
class Tipo14(Sentencia): 
     def __init__(self,_text ):
	     self._text = _text
     
class Tipo15(Sentencia): 
     def __init__(self,_date ):
	     self._date = _date
     
class Tipo16(Sentencia): 
     def __init__(self,_boolean ):
	     self._boolean = _boolean
     
class Tipo17(Sentencia): 
     def __init__(self,_int ):
	     self._int = _int

class Tipo18(Sentencia): 
     def __init__(self,identificador ):
	     self.identificador = identificador
     

#ALTER
class SetenciaAlter(Sentencia): 
     def __init__(self,_alter , alter_objeto ) :
	     self._alter = _alter
	     self.alter_objeto = alter_objeto
     
class AlterObjeto(Sentencia): 
     def __init__(self,_table , identificador , alter_cont , pycx):
	     self._table = _table
	     self.identificador = identificador
	     self.alter_cont = alter_cont
	     self.pycx = pycx
     

         
class AlterObjeto2(Sentencia): 
     def __init__(self,database_, identificador, rename_ , to_ , identificador2, pyc):
	     self.database_ = database_
	     self.identificador = identificador
	     self.rename_ = rename_
	     self.to_ = to_
	     self.identificador2 = identificador2
	     self.pyc = pyc
     



class AlterObjecto3(Sentencia): 
     def __init__(self,_database , identificador , _owner , _to , identificador2 , pyc ) :
	     self._database = _database
	     self.identificador = identificador
	     self._owner = _owner
	     self._to = _to
	     self.identificador = identificador2
	     self.pyc = pyc
     
class AlterCont(Sentencia): 
     def __init__(self,_add , con_add ):
	     self._add = _add
	     self.con_add = con_add
class AlterCont2(Sentencia): 
     def __init__(self,_drop ,con_drop ):
	     self._drop = _drop
	     self.con_drop = con_drop
     
class AlterCont3(Sentencia): 
     def __init__(self,_rename ,con_rename ):
	     self._rename = _rename
	     self.con_rename = con_rename
     
class AlterCont4(Sentencia): 
     def __init__(self,_alter ,con_alter ):
	     self._alter = _alter
	     self.con_alter = con_alter

class ConAdd(Sentencia): 
     def __init__(self, _column, identificador, tipo):
	     self._column =  _column
	     self.identificador = identificador
	     self.tipo = tipo

class ConAdd2(Sentencia): 
     def __init__(self, _check, par1, valor, diferente, vacio, par2):
	     self._check =  _check
	     self.par1 = par1
	     self.valor = valor
	     self.diferente = diferente
	     self.vacio = vacio
	     self.par2 = par2
     
class ConAdd3(Sentencia): 
     def __init__(self, _foreing, key, par1, identificador, par2, references, identificador2):
	     self._foreing =  _foreing
	     self.key = key
	     self.par1 = par1
	     self.identificador = identificador
	     self.par2 = par2
	     self.references = references
	     self.identificador2 = identificador2

class ConDrop(Sentencia): 
     def __init__(self, _column, identificador):
	     self._column =  _column
	     self.identificador = identificador
     
class ConDrop2(Sentencia): 
     def __init__(self, constraint_ , identificadorx):
          self.constraint_ =  constraint_
          self.identificadorx = identificadorx      
      
class DeleteExp(Sentencia):


 class ConAlter(Sentencia): 
      def __init__(self,_column, identificador, _set, _not, _null):
          self._column =  _column
          self.identificador = identificador
          self._set = _set
          self._not = _not
          self._null = _null
      
  #Sentencia DROP    
class Drop(Sentencia): 
     def __init__(self, _drop, objeto, if_exist, pyc):
          self._drop =  _drop
          self.objeto = objeto
          self.if_exist = if_exist
          self.pyc = pyc
     
class IfExist(Sentencia): 
     def __init__(self, _if, _exists, identificador):
          self._if =  _if
          self._exists = _exists
          self.identificador = identificador
     
class IfExist2(Sentencia): 
     def __init__(self, identificador):
          self.identifica =  identificador
     
class DeleteExp2(Sentencia):

 class Objeto(Sentencia): 
      def __init__(self, _table):
          self._table =  _table



 class Objeto2(Sentencia): 
      def __init__(self, _database):
          self._database =  _database
      
 #TRUNCATE

 class Truncate(Sentencia): 
      def __init__(self, _truncate, _table, identificador, pyc):
          self._truncate =  _truncate
          self._table = _table
          self.identificador = identificador
          self.pyc = pyc
      
#-------------DML -------------------
#INSERT
class INSERTAR(Sentencia): 
     def __init__(self, _insert, _into, identificador, insert_cont, pyc):
          self._insert =  _insert
          self._into = _into
          self.identificador = identificador
          self.insert_cont = insert_cont
          self.pyc = pyc
     
class InsertarCont(Sentencia): 
     def __init__(self, _values, par1, lista_insertar, par2):
          self._values =  _values
          self.par1 = par1
          self.lista_insertar = lista_insertar
          self.par2 = par2
class InsertarCont2(Sentencia): 
     def __init__(self, par1, lista_campos, par2, _values, par12, lista_insertar, par22):
          self.par1 =  par1
          self.lista_campos = lista_campos
          self.par2 = par2
          self._values = _values
          self.par12 = par12
          self.lista_insertar = lista_insertar
          self.par22 = par22
     
class ListaCampos(Sentencia): 
     def __init__(self, lista_campos, coma, identificador):
          self.lista_campos =  lista_campos
          self.coma = coma
          self.identificador = identificador
     
class Valor(Sentencia): 
     def __init__(self, _num):
          self._num =  _num

class Valor2(Sentencia): 
     def __init__(self, cadena):
          self.cadena =  cadena
     
class Valor3(Sentencia): 
     def __init__(self, pdecimal):
          self.pdecimal =  pdecimal
     
class Valor4(Sentencia): 
     def __init__(self, identificador):
          self.identificador =  identificador
     
class Valor5(Sentencia): 
     def __init__(self, cadenacaracter):
          self.cadenacaracter =  cadenacaracter
     
class Valor6(Sentencia): 
     def __init__(self, _substring, par1, valor, coma, valor1, coma2, valor3, par2):
          self._substring =  _substring
          self.par1 = par1
          self.valor = valor
          self.coma = coma
          self.valor1 = valor1
          self.coma2 = coma2
          self.valor3 = valor3
          self.par2 = par2
     
class ListaInsertar(Sentencia): 
     def __init__(self, lista_insertar, coma, operacion_aritmetica):
          self.lista_insertar =  lista_insertar
          self.coma = coma
          self.operacion_aritmetica = operacion_aritmetica
     
class ListaInsertar2(Sentencia): 
     def __init__(self, operacion_aritmetica):
          self.operacion_aritmetica =  operacion_aritmetica
     
#Update
class Update(Sentencia): 
     def __init__(self, _update, identificador, _set, identificador2, igual, operacion_aritmetica, condicion):
          self._update =  _update
          self.identificador = identificador
          self._set = _set
          self.identificador2 = identificador2
          self.igual = igual
          self.operacion_aritmetica = operacion_aritmetica
          self.condicion = condicion
#Delete

class Delete(Sentencia): 
     def __init__(self, _delete, _from, delete_cont, condicion):
          self._delete =  _delete
          self._from = _from
          self.delete_cont = delete_cont
          self.condicion = condicion
     
class DeleteCont(Sentencia): 
     def __init__(self, _only, identificador):
          self._only =  _only
          self.identificador = identificador
     
class DeleteCont2(Sentencia): 
     def __init__(self, _only, identificador, por):
          self._only =  _only
          self.identificador = identificador
          self.por = por

class DeleteCont3(Sentencia): 
     def __init__(self, identificador, por):
          self.identificador =  identificador
          self.por = por
     
class DeleteCont4(Sentencia): 
     def __init__(self, identificador):
          self.identificador =  identificador
     

#select
class Select(Sentencia): 
     def __init__(self, _select, opciones_fecha):
          self._select =  _select
          self.opciones_fecha = opciones_fecha
     
class Select2(Sentencia): 
     def __init__(self, _select, select_cont, _from, lista_from, condicion_cont):
          self._select =  _select
          self.select_cont = select_cont
          self._from = _from
          self.lista_from = lista_from
          self.condicion_cont = condicion_cont

class OrderBy(Sentencia): 
     def __init__(self,order_, _by, identificador, opcion_order, order_by):
	     self.order_ = order_
	     self._by = _by
	     self.identificador = identificador
	     self.opcion_order = opcion_order
	     self.order_by = order_by
     
class OrderBy2(Sentencia): 
     def __init__(self, condicion_cont):
	     self.condicion_cont =  condicion_cont
     
class OrderBy3(Sentencia): 
     def __init__(self,_limit, operacion_aritmetica, orber_by):
	     self._limit = _limit
	     self.operacion_aritmetica = operacion_aritmetica
	     self.orber_by = orber_by
     
class OrderBy4(Sentencia): 
     def __init__(self,_offset, operacion_aritmetica, orderb_by):
	     self._offset = _offset
	     self.operacion_aritmetica = operacion_aritmetica
	     self.orderb_by = orderb_by
class OpcionOrder(Sentencia): 
     def __init__(self,_asc):
	     self._asc = _asc
     
class OpcionOrder2(Sentencia): 
     def __init__(self,_desc):
	     self._desc = _desc

class CondicionCont(Sentencia): 
     def __init__(self,_where, operacion_logica, fin_select):
          self._where = _where
          self.operacion_logica = operacion_logica
          self.fin_select = fin_select
class CondicionCont2(Sentencia): 
     def __init__(self,_where, operacion_relacional, fin_select):
          self._where = _where
          self.operacion_relacional = operacion_relacional
          self.fin_select = fin_select
class CondicionCont3(Sentencia): 
     def __init__(self,_where, operacion_loigca, _group, _by, identificador2, fin_select):
	     self._where = _where
	     self.operacion_loigca = operacion_loigca
	     self._group = _group
	     self._by = _by
	     self.identificador2 = identificador2
	     self.fin_select = fin_select
class CondicionCount4(Sentencia): 
     def __init__(self,_group, _by, lista_id, fin_select):
	     self._group = _group
	     self._by = _by
	     self.lista_id = lista_id
	     self.fin_select = fin_select
     
class CondicionCount5(Sentencia): 
     def __init__(self,_group, _by, _lista_id, _having, operacion_logica, fin_select):
	     self._group = _group
	     self._by = _by
	     self._lista_id = _lista_id
	     self._having = _having
	     self.operacion_logica = operacion_logica
	     self.fin_select = fin_select

class CondicionCount6(Sentencia): 
     def __init__(self,_where, _exists, par1, sentencia_select, par2, fin_select):
	     self._where = _where
	     self._exists = _exists
	     self.par1 = par1
	     self.sentencia_select = sentencia_select
	     self.par2 = par2
	     self.fin_select = fin_select

class CondicionCount7(Sentencia): 
     def __init__(self,_where, operacion_aritmetica, _in, par1, sentencia_select, par2, fin_select):
	     self._where = _where
	     self.operacion_aritmetica = operacion_aritmetica
	     self._in = _in
	     self.par1 = par1
	     self.sentencia_select = sentencia_select
	     self.par2 = par2
	     self.fin_select = fin_select
class CondicionCount8(Sentencia): 
     def __init__(self,_where, operacion_aritmetica, _not, _in, par1, sentencia_select, par2, fin_select):
	     self._where = _where
	     self.operacion_aritmetica = operacion_aritmetica
	     self._not = _not
	     self._in = _in
	     self.par1 = par1
	     self.sentencia_select = sentencia_select
	     self.par2 = par2
	     self.fin_select = fin_select

     
class CondicionCount9(Sentencia): 
     def __init__(self,fin_select):
	     self.fin_select = fin_select
       
class FinSelect(Sentencia): 
     def __init__(self,order_by):
	     self.order_by = order_by
class FinSelect2(Sentencia): 
     def __init__(self, pyc):
	     self.pyc =  pyc
     
class FinSelect3(Sentencia): 
     def __init__(self,_union, sentencia_select):
	     self._union = _union
	     self.sentencia_select = sentencia_select
     
class FinSelect4(Sentencia): 
     def __init__(self,_intersect, sentencia_select):
	     self._intersect = _intersect
	     self.sentencia_select = sentencia_select
     
class FinSelect5(Sentencia): 
     def __init__(self,_except, sentencia_select):
	     self._except = _except
	     self.sentencia_select = sentencia_select

class ListaFrom(Sentencia): 
     def __init__(self,lista_from, coma, identificador, _as, identificador2):
	     self.lista_from = lista_from
	     self.coma = coma
	     self.identificador = identificador
	     self._as = _as
	     self.identificador2 = identificador2

class ListaFrom2(Sentencia): 
     def __init__(self,lista_from, coma, identificador):
	     self.lista_from = lista_from
	     self.coma = coma
	     self.identificador = identificador
     
class ListaFrom3(Sentencia): 
     def __init__(self,identificador, _as, identificador2):
	     self.identificador = identificador
	     self._as = _as
	     self.identificador2 = identificador2    
class ListaFrom4(Sentencia): 
     def __init__(self, identificador):
	     self.identificador =  identificador
     
class ListaFrom5(Sentencia): 
     def __init__(self,hacer_join):
	     self.hacer_join = hacer_join
     

class ListaFrom6(Sentencia): 
     def __init__(self,par1, sentencia_select, par2, _as, identificador):
	     self.par1 = par1
	     self.sentencia_select = sentencia_select
	     self.par2 = par2
	     self._as = _as
	     self.identificador = identificador
     
class ListaFrom7(Sentencia): 
     def __init__(self,par1, sentencia_select, par2):
	     self.par1 = par1
	     self.sentencia_select = sentencia_select
	     self.par2 = par2
     
class TipoJoin(Sentencia): 
     def __init__(self, _inner):
	     self._inner =  _inner
     
class TipoJoin2(Sentencia): 
     def __init__(self, _left):
	     self._left =  _left
     
class TipoJoin3(Sentencia): 
     def __init__(self,_right):
	     self._right = _right
     
class TipoJoin4(Sentencia): 
     def __init__(self, _full):
	     self._full =  _full
     
class TipoJoin5(Sentencia): 
     def __init__(self, _outer):
	     self._outer =  _outer
     
class HacerJoin(Sentencia): 
     def __init__(self,identificador, tipo_join, join, identificador2, _on, operacion_logica):
	     self.identificador = identificador
	     self.tipo_join = tipo_join
	     self.join = join
	     self.identificador2 = identificador2
	     self._on = _on
	     self.operacion_logica = operacion_logica
     
class HacerJoin2(Sentencia): 
     def __init__(self,identificador, tipo_join, _join, identificador2):
	     self.identificador = identificador
	     self.tipo_join = tipo_join
	     self._join = _join
	     self.identificador2 = identificador2
class SelectCont(Sentencia): 
     def __init__(self,por):
	     self.por = por
     
class SelectCont2(Sentencia): 
     def __init__(self,_distinct, lista_id):
	     self._distinct = _distinct
	     self.lista_id = lista_id
     
class SelectCont3(Sentencia): 
     def __init__(self,lista_id):
	     self.lista_id = lista_id
     
class SelectCont4(Sentencia): 
     def __init__(self,sen_case):
	     self.sen_case = sen_case

class SenCase(Sentencia): 
     def __init__(self, _case, case_when):
	     self. _case =  _case
	     self.case_when = case_when

class CaseWhen(Sentencia): 
     def __init__(self,_where, operacion_logica, _then, operacion_aritmetica, case_when):
	     self._where = _where
	     self.operacion_logica = operacion_logica
	     self._then = _then
	     self.operacion_aritmetica = operacion_aritmetica
	     self.case_when = case_when
     
class CaseWhen2(Sentencia): 
     def __init__(self,_end, valor):
	     self._end = _end
	     self.valor = valor
class ListaId(Sentencia): 
     def __init__(self,lista_id, coma, operacion_aritmetica):
	     self.lista_id = lista_id
	     self.coma = coma
	     self.operacion_aritmetica = operacion_aritmetica

class ListaId2(Sentencia): 
     def __init__(self,lista_id, coma, identificador, punto, identificador2):
	     self.lista_id = lista_id
	     self.coma = coma
	     self.identificador = identificador
	     self.punto = punto
	     self.identificador2 = identificador2
     
class ListaId3(Sentencia): 
     def __init__(self,operacion_aritmetica):
	     self.operacion_aritmetica = operacion_aritmetica
     
class ListaId4(Sentencia): 
     def __init__(self,identificador, punto, identificador2):
	     self.identificador = identificador
	     self.punto = punto
	     self.identificador2 = identificador2
     
class ListaId5(Sentencia): 
     def __init__(self,_substring, par1, valor, coma,valor2,coma2, valor3,par2):
	     self._substring = _substring
	     self.par1 = par1
	     self.valor = valor
	     self.coma = coma
	     self.valor2 = valor2
	     self.coma2 = coma2
	     self.valor3 = valor3
	     self.par2 = par2
     
class OpcionesFecha(Sentencia): 
     def __init__(self,_extract, par1, tipo_date, _from, tiemestamp_, valor, par2, pyc):
	     self._extract = _extract
	     self.par1 = par1
	     self.tipo_date = tipo_date
	     self._from = _from
	     self.tiemestamp_ = tiemestamp_
	     self.valor = valor
	     self.par2 = par2
	     self.pyc = pyc
     
class OpcionesFecha2(Sentencia): 
     def __init__(self,_now, par1, par2, pyc):
	     self._now = _now
	     self.par1 = par1
	     self.par2 = par2
	     self.pyc = pyc
     
class OpcionesFecha3(Sentencia): 
     def __init__(self,date_part, par1, valor, coma, interval, valor2, par2, pyc):
	     self.date_part = date_part
	     self.par1 = par1
	     self.valor = valor
	     self.coma = coma
	     self.interval = interval
	     self.valor2 = valor2
	     self.par2 = par2
	     self.pyc = pyc
     
class Opcionesfecha4(Sentencia): 
     def __init__(self,current_date, pyc):
	     self.current_date = current_date
	     self.pyc = pyc
     
class OpcionesFecha5(Sentencia): 
     def __init__(self,current_time, pyc):
	     self.current_time = current_time
	     self.pyc = pyc
class OpcionesFecha6(Sentencia): 
     def __init__(self,_timestamp, valor, pyc):
	     self._timestamp = _timestamp
	     self.valor = valor
	     self.pyc = pyc

class TipoDate(Sentencia): 
     def __init__(self,_year):
	     self._year = _year
     
class TipoDate2(Sentencia): 
     def __init__(self,_month):
	     self._month = _month
     
class TipoDate3(Sentencia): 
     def __init__(self,_day):
	     self._day = _day
     
class TipoDate4(Sentencia): 
     def __init__(self,_hour):
	     self._hour = _hour
     
class TipoDate5(Sentencia): 
     def __init__(self,_hour):
	     self._hour = _hour
     
class TipoDate6(Sentencia): 
     def __init__(self,_minute):
	     self._minute = _minute
     
class TipoDate7(Sentencia): 
     def __init__(self,_second):
	     self._second = _second
class Condicion(Sentencia): 
     def __init__(self,pyc):
	     self.pyc = pyc
     
class Condicion2(Sentencia): 
     def __init__(self,_where, operacion_logica, pyc):
	     self._where = _where
	     self.operacion_logica = operacion_logica
	     self.pyc = pyc


class Condicion3(Sentencia): 
     def __init__(self,_where, identificador, igual, operacion_aritmetica, pyc):
	     self._where = _where
	     self.identificador = identificador
	     self.igual = igual
	     self.operacion_aritmetica = operacion_aritmetica
	     self.pyc = pyc
     

     
class Condicion4(Sentencia): 
     def __init__(self,_where, _exists, par1, sentencia_select, par2, pyc):
	     self._where = _where
	     self._exists = _exists
	     self.par1 = par1
	     self.sentencia_select = sentencia_select
	     self.par2 = par2
	     self.pyc = pyc
     

class Condicion5(Sentencia): 
     def __init__(self,_where, operacion_aritmetica, _in, par1, sentencia_select, par2, pyc):
	     self._where = _where
	     self.operacion_aritmetica = operacion_aritmetica
	     self._in = _in
	     self.par1 = par1
	     self.sentencia_select = sentencia_select
	     self.par2 = par2
	     self.pyc = pyc
     
class Condicion6(Sentencia): 
     def __init__(self,_where, operacion_aritmetica, _not, _in, par1, setencia_select, par2, pyc):
	     self._where = _where
	     self.operacion_aritmetica = operacion_aritmetica
	     self._not = _not
	     self._in = _in
	     self.par1 = par1
	     self.setencia_select = setencia_select
	     self.par2 = par2
	     self.pyc = pyc
     

class OperacionAritmetica(Sentencia): 
     def __init__(self,operacion_aritmetica, mas, operacion_aritmetica2):
	     self.operacion_aritmetica = operacion_aritmetica
	     self.mas = mas
	     self.operacion_aritmetica2 = operacion_aritmetica2
     
class OperacionAritmetica2(Sentencia): 
     def __init__(self,operacion_aritmetica, menos, operacion_aritmetica2):
	     self.operacion_aritmetica = operacion_aritmetica
	     self.menos = menos
	     self.operacion_aritmetica2 = operacion_aritmetica2
     
class OperacionAritmetica3(Sentencia): 
     def __init__(self,operacion_aritmetica, por, operacion_aritmetica2):
	     self.operacion_aritmetica = operacion_aritmetica
	     self.por = por
	     self.operacion_aritmetica2 = operacion_aritmetica2
     
class OperacionAritmetica4(Sentencia): 
     def __init__(self,operacion_aritmetica, div, operacion_aritmetica2):
	     self.operacion_aritmetica = operacion_aritmetica
	     self.div = div
	     self.operacion_aritmetica2 = operacion_aritmetica2
     
class OperacionAritmetica5(Sentencia): 
     def __init__(self,par1, operacion_aritmetica, par2):
	     self.par1 = par1
	     self.operacion_aritmetica = operacion_aritmetica
	     self.par2 = par2
     
class OperacionAritmetica6(Sentencia): 
     def __init__(self,valor):
	     self.valor = valor
     
class OperacionAritmetica7(Sentencia): 
     def __init__(self,_sum, par1, operacion_aritmetica, par2):
	     self._sum = _sum
	     self.par1 = par1
	     self.operacion_aritmetica = operacion_aritmetica
	     self.par2 = par2
     
class OperacionAritmetica8(Sentencia): 
     def __init__(self,_avg, par1, operacion_aritmetica, par2):
	     self._avg = _avg
	     self.par1 = par1
	     self.operacion_aritmetica = operacion_aritmetica
	     self.par2 = par2
     
class OperacionAritmetica9(Sentencia): 
     def __init__(self,_max, par1, operacion_aritmetica, par2):
	     self._max = _max
	     self.par1 = par1
	     self.operacion_aritmetica = operacion_aritmetica
	     self.par2 = par2
     
class OperacionAritmetica10(Sentencia): 
     def __init__(self,_pi):
	     self._pi = _pi
     
class OperacionAritmetica11(Sentencia): 
     def __init__(self,_power, par1, operacion_aritmetica, par2):
	     self._power = _power
	     self.par1 = par1
	     self.operacion_aritmetica = operacion_aritmetica
	     self.par2 = par2
     
class OperacionAritmetica12(Sentencia): 
     def __init__(self,_sqrt, par1, operacion_aritmetica, par2):
	     self._sqrt = _sqrt
	     self.par1 = par1
	     self.operacion_aritmetica = operacion_aritmetica
	     self.par2 = par2
     
class OperacionAritmetica13(Sentencia): 
     def __init__(self,valor, _between, valor2):
	     self.valor = valor
	     self._between = _between
	     self.valor2 = valor2
     
class OperacionAritmetica14(Sentencia): 
     def __init__(self,valor, _is, _distinct,_from, valor2):
	     self.valor = valor
	     self._is = _is
	     self._distinct = _distinct
	     self._from = _from
	     self.valor2 = valor2
     
class OperacionAritmetica15(Sentencia): 
     def __init__(self,valor, _is, _not, _distinct, _from, valor2):
	     self.valor = valor
	     self._is = _is
	     self._not = _not
	     self._distinct = _distinct
	     self._from = _from
	     self.valor2 = valor2
     
class OperacionAritmetica16(Sentencia): 
     def __init__(self,valor, _is, _null):
	     self.valor = valor
	     self._is = _is
	     self._null = _null
     

     
class OperacionAritmetica17(Sentencia): 
     def __init__(self,valor, _is, _not, _null):
          self.valor = valor
          self._is = _is
          self._not = _not
          self._null = _null
     
class OperacionAritmetica18(Sentencia): 
     def __init__(self,valor, _is,_true):
	     self.valor = valor
	     self._is = _is
	     self._true = _true

class OperacionAritmetica19(Sentencia): 
     def __init__(self,valor, _is, _not, _true):
	     self.valor = valor
	     self._is = _is
	     self._not = _not
	     self._true = _true
     
class OperacionesAritmeticas20(Sentencia): 
     def __init__(self,valor, _is, _false):
	     self.valor = valor
	     self._is = _is
	     self._false = _false
     
class OperacionesAritmeticas21(Sentencia): 
     def __init__(self,valor, _is, _not, _false):
	     self.valor = valor
	     self._is = _is
	     self._not = _not
	     self._false = _false
     
class OperacionRelacional(Sentencia): 
     def __init__(self,operacion_relacional, mayor, operacion_relacional2):
	     self.operacion_relacional = operacion_relacional
	     self.mayor = mayor
	     self.operacion_relacional2 = operacion_relacional2

class OperacionRelacional2(Sentencia): 
     def __init__(self,operacion_relacional, menor, operacionrelacional2):
	     self.operacion_relacional = operacion_relacional
	     self.menor = menor
	     self.operacionrelacional2 = operacionrelacional2
     
class OperacionRelacional3(Sentencia): 
     def __init__(self,operacion_relacional, mayorigual, operacion_relacional2):
	     self.operacion_relacional = operacion_relacional
	     self.mayorigual = mayorigual
	     self.operacion_relacional2 = operacion_relacional2
     
class OperacionRelacional4(Sentencia): 
     def __init__(self,operacion_relacional,menorigual, operacional_relacional2):
	     self.operacion_relacional = operacion_relacional
	     self.menorigual = menorigual
	     self.operacional_relacional2 = operacional_relacional2
     
class OperacionRelacional5(Sentencia): 
     def __init__(self,operacion_relacional, diferente, operacion_relacional2):
	     self.operacion_relacional = operacion_relacional
	     self.diferente = diferente
	     self.operacion_relacional2 = operacion_relacional2
     
class OperacionRelacional6(Sentencia): 
     def __init__(self,operacion_relacional, igual, operacion_relacional2):
	     self.operacion_relacional = operacion_relacional
	     self.igual = igual
	     self.operacion_relacional2 = operacion_relacional2
     
class OperacionRelacional7(Sentencia): 
     def __init__(self,opracion_aritmetica):
	     self.opracion_aritmetica = opracion_aritmetica
     
class OperacionLogica(Sentencia): 
     def __init__(self,operacion_logica, _and, operacion_logica2):
	     self.operacion_logica = operacion_logica
	     self._and = _and
	     self.operacion_logica2 = operacion_logica2
     
class OperacionLogica2(Sentencia): 
     def __init__(self,operacion_logica, _or, operacion_logica2):
	     self.operacion_logica = operacion_logica
	     self._or = _or
	     self.operacion_logica2 = operacion_logica2
class OperacionLogica3(Sentencia): 
     def __init__(self,operacion_logica, _not, operacion_logica2):
	     self.operacion_logica = operacion_logica
	     self._not = _not
	     self.operacion_logica2 = operacion_logica2
     
class OperacionLogica4(Sentencia): 
     def __init__(self,operacion_relacional):
	     self.operacion_relacional = operacion_relacional
     

class SentenciaShow(Sentencia): 
     def __init__(self,_show, databases,show_cont):
	     self._show = _show
	     self.databases = databases
	     self.show_cont = show_cont
     
class ShowCont(Sentencia): 
     def __init__(self,pyc):
	     self.pyc = pyc
     
class ShowCont2(Sentencia): 
     def __init__(self,ins_like, pyc):
	     self.ins_like = ins_like
	     self.pyc = pyc
     
class InsLike(Sentencia): 
     def __init__(self,_like, porcentaje, identificador, porcentaje2):
	     self._like = _like
	     self.porcentaje = porcentaje
	     self.identificador = identificador
	     self.porcentaje2 = porcentaje2
     
class Empty(Sentencia): 
     def __init__(self,_empty):
	     self._empty = _empty
     

     


     




     



     



     



     

     


     



     



     



     

     








     

     


     



     


     

 
      
 
 


     



     




     





































































