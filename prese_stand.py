from stand import Stand

class StandConPrese(Stand):
    def __init__(self, codice, superfice, padiglione,  prezzo, prese):
        super().__init__(codice, superfice, padiglione,  prezzo) #ho esteso la classe stand
        self.__prese = prese

    @property
    def prese(self):
        return self.__prese

    @prese.setter
    def prese(self, prese):
        self.__prese = prese

    @property
    def prezzo(self):
        return super().prezzo * (1 + 0.07 * self.prese)

    def __str__(self):
        return f"{super().__str__()} - Prese aggiuntive: {self.prese}"