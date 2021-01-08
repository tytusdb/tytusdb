from . import InterfazBD
from . import ISAMMode as Storage

vectorBases=Storage.showDatabases()
InterfazBD.PantallaBD(vectorBases)
