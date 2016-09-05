from Tkinter import *

# crea la funzione di gestione dell'evento 
def evCanc():
  eCiao.delete(0,END)

# crea finestra e frame di primo livello
cima = Tk()
F = Frame(cima)
F.pack(expand="true")

# aggiungi il frame di immissione del testo
fTesto = Frame(F, border="1")
eCiao = Entry(fTesto)
fTesto.pack(side="top", expand="true")
eCiao.pack(side="left", expand="true")

# Infine il frame con i bottoni
# per evidenziarlo lo facciamo incavato
fBottoni = Frame(F, relief="sunken", border=1)
bCanc = Button(fBottoni, text="Cancella testo", command=evCanc)
bCanc.pack(side="left", padx=5, pady=2)
bEsci = Button(fBottoni, text="Esci", command=F.quit)
bEsci.pack(side="left", padx=5, pady=2)
fBottoni.pack(side="top", expand="true")

# Adesso attiviamo il ciclo degli eventi
F.mainloop()