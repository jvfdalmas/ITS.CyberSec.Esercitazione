# Esercizio: Sistema di Recensioni

"""Obiettivo: Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione()."""

print("Esercizio: Sistema di Recensioni - Soluzione: \n")

import math

class Media:

    def __init__(self) -> None:
        self.title: str = ""
        self.reviews: list = []
        self.giudizio: dict = {1: "Terribile", 2: "Brutto", 3: "Normale", 4: "Bello", 5: "Grandioso"}

    def set_title(self, title: str) -> None:
        self.title: str = title
        return self.title
    
    def get_title(self) -> str:
        return self.title
    
    def aggiungiValutazione(self, voto: int):
        if 1 <= voto <= 5:
            self.reviews.append(voto)
            return self.reviews
    
    def getMedia(self) -> float:
        return round(sum(self.reviews)/len(self.reviews),2)
    
    def getRate(self) -> str:
        media = self.getMedia()
        return self.giudizio.get(math.floor(media))

    def ratePercentage(self, voto: int):
        counter = 0

        for rate in self.reviews:
            if rate == voto:
                counter += 1
        
        if counter == 0:
            return "0%"
        if counter > 0:
            percentage = round(((counter / len(self.reviews)) * 100), 2)
            return f"{str(percentage)}%"
        
    def recensione(self):
        
        return f"Titolo del Film: {self.title}\nVoto Medio: {self.getMedia()}\nGiudizio:{self.getRate()}\nTerribile: {self.ratePercentage(1)}%\nBrutto: {self.ratePercentage(2)}\nNormale: {self.ratePercentage(3)}\nBello: {self.ratePercentage(4)}\nGrandioso: {self.ratePercentage(5)}"
    

film: Media = Media()
film.set_title("Alien")
film.aggiungiValutazione(1)
film.aggiungiValutazione(1)
film.aggiungiValutazione(5)
film.aggiungiValutazione(5)
film.aggiungiValutazione(5)
film.aggiungiValutazione(2)
film.aggiungiValutazione(3)
film.aggiungiValutazione(3)
film.aggiungiValutazione(4)
film.aggiungiValutazione(4)
film.aggiungiValutazione(4)
print(film.recensione())