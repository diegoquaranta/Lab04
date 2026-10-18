
class Stand:
    def __init__(self, codice, superfice, padiglione,  prezzo):
        self.__codice = codice
        self.__superfice = superfice
        self.__padiglione = padiglione
        self.__prezzo = prezzo

        self.__espositore = None

    @property
    def codice(self):
        return self.__codice
    @codice.setter
    def codice(self, codice):
        self.__codice = codice

    @property
    def espositore(self):
        return self.__espositore
    @espositore.setter
    def espositore(self, espositore):
        self.__espositore = espositore

    @property
    def disponibile(self):
        return self.__espositore is None

    @property
    def prezzo(self):
        return self.__prezzo

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Occupato"
        return f"{self.codice} - Prezzo: {self.prezzo:.2f}€ - {stato}"