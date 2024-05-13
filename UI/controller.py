import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._id_map_corsi = {}
        self.corso_selezionato = None

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handle_iscritti(self, e):
        if self.corso_selezionato is None:
            self.view.create_alert("Selezionare un corso!")
            return
        iscritti = self._model.get_iscritti_corso(self.corso_selezionato)
        if iscritti is None:
            self._view.create_alert("Problema nella connessione!")
            return
        self._view.txt_result.controls.clear()
        if len(iscritti) == 0:
            self._view.txt_result.controls.append(ft.Text("Non ci sono iscritti al corso"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
            for studente in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{studente}"))
            self._view.update_page()

    def handle_studente(self,e):
        matricola = self._view.text_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire la matricola!")
            return
        studente = self._model.cerca_studente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non esistente")
            return
        else:
            self._view.txt_name.value == f"{studente.nome}"
            self._view.text_cognome.value == f"{studente.cognome}"
        self._view.update_page()

    def handle_corsi(self,e):
        matricola = self._view.text_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire la matricola!")
            return
        else:
            corsi = self._model.get_corsi_studente(matricola)
            if len(corsi) == 0:
                self._view.create_alert("Lo studente non è iscritto ad alcun corso")
            else:
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi"))
                for corso in corsi:
                    self._view.txt_result.controls.append(ft.Text(f"{corso}"))
                self._view.update_page()

    def handle_iscrivi(self,e):
        matricola = self._view.text_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola")
            return
        studente = self._model.cerca_studente(matricola)
        if studente is None:
            self._view.create_alert("Inserire una matricola già esitente nel database")
            return
        codice_corso = self._view.text_corso.value
        if codice_corso is None:
            self._view.create_alert("Selezionare un corso!")
            return
        result = self._model.iscrivi_corso(matricola, codice_corso)
        self._view.txt_result.controls.clear()
        if result:
            self._view.txt_result.controls.append(ft.Text("Iscrizione avvenuta con successo"))
        else:
            self._view.txt_result.controls.append(ft.Text("Iscrizione fallita"))
        self._view.update_page()

    def populate_corso(self):
        for corso in self._model.get_corsi():
            self._id_map_corsi[corso.codins] = corso
            self._view.text_corso.options.append(ft.dropdown.Option(key =corso.codins, text = corso))
        self._view.update_page()

    def leggi_corso(self,e):
        self.corso_selezionato = self._view.text_corso.value