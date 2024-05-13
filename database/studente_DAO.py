
from database.DB_connect import get_connection
from model.studente import Studente
    def cerca_studente(matricola) -> Studente | None:
        cnx = get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                FROM studente
                WHERE studente.matricola =%s,(matricola,))"""
            cursor.execute(query)
            row = cursor.fetchone()
            if row is not None:
                result = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
            else:
                result = None

            cursor.close()
            cnx.close()
            return result
        else:
            print("Impossibile connettersi")
            return None



