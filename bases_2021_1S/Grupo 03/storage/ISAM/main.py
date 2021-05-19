from storage.ISAM import InterfazBD
from storage.ISAM import ISAMMode as Storage

vectorBases = Storage.showDatabases()
InterfazBD.PantallaBD(vectorBases)
