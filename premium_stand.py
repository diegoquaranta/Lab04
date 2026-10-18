from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice, superfice, padiglione,  prezzo, stringa):
        super().__init__(codice, superfice, padiglione,  prezzo)
        self.__stringa = stringa

    @property
    def stringa(self):
        return self.__stringa

    @stringa.setter
    def stringa(self, stringa):
        self.__stringa = stringa

    @property
    def prezzo(self):
        return super().prezzo * 1.30

    def __str__(self):
        return f"{super().__str__()} - Posizione: {self.stringa}"
