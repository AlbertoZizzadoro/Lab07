import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''


class Controller:
    def __init__(self, view: View, model: Model) -> None:
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        # Inizializziamo a None (che corrisponde a "Nessun filtro")
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        # Popola Musei
        lista_musei = self._model.get_musei()
        opzioni_musei = [ft.dropdown.Option("Nessun filtro")]  # Aggiungo "Nessun filtro"
        opzioni_musei.extend([ft.dropdown.Option(museo.nome) for museo in lista_musei])


        self._view._musei.options = opzioni_musei

        # Popola Epoche
        lista_epoche = self._model.get_epoche()
        opzioni_epoche = [ft.dropdown.Option("Nessun filtro")]
        opzioni_epoche.extend([ft.dropdown.Option(epoca) for epoca in lista_epoche])


        self._view._epoche.options = opzioni_epoche

        self._view.update()


    def seleziona_museo(self, e):

        if e.control.value == "Nessun filtro":
            self.museo_selezionato = None
        else:
            self.museo_selezionato = e.control.value

    def seleziona_epoca(self, e):

        if e.control.value == "Nessun filtro":
            self.epoca_selezionata = None
        else:
            self.epoca_selezionata = e.control.value

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, e):

        self._view._listArtefatti.controls.clear()


        try:
            artefatti = self._model.get_artefatti_filtrati(
                self.museo_selezionato,
                self.epoca_selezionata
            )

            # Controlla i risultati
            if not artefatti:
                # Se la lista è vuota, mostra un alert
                self._view.show_alert("Nessun artefatto trovato con i filtri selezionati.")
            else:
                #  Popola la ListView
                for artefatto in artefatti:

                    self._view._listArtefatti.controls.append(
                        ft.Text(str(artefatto))
                    )

        except Exception as ex:
            self._view.show_alert(f"Errore durante il recupero dati: {ex}")

        #  Aggiorna la view
        self._view.update()