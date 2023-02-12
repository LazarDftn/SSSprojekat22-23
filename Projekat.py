class Klijent:
    def __init__(self, ime, prezime, email, br_telefona, adresa, katrica_placanje, jezik_osnovni, jezik_dodatni, visina, tezina, stanje, ciljevi, rekviziti):
        self.ime = ime
        self.prezime = prezime
        self.email = email
        self.br_telefona = br_telefona
        self.adresa = adresa
        self.katrica_placanje = katrica_placanje
        self.jezik_osnovni = jezik_osnovni
        self.jezik_dodatni = jezik_dodatni
        self.visina = visina
        self.tezina = tezina
        self.stanje = stanje
        self.ciljevi = ciljevi
        self.rekviziti = rekviziti
        self.treninzi = []
        
    def book_trening(self, trener, date_and_time):
        self.treninzi.append({"Trener": Trener, "date_and_time": date_and_time})
        
    def cancel_trening(self, trener, date_and_time):
        for trening in self.treninzi:
            if trening["Trener"] == trener and trening["date_and_time"] == date_and_time:
                self.treninzi.remove(trening)
                return True
        return False
        
    def update_zdravlje_data(self, visina, tezina, stanje):
        self.visina = visina
        self.tezina = tezina
        self.stanje = stanje
        
    def oceniti_trener(self, trener, ocena, komentar):
        for trening in self.treninzi:
            if trening["trener"] == trener:
                trening["ocena"] = ocena
                trening["komentar"] = komentar
                return True
        return False
        
        
class Trener:
    def __init__(self, ime, prezime, email, br_telefona, adresa, katrica_placanje, jezik_osnovni, jezik_dodatni, diploma, sertifikat, zvanje):
        self.ime = ime
        self.prezime = prezime
        self.email = email
        self.br_telefona = br_telefona
        self.adresa = adresa
        self.katrica_placanje = katrica_placanje
        self.jezik_osnovni = jezik_osnovni
        self.jezik_dodatni = jezik_dodatni
        self.diploma = diploma
        self.sertifikat = sertifikat
        self.zvanje = zvanje
        self.dostupnost = []
        self.aktivan = False
        self.treninzi = []
        
    def add_dostupnost(self, date_and_time):
        self.dostupnost.append(date_and_time)
        
    def remove_dostupnost(self, date_and_time):
        self.dostupnost.remove(date_and_time)
        
    def design_trening(self, klijent):
        equipment = klijent.rekviziti
        zdravlje_data = {"visina": klijent.visina, "tezina": klijent.tezina, "stanje": klijent.stanje}
        ciljevi = klijent.ciljevi

        
 
