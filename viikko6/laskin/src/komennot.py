class Summa:
    def __init__(self, logiikka, lue_syote):
        self._logiikka = logiikka
        self._lue_syote = lue_syote
        self._arvo_ennen = logiikka.arvo()
        print(f'arvo_ennen: {self._arvo_ennen }')

    def suorita(self):
        arvo = self._lue_syote()
        self._logiikka.plus(arvo)

    def kumoa(self):
        print(f'arvo ennen: {self._arvo_ennen}')
        self._logiikka.aseta_arvo(self._arvo_ennen)


class Erotus:
    def __init__(self, logiikka, lue_syote):
        self._logiikka = logiikka
        self._lue_syote = lue_syote
        self._arvo_ennen = logiikka.arvo()

    def suorita(self):
        arvo = self._lue_syote()
        self._logiikka.miinus(arvo)
    
    def kumoa(self):
        self._logiikka.aseta_arvo(self._arvo_ennen)

class Nollaus:
    def __init__(self, logiikka, lue_syote):
        self._logiikka = logiikka
        self._lue_syote = lue_syote
        self._arvo_ennen = logiikka.arvo()

    def suorita(self):
        self._logiikka.nollaa()

    def kumoa(self):
        self._logiikka.aseta_arvo(self._arvo_ennen)
