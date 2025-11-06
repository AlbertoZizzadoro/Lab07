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
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        self._model._musei.options = [ft.dropdown.Option(museo.nome) for museo in self._model.get_musei()]
        self._model._epoche.options = [ft.dropdown.Option(epoca) for epoca in self._model.get_epoche()]


    # CALLBACKS DROPDOWN
    def seleziona_museo(self, e):
        self.museo_selezionato = e.control.value

    def seleziona_epoca(self, e):
        self.epoca_selezionata = e.control.value

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
