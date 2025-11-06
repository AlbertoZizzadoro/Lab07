import flet as ft
from UI.alert import AlertManager
from UI.controller import Controller
from model.model import Model

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = Controller(self, Model())
        self.controller.popola_dropdown()

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self._musei = ft.Dropdown(label="Seleziona Museo",
                                  #options=[self._model.get_musei()],
                                  width=300,
                                  hint_text="Seleziona un museo",
                                  on_change=self.controller.popola_dropdown,

                                  )
        self._epoche = ft.Dropdown(label="Seleziona Epoca",
                                   options=[self._controller.popola_dropdown()],
                                   width=200,
                                   hint_text="Seleziona un'epoca",
                                   on_change=self.controller.popola_dropdown,
                                   )
        self._row=ft.Row(controls=[self._musei,self._epoche],
                         alignment=ft.MainAxisAlignment.CENTER)



        # Sezione 3: Artefatti
        self._btnMostrArtefatti = ft.ElevatedButton(text="Mostra Artefatti",
                                                    width=300,
                                                   # on_click=self.controller.mostra_artefatti
                                                )
        self._listArtefatti = ft.ListView(expand=True, spacing=10, padding=20)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            self._row,
            ft.Divider(),

            # Sezione 3: Artefatti
            self._btnMostrArtefatti,
            self._listArtefatti

        )


        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
