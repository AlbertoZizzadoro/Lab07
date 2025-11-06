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
        lista_musei=[]
        cnx=ConnessioneDB.get_connection()
        cursor=cnx.cursor()
        query="SELECT * FROM musei"
        cursor.execute(query)
        for riga in cursor:
            lista_musei.append(Museo(*riga))

        cursor.close()
        cnx.close()
        return lista_musei

    def get_epoche(self):
        lista_epoche=[]
        cnx=ConnessioneDB.get_connection()
        cursor=cnx.cursor()
        query="SELECT DISTINCT(epoca) FROM artefatti"
        cursor.execute(query)
        for riga in cursor:
            lista_epoche.append(riga[0])
        cursor.close()
        cnx.close()
        return lista_epoche





