import flet as ft

from model import corso


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._text_corso = None
        self.btn_cerca_iscritti= None
        self.text_matricola = None
        self.txt_name = None
        self.text_cognome = None
        self.btn_cerca_studente = None
        self.btn_cerca_corsi = None
        self.btn_iscrivi = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.text_corso= ft.dropdown(key= corso.codins, text = corso.__str(), label="corso", width=550, hint_text="Selezionare un corso", options=[], autofocus= True, on_change= self._controller.leggi_corso)
        self._controller.populate_corso()
        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click= self._controller.handle_iscritti)
        row1 = ft.Row([self.text_corso, self.btn_cerca_iscritti],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.text_matricola = ft.TextField(label="matricola", width=250, hint_text="Inserisci la tua matricola")
        self.txt_name = ft.TextField(label="nome", width=250, read_only=True) #value=self._controller.getNome())
        self.text_cognome = ft.TextField(label="cognome", width=250, read_only=True) # value = self._controller.getCognome())
        row2 = ft.Row([self.text_matricola,self.txt_name,self.text_cognome], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.btn_cerca_studente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_studente)
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_corsi)
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrivi)
        row3 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # button for the "hello" reply
        #self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)
        #row1 = ft.Row([self.txt_name, self.btn_hello],
               #       alignment=ft.MainAxisAlignment.CENTER)
        #self._page.controls.append(row1)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
