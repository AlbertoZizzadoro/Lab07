from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto
from model.museoDTO import Museo

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""


class ArtefattoDAO:
    def __init__(self):
        pass

    def get_artefatti_filtrati(self, nome_museo: str | None, epoca: str | None):
        """
        Filtra gli artefatti per nome museo e/o epoca.
        Accetta None per entrambi i parametri se il filtro non è attivo.
        """
        lista_artefatti = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Errore connessione DB")
            return []

        cursor = cnx.cursor(dictionary=True)

        # Query che unisce artefatto e museo per filtrare per nome
        # e usa COALESCE per i filtri opzionali
        query = """
            SELECT a.* FROM artefatto a JOIN museo m ON a.id_museo = m.id
            WHERE m.nome = COALESCE(%s, m.nome) 
              AND a.epoca = COALESCE(%s, a.epoca)
            ORDER BY a.nome
        """

        cursor.execute(query, (nome_museo, epoca))

        for riga in cursor:
            lista_artefatti.append(Artefatto(id=riga["id"],
                                             nome=riga["nome"],
                                             tipologia=riga["tipologia"],
                                             epoca=riga["epoca"],
                                             id_museo=riga["id_museo"]))

        cursor.close()
        cnx.close()
        return lista_artefatti