# Testi Digitali

""" Si definisca una classe Documento che contenga una variabile di tipo stringa chiamata testo e che memorizza qualsiasi contenuto testuale per il documento.

Si crei un metodo getText() che restituisca il testo. Si crei un metodo setText() per impostare il testo. Scrivere un metodo isInText() che restituisce True se un documento contiene la parola chiave specificata.

Si definisca poi una classe Email che sia derivata da Documento e che includa le variabili per il mittente, il destinatario e il titolo del messaggio.

Si implementino i metodi get() e set() appropriati per tali variabili. Il corpo del messaggio dell’e-mail dovrebbe essere memorizzato nella variabile ereditata testo.

Si ridefinisca il metodo getText() per concatenare e ritornare tutti i campi di testo (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
 
    Da: alice@example.com, A: bob@example.com
    Titolo: Incontro
    Messaggio: Ciao Bob, possiamo incontrarci domani?
 
Inoltre, si implementi un metodo writeToFile() per scrivere il risultato del metodo getText() in un file di testo e in un percorso specificato.
 
Analogamente, si definisca una classe File che sia derivata da Documento e includa una variabile per il nomePercorso.
Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.

I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in nomePercorso e memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().

Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:
 
    Percorso: nomePercorso/document.txt
    Contenuto: Questo e' il contenuto del file."""


print("Test tramite codice driver".upper(), "\n")

# doc = Documento()
# doc.setText("""SUGLI ERRORI
# Gli errori sono inevitabili. Errare è umano,
# perseverare è diabolico. Non ci sono rimedi
# a questo stato di cose (su questa terra).""")
# print(doc.getText())

# print("\n")

# mail = Email()
# mail.setText("""Questo è il contenuto del file.""")
# mail.setDestinatario("dddd@hotmail.com")
# mail.setMittente("mmm@gmail.com")
# mail.setOggetto("TESTE")
# print(mail.getText())
# mail.writeToFile()

# print("\n")

# file = File()
# file.setPath(r"C:\Users\Cloud\Documents\Github_windows_JDM\document.txt")
# print(file.getText())

# print("\n")

# print(file.isInText("gmail.com")) # true
# print(file.isInText("gmail.it")) # false

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

### Test con UnitTest

"""Utilizzando il modulo unittest, definire i seguenti test per le classi Documento, Email e File.
 
I test devono includere:

    Verifica dei metodi getText() e setText() nella classe Documento.
    Verifica del metodo isInText() nella classe Documento.
    Verifica del metodo getText() nella classe Email.
    Verifica del metodo writeToFile() nella classe Email.
    Verifica del metodo isInText() nella classe Email.
    Verifica del metodo getText() nella classe File.
    Verifica del metodo isInText() nella classe File."""

print("Test con UnitTest".upper(), "\n")