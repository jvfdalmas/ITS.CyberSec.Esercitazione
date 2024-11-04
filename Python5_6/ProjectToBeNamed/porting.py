import os
import dbclient as db
import sys

mydb = db.connect()
if mydb is None:
    print("Errore conessione al DB")
    sys.exit()
else:
    print("Connessione avenuta correttamente")
    db.close(mydb)