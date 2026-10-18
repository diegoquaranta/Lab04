from stand import Stand
from espositori import Espositori
from prese_stand import StandConPrese
from premium_stand import StandPremium


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.listaStand = []
        self.listaEspositori = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        with open(file_path, "r", encoding="utf8") as f:
            righe = f.readlines()

        for i in range(len(righe)):
            righe[i] = righe[i].strip().split(",")


        for riga in righe:
            if len(riga) == 4:
                codice = riga[0]
                if codice[:2] == "ST":
                    superfice = int(riga[1])
                    padiglione = int(riga[2])
                    prezzo = int(riga[3])

                    self.listaStand.append(Stand(codice, superfice, padiglione, prezzo))

            elif len(riga) == 5:
                codice = riga[0]
                if codice[:2] == "ST":
                    superfice = int(riga[1])
                    padiglione = int(riga[2])
                    prezzo = int(riga[3])

                    if riga[4]:
                        if riga[4].isdigit():
                            prese = int(riga[4])
                            self.listaStand.append(StandConPrese(codice, superfice, padiglione, prezzo, prese))

                        elif riga[4].isalpha():
                            stringa = riga[4]
                            self.listaStand.append(StandPremium(codice, superfice, padiglione, prezzo, stringa))

            elif len (riga) == 3:
                codice = riga[0]
                if codice [:2] == "ES":
                    nome = riga[1]
                    cognome =  riga[2]

                    self.listaEspositori.append(Espositori(codice, nome, cognome))


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        stand_trovato = None

        for stand in self.listaStand:
            if stand.codice == codice_stand:
                stand_trovato = stand
                break

        if stand_trovato is None:
            raise ValueError("Stand non trovato")

        espositore_trovato = None

        for espositore in self.listaEspositori:
            if espositore.codice == codice_espositore:
                espositore_trovato = espositore
                break

        if espositore_trovato is None:
            raise ValueError("Espositore non trovato")

        if stand_trovato.espositore is not None:
            raise ValueError("Stand già occupato")

        for stand in self.listaStand:
            if stand.espositore is espositore_trovato:
                raise ValueError ("Espositore gia assegnato ad uno stand")

        stand_trovato.espositore = espositore_trovato



    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for espositore in self.listaEspositori:
            stand_trovato = None

            for stand in self.listaStand:
                if stand.espositore == espositore:
                    stand_trovato = stand
                    break

            if stand_trovato is not None:
                print(espositore.codice, "- Stand:", stand_trovato.codice)
            else:
                print(espositore.codice, "-Nessuno stand")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        return sorted(self.listaStand, key=lambda stand:stand.prezzo)
