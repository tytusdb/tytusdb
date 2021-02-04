from Block import Block
from ListaBlockchain import *

l = BlockChain()
tabla = []

#VERIFICAR QUE FUNCIONE BIEN EL METODO AL HACER LAS LLAMADAS!!!!!!!!!
def activar_SaveModo(registro):
    tabla = registro
    genesis_block = Block("0", tabla)
    if l.listaVacia() is True:
        #genesis_block = Block("0", tabla)
        l.agregarLista(str(genesis_block.transaction), str(genesis_block.block_hash))
        #bloque_anterior = bloque_genesis.block_hash
        l.archivo_json()
        l.GraficarConArchivo()
        #print(l.imprimir())
    else:
        tabla1 = registro
        second_block = Block(genesis_block.block_hash, tabla1)
        l.agregarLista(str(second_block.transaction), str(second_block.block_hash))
        #bloque_anterior = bloque.block_hash
    #l.imprimir()
    l.GraficarConArchivo()
    l.archivo_json()

def modificar_cadena(indice,registro):
    l.modificarNodo(indice,registro)
    #l.GraficarConArchivo()
    #l.archivo_json()
def desactivar_SaveModo(database, table):
    #0 operación exitora, 1 error en la operación, 
    #2 base de datos inexistente, 3 tabla inexistente, 4 modo seguro no existente.
    return None

def abrir():
    l.abrirImagen()