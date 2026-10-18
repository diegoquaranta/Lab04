
class Espositori:

    def __init__(self, codice , nome , cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome

    @property
    def codice(self):
        return self.__codice

    @codice.setter
    def codice(self, codice):
        self.__codice = codice

    @property
    def nome(self):
        return self.__nome

    @property
    def cognome(self):
        return self.__cognome

    def __eq__(self, other):
        if isinstance(other, Espositori):
            return self.codice == other.codice
        return False

    def __str__(self):
        return f"{self.codice} - {self.nome} {self.cognome}"