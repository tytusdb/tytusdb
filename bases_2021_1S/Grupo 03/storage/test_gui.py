from storage.AVL.View.Interfaz import run as avlGUI
#from storage.BTree import Interfaz as bTreeGUI
#from storage.BPTree import Interfazz as bPTreeGUI
#from storage.ISAM import InterfazBD as isamGUI
#from storage.ISAM import ISAMMode as storageISAM
#from storage.Hash.storage import ReporteGrafico as hashGUI


def GUI(mode):
    if mode == 1:
        avlGUI()
    elif mode == 2:
        # bTreeGUI.runInterface()
        pass
    elif mode == 3:
        # bPTreeGUI.start()
        pass
    elif mode == 4:
        # vectorBases = storageISAM.showDatabases()
        # isamGUI.PantallaBD(vectorBases)
        pass
    elif mode == 5:
        # hashGUI.Mostrar()
        pass
