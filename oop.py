# definizione della classe Studente
class Studente:
    # Attributi
    matricola = 0
    nome = ""
    cognome = ""

    # Funzioni
    # def immatricola(self, m):
    #     self.matricola = m # per far capire che stiamo usando quella variabile

    # COSTRUTTORE: funzione standard per inizializzare l'oggetto
    def __init__(self, matricola, nome, cognome):
        self.matricola = matricola # self significa questo oggetto
        self.nome = nome
        self.cognome = cognome

    # Altre funzioni
    def sostiene_esame(self):
        print("Sostieme esame")

    def si_unisce_a_gruppo_studentesco(self):
        print("Si unisce a gruppo studentesco")





# creo un oggetto/istanza della classe Studente

# iniziale maiuscola --> CLASSE
# iniziale minuscola --> FUNZIONI / VARIABILI

s = Studente(12345, "Mario", "Rossi") # sto creando e inizializzando uno studente
               # Python chiama la funzione __init__ (costruttore)
               # se non passo nessun parametro mette i valori di default agli attributi


print(s) # stampa: <__main__.Studente object at 0x000001B8ADF83230>
         # oggetto della classe studente presente nel main all'indirizzo di memoria 0x000001B8ADF83230

# Accedo alla pancia dell'oggetto per leggere o scrivere i suoi attributi
print(f"Matricola {s.matricola}\n"
      f"Nome: {s.nome}\n"
      f"Cognome: {s.cognome}")

s.sostiene_esame() # posso invocare su QUELLO studente Mario Rossi
                   # la funzione che serve per fargli sostenere
                   # l'esame: DATI E OPERAZ. SUI DATI SONO INCAPSULARE NELL'OGGETTO

# in Python anche i file sono gestiti come classi e oggetti

# Collezione di studenti

lista_studenti = []
lista_studenti.append(s)
lista_studenti.append(Studente(67890, "Gianni", "Verdi")) # posso anche aggiungere uno studente creandolo al volo

print("\nElenco studenti:\n")
for studente in lista_studenti:
    print(f"Matricola: {studente.matricola}\n"
          f"Nome: {studente.nome}\n"
          f"Cognome: {studente.cognome}\n")