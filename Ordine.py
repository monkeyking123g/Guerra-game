# Conto per ordine
from tkinter import *

class Application(Frame):
    """ GUI per menu di ristorante. """
    def __init__(self, master):
        """ Initialize Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Creazione di widgets per Menu"""
        Label(self,
              text = "Cosa rdiniamo Oggi"
              ).grid(row = 0, column = 0, sticky = W)
        # name
        Label(self,
              text = "Tuo nuome: "
              ).grid(row = 1, column = 0, sticky = W)
        self.naim_ent = Entry(self)
        self.naim_ent.grid(row = 1, column = 1, sticky = W)
        

        # creazione di primi piatti
        Label(self,
              text = "Primi piatti"
              ).grid(row = 2, column = 0, sticky = W)
        
        self.primi_piat = StringVar()
        self.primi_piat.set(None)
        
        primi_piat = ["pasta al foro", "pasta genovese", "pasta tonno piselli"]
        column = 1
        for piat in primi_piat:
            Radiobutton(self,
                        text = piat,
                        variable = self.primi_piat,
                        value = piat
                        ).grid(row = 2, column = column, sticky = W)
            column += 1

        # creazione dei secondi piatti
        Label(self,
              text = "Secondi piatti"
              ).grid(row = 3, column = 0, sticky = W)
        
        self.secondi_piat = StringVar()
        self.secondi_piat.set(None)
        
        secondi_piat = ["tagliata di cavalo", "pesche", "gamberoni"]
        column = 1
        for piat in secondi_piat:
            Radiobutton(self,
                        text = piat,
                        variable = self.secondi_piat,
                        value = piat
                        ).grid(row = 3, column = column, sticky = W)
            column += 1

        # creazione di caffe e aqua
        Label(self,
              text = "Caffe e Aqua"
              ).grid(row = 4, column = 0, sticky = W)

        self.caffe = BooleanVar()
        Checkbutton(self,
                    text = "Caffe",
                    variable = self.caffe
                    ).grid(row = 4, column = 1, sticky = W)
        
        self.aqua_n = BooleanVar()
        Checkbutton(self,
                    text = "Aqua naturale",
                    variable = self.aqua_n
                    ).grid(row = 4, column = 2, sticky = W)
        
        self.aqua_f = BooleanVar()
        Checkbutton(self,
                    text = "Aqua Frizzante",
                    variable = self.aqua_f
                    ).grid(row = 4, column = 3, sticky = W)
        
        

        # creazione di conto per cena
        Button(self,
               text = "Clicka per sapere conto",
               command = self.conto
               ).grid(row = 5, column = 0, sticky = W)

        self.conto_txt = Text(self, width = 75, height = 10, wrap = WORD, bd = 5)
        self.conto_txt.grid(row = 6, column = 0, columnspan = 4)

    def conto(self):
        total = 0
        c = 1
        a = 2
        pr = 8
        sc = 15
        cop = 2.5
        person = self.naim_ent.get()
        primi = self.primi_piat.get()
        secondi = self.secondi_piat.get()
        bibita = ""
        piatt= ""
        padel = ""
        if primi:
            piatt += primi + " 8$"
            total += pr 
            
        if secondi:
            padel += secondi + " 15$"
            total += sc

        if self.aqua_n.get():
            bibita += "Aqua naturale 2$ \n"
            total  += a
            
        if self.aqua_f.get():
            bibita += "Aqua frizzante 2$ \n"
            total += a
            
        if self.caffe.get():
            bibita += "Caffe 1$ \n"
            total += c
            
        total += cop

        message = ""
        message += person + "\n"
        message += piatt + "\n"
        message += padel + "\n"
        message += bibita 
        message += "Coperta 2,50\n"
        message += "Totale: " + str(total)



        # display                                
        self.conto_txt.delete(0.0, END)
        self.conto_txt.insert(0.0, message)


# main
root = Tk()
root.title("Conto")
root.geometry("600x400")
app = Application(root)
root.mainloop()

        

        

        
