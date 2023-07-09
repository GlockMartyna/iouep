class Samochod:
    def __init__(self, marka, model, rok_prod, kolor, ilosc_drzwi, spalanie, wazne_ubez, max_pred):
        self.marka = marka
        self.model = model
        self.rok_prod = rok_prod
        self.kolor = kolor
        self.ilosc_drzwi = ilosc_drzwi
        self.spalanie = spalanie
        self.wazne_ubez = wazne_ubez
        self.max_pred = max_pred
        self.indeks = []

    def __str__(self):
        return self.marka + ' ' + self.model + " " + str(self.rok_prod)

    def zmien_model(self, model):
        self.model=model

    def wiek_auta(self):
            rok=2023
            return rok -self.rok_prod

samochod_citroen = Samochod("Citroen","Berlingo",2005,"srebrny",3,8,True,150)
samochod_citroen.zmien_model("Xara Picasso")
samochod_citroen.wiek_auta()

print(samochod_citroen.wiek_auta())
