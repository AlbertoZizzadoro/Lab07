from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""


class MuseoDAO:
    def __init__(self):
        pass

    def get_musei(self):
        lista_musei = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Errore connessione DB")
            return []

        cursor = cnx.cursor(dictionary=True)  # Usiamo dictionary=True per mappare DTO
        query = "SELECT * FROM museo"  # CORREZIONE: museo (singolare)
        cursor.execute(query)
        for riga in cursor:
            # Mappiamo i campi del DB ai campi del DTO
            lista_musei.append(Museo(id=riga["id"],
                                     nome=riga["nome"],
                                     tipologia=riga["tipologia"]))

        cursor.close()
        cnx.close()
        return lista_musei

    def get_epoche(self):
        lista_epoche = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Errore connessione DB")
            return []

        cursor = cnx.cursor()
        query = "SELECT DISTINCT(epoca) FROM artefatto"  # CORREZIONE: artefatto (singolare)
        cursor.execute(query)
        for riga in cursor:
            lista_epoche.append(riga[0])
        cursor.close()
        cnx.close()
        return lista_epoche