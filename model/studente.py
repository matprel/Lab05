class Studente:
    matricola: int = 0
    cognome: str = ""
    nome: str = ""
    cds: str = ""

    def __str__(self):
        return f"{self.nome},{self.cognome},{self.matricola}"

    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)