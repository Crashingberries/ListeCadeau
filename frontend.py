from tkinter import *
import fonctions

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.donnees_application = {"nomEnfant":    StringVar()}
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        #self.donnees_application["nomEnfant"]="Simon" #BYPASS
        self.frames = {}
        for F in (StartPage, Ajouter, Recherche, ResultatRecherche):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        Frame.__init__(self, parent)

        label = Label(self, text="Accueil")
        label.pack(padx=10, pady=10)

        buttonadd = Button(self, text="Ajouter un enfant", bg="yellow", fg="black", command=lambda:controller.show_frame(Ajouter))
        buttonadd.pack()
        buttonsearch = Button(self, text="Rechercher un enfant", bg="orange", fg="black", command=lambda:controller.show_frame(Recherche))
        buttonsearch.pack()

class Ajouter(Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        def callback():
            fonctions.AjoutClient(var_nomEnfant.get(),var_dateDeFete.get(),var_adresse.get())
        Frame.__init__(self, parent)

        label = Label(self, text="Ajouter un enfant")
        label.pack(padx=10, pady=10)

        champ_label = Label(self, text="Nom de l'enfant")
        champ_label.pack()
        var_nomEnfant = StringVar()
        ligne_texte1 = Entry(self, textvariable=var_nomEnfant, width=30)
        ligne_texte1.pack()

        champ_label2 = Label(self, text="Date de fête")
        champ_label2.pack()
        var_dateDeFete = StringVar()
        ligne_texte2 = Entry(self, textvariable=var_dateDeFete, width=30)
        ligne_texte2.pack()

        champ_label3 = Label(self, text="Adresse")
        champ_label3.pack()
        var_adresse = StringVar()
        ligne_texte3 = Entry(self, textvariable=var_adresse, width=30)
        ligne_texte3.pack()

        buttonsummit = Button(self, text="Enregistrer", bg="Orange", fg="black",command=callback)
        buttonsummit.pack()

        buttonadd = Button(self, text="Revenir à l'accueil", bg="yellow", fg="black", command=lambda:controller.show_frame(StartPage))
        buttonadd.pack(side=BOTTOM)

class Recherche(Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        Frame.__init__(self, parent)
        label = Label(self, text="Rechercher un enfant")
        label.pack(padx=10, pady=10)

        champ_label = Label(self, text="Nom de l'enfant")
        champ_label.pack()
        var_nomenfant = StringVar()
        ligne_texte1 = Entry(self, textvariable=var_nomenfant, width=30)
        ligne_texte1.pack()

        buttonrecherche = Button(self, text="Rechercher", bg="Orange", fg="black", command=lambda:[self.controller.donnees_application["nomEnfant"].set(ligne_texte1.get()),controller.show_frame(ResultatRecherche)])
        buttonrecherche.pack()

        buttonadd = Button(self, text="Revenir à l'accueil", bg="yellow", fg="black", command=lambda: controller.show_frame(StartPage))
        buttonadd.pack(side=BOTTOM)

class ListeGlobale:
    def __init__(self):
        self.ListeGlobale=[]
        self.TermeRecherche=""
    def ExecuterRecherche(self, TermeRecherche):
        self.TermeRecherche=TermeRecherche
        for i in fonctions.RechercheClient(TermeRecherche): #Nontype
            self.ListeGlobale.append(i)
        return self.ListeGlobale


class ResultatRecherche(Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        Frame.__init__(self, parent)
        label = Label(self, text="Quel enfant")
        label.pack(padx=30, pady=30)

        champ_label = Label(self, text="Résultat")
        champ_label.pack()
        print(self.controller.donnees_application["nomEnfant"])
        ListeEnfant=ListeGlobale()
        ListeEnfant.ListeGlobale=ListeEnfant.ExecuterRecherche(self.controller.donnees_application["nomEnfant"].get())
        listeResultat = Listbox(self)
        i=1
        for x in ListeEnfant.ListeGlobale:
            listeResultat.insert(i,x)
            i=i+1
        listeResultat.pack()


        buttonprofil = Button(self, text="Aller au profil", bg="Orange", fg="black", command=lambda:controller.show_frame(StartPage))
        buttonprofil.pack()

        buttonadd = Button(self, text="Revenir à l'accueil", bg="yellow", fg="black", command=lambda: controller.show_frame(StartPage))
        buttonadd.pack(side=BOTTOM)

App = App()
App.title("Liste Cadeaux")
App.geometry('1000x800+450+100')

menu = Menu(App)
App.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Menu', menu=filemenu)
filemenu.add_command(label='Exit', command=App.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Aide', menu=helpmenu)
helpmenu.add_command(label='About')

App.mainloop()
