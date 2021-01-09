import storage.isam.InterfazBD as InterfazBD
import storage.isam.isam_Mode as Storage

vectorBases=Storage.showDatabases()
InterfazBD.PantallaBD(vectorBases)
