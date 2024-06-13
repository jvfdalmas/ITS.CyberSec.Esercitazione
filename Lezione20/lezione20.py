# Esercizi Classi Astratte, Ereditarietà, Polimorfismo

"""GESTIONALE PAGAMENTO
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento e si definiscano appropriati metodi get() e set(). L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti e si invochi dettagliPagamento() per ognuno di essi.

Esempio di output:
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321
"""
class Pagamento:

    def __init__(self):
        self.__amount: float = None

    def setImport(self, amount: float):
        # Consente di impostare il importo
        if isinstance(amount, float):
            self.__amount = amount
            return self.__amount
        else:
            return "Amount is not a float value!"
        
    def getImport(self):
        return round(self.__amount,2)
    
    def dettagliPagamento(self) -> str:
        return f"Importo del pagamento: €{self.getImport():.2f}."


class PagamentoContanti(Pagamento):

    def __init__(self):
        Pagamento.__init__(self)
    
    def dettagliPagamento(self) -> str:
        return f"Importo del pagamento: €{self.getImport():.2f} in contanti."
    
    def inPezzida(self):
        total_amount: float = self.getImport()
        contanti: dict[float,int] = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.50: 0, 0.20: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        result: list = [f"{self.getImport():.2f} euro da pagare in contanti con:\n"]

        for amount in contanti.keys():
            while total_amount >= amount and total_amount > 0:
                total_amount = round(total_amount - amount, 2)
                contanti[amount] += 1
        
        for amount, banconote in contanti.items():
            if banconote > 0 and amount > 2:
                msg: str = f"{banconote} banconota da {amount} euro.\n"
                result.extend(msg)
            if banconote > 0 and 2 >= amount:
                msg: str = f"{banconote} moneta da {amount} euro.\n"
                result.extend(msg) 
        
        return "".join(result), result[-1]
    
    
    

class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, titolare, numero, scadenza):
        Pagamento.__init__(self)
        
        if isinstance(titolare, str):
            self.__titolare: str = titolare
        else:
            return "name should be str"
        if isinstance(scadenza, str):
            self.__scadenza: int = scadenza
        else:
            return "scadenza should be str"
        if isinstance(numero, int):
            self.__numero:int = numero
        else:
            return "numero should be int"
        
    def getName(self):
        return self.__titolare

    def getData(self):
        return self.__scadenza
    
    def getNumero(self):
        return self.__numero
    
    def dettagliPagamento(self) -> str:
        return f"Pagamento di: €{self.getImport():.2f} effettuato con la carta di credito\nNome sulla carta: {self.getName()}\nData di scadenza: {self.getData()}\nNumero della carta: {self.getNumero()}"
    

pgto_contanti_150 = PagamentoContanti()
pgto_contanti_150.setImport(150.00)
print(pgto_contanti_150.dettagliPagamento())
print(pgto_contanti_150.inPezzida())

pgto_contanti_95 = PagamentoContanti()
pgto_contanti_95.setImport(95.25)
print(pgto_contanti_95.dettagliPagamento())
print(pgto_contanti_95.inPezzida())

pgto_carta_200 = PagamentoCartaDiCredito("Mario Rossi", 1234567890123456, "12/24")
pgto_carta_200.setImport(200.00)
print(pgto_carta_200.dettagliPagamento())

pgto_carta_500 = PagamentoCartaDiCredito("Luigi Bianchi", 6543210987654321, "01/25")
pgto_carta_500.setImport(500.00)
print(pgto_carta_500.dettagliPagamento())