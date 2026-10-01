lista = [4, 6]

tupla = (4, 5, -6) # Es. un punto nello spazio 3D

# dizionario di studenti con chiave la matricola e valore il nomeCognome
diz_studenti = {"015675" : "Mario Rossi", "12345" : "Gianni Verdi"}

# lista di liste (tabella)
lista_studenti = [["015675", "Mario Rossi"],
                  ["12345", "Gianni Verdi"]]

# liste separate
lista_matricole = ["015675", "12345"]
lista_nomi_cognomi = ["Mario Rossi", "Gianni Verdi"]

# dizionario -> struttura ottimizzata per ricerche

nuova_lista = lista_studenti # non copia la lista!
# crea solamente un "alias", in memoria i dati non sono stati duplicati

copia_della_lista = list(nuova_lista) # questa crea proprio una copia
