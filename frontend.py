from tkinter import *
import fonctions
import time
import datetime


root = Tk()

def raise_frame(frame):
    frame.tkraise()

def popup(msg):
    popup = Tk()

    popup.title("Erreur!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=20, padx=20)
    Button(popup, text="Ok", command=popup.destroy, takefocus=TRUE).pack()

    popup.mainloop()

class Enfant:
    def __init__(self, nom="", adresse="", DateDeFete="",ID=""):
        self.Id=ID
        self.Nom = nom
        self.Adresse = adresse
        self.DateDeFete = DateDeFete
    def __str__ (self) :
        return f'{self.Id}: {self.Nom}, fêté le {self.DateDeFete} au {self.Adresse}'

    def copie(LaSelection):
        self.Nom=LaSelection.Nom
        self.Adresse=LaSelection.Adresse
        self.DateDeFete=LaSelection.DateDeFete
        print(self)

class Produit:
    def __init__(self, cup, Nom="", Prix="0"):
        self.Cup = cup
        self.Nom = Nom
        self.Prix = Prix
    def __str__ (self) :
        return f'{self.Nom}, {self.Prix}$ Code Produit:{self.Cup}'

    def ModifierNom(self,StringsAcorriger):
        y=0
        x=["[","]","(",")","{","}","'",",","END"]
        while x[y]!="END":
            while (StringsAcorriger.count(x[y]))!=0:
                print(StringsAcorriger)
                StringsAcorriger=StringsAcorriger.replace(x[y],"")
                print(StringsAcorriger)
            y+=1
        self.Nom=StringsAcorriger

    def ModifierPrix(self,StringsAcorriger):
        y=0
        x=["[","]","(",")","{","}","'",",","END"]
        while x[y]!="END":
            while (StringsAcorriger.count(x[y]))!=0:
                print(StringsAcorriger)
                StringsAcorriger=StringsAcorriger.replace(x[y],"")
                print(StringsAcorriger)
            y+=1
        self.Prix=StringsAcorriger

def AEnfant():
    if not len(var_dateDeFete.get()):
        popup("La case nom de l'enfant est vide")
    elif not len(var_dateDeFete.get()):
        popup("La case date est vide")
    elif not len(var_adresse.get()):
        popup("La case adresse est vide")
    else:
        LabelIDProfil.set(fonctions.AjoutClient(Enfant(var_nomEnfant.get(), var_adresse.get(), var_dateDeFete.get())))
        ExecuterRechercheProduitClient("",ListeCadeaux)
        raise_frame(ProfilEnfant)
        var_nomEnfant.set("")
        var_dateDeFete.set("")
        var_adresse.set("")

def ExecuterRechercheClient(TermeRecherche,Liste):
        Liste.delete(0,END)
        i=0
        for x in fonctions.RechercheClient(TermeRecherche): #Nontype
            temp=Enfant(x[0],x[1],x[2],x[3])
            Liste.insert(i, temp)
            i=i+1
        Liste.pack()
        var_nomEnfantRecherche.set("")

def ExecuterRechercheProduitClient(ListeDesEnfant,ListeDesCadeaux,ValeurAchete=0,ListeAdditionnelle=""):
        ListeDesCadeaux.delete(0, END)
        if ListeDesEnfant!="":
            Temp=ListeDesEnfant.get(ACTIVE)
            EnregistrementClient=fonctions.InfoClient(Enfant(ID=Temp[0:Temp.find(":")]))
        else:
            EnregistrementClient=fonctions.InfoClient(Enfant(ID=LabelIDProfil.get()))
        LabelIDProfil.set(EnregistrementClient.Id)
        LabelNomProfil.set(EnregistrementClient.Nom)
        LabelAdresseProfil.set(EnregistrementClient.Adresse)
        LabelDateProfil.set(EnregistrementClient.DateDeFete)
        i=0
        if ListeAdditionnelle!="":
            ListeAdditionnelle.delete(0, END)
            for x in fonctions.RechercheListe(EnregistrementClient.Id,1):
                temp = Produit(x[2],x[0],x[1])
                temp.ModifierNom=(temp.Nom)
                temp.ModifierPrix=(temp.Prix)
                ListeAdditionnelle.insert(i,temp)
                i=i+1
            ListeAdditionnelle.pack()
        for x in fonctions.RechercheListe(EnregistrementClient.Id,ValeurAchete):
            temp = Produit(x[2],x[0],x[1])
            temp.ModifierNom=(temp.Nom)
            temp.ModifierPrix=(temp.Prix)
            ListeDesCadeaux.insert(i,temp)
            i=i+1
        ListeDesCadeaux.pack()


def ExecuterModificationsClient(Liste):
    Liste.delete(0,END)
    i=0
    for x in fonctions.RechercheListe(LabelIDProfil.get()):
        temp = Produit(x[2],x[0],x[1])
        temp.ModifierNom=(temp.Nom)
        temp.ModifierPrix=(temp.Prix)
        Liste.insert(i,temp)
        i=i+1
    Liste.pack()
    BindAdd.focus_set()

def ModifierProfilEnfant(Nom,Date,Adresse,Enregistrement):
    Modification=[Nom,Date,Adresse]
    fonctions.ModifierClient(Enregistrement.get(0,END), Modification)
    LabelNomProfil.set(Modification[0])
    LabelDateProfil.set(Modification[1])
    LabelAdresseProfil.set(Modification[2])


def AddCadeaux(Liste):
    Message=fonctions.AjoutProduitListe(LabelIDProfil.get(), Produit(var_editListeCadeaux.get()))
    if Message==None:
        ExecuterModificationsClient(ListeModifCadeaux)
        BindAdd.delete(0, END)
    else:
        popup(Message)

def ChangerListeCadeau():
        if ListeCadeaux.curselection():
            Temp=ListeCadeaux.get(ACTIVE)
            print('ListeCadeau')
            fonctions.ChangerListeCadeau(LabelIDProfil.get(),Temp[Temp.rfind(":")+1:len(Temp)],1)
        elif ListeCadeauxAcheter.curselection():
            Temp=ListeCadeauxAcheter.get(ACTIVE)
            print("ListeCadeauxAcheter")
            fonctions.ChangerListeCadeau(LabelIDProfil.get(),Temp[Temp.rfind(":")+1:len(Temp)],0)
        ExecuterRechercheProduitClient("",ListeCadeaux,0)
        ExecuterRechercheProduitClient("",ListeCadeauxAcheter,1)

def EffacerCadeaux():
    Temp=ListeModifCadeaux.get(ACTIVE)
    fonctions.EffacerProduitListe(LabelIDProfil.get(),Temp[Temp.rfind(":")+1:len(Temp)])
    ExecuterModificationsClient(ListeModifCadeaux)


root.title("Le Coffre à Jouets")
root.wm_iconbitmap('icone.ico')

photo = PhotoImage(file='logo.png')
addkid = PhotoImage(file='addkid3.png')
look = PhotoImage(file='look.png')
lookmini = PhotoImage(file='lookmini.png')
enregistrer = PhotoImage(file='enregistrer2.png')
AProfil = PhotoImage(file='AProfil.png')
MProfil = PhotoImage(file='MProfil.png')
ACoffre = PhotoImage(file='MCoffre.png')
Retour = PhotoImage(file='Retour.png')
Supprimer = PhotoImage(file='Supprimer.png')


EnregistrementClient=Enfant()

var_editListeCadeaux = StringVar()

StartPage = Frame(root, bg="LightCyan2")
Ajouter = Frame(root, bg="LightCyan2")
Recherche = Frame(root, bg="LightCyan2")
ResultatRecherche = Frame(root, bg="LightCyan2")
ProfilEnfant = Frame(root, bg="LightCyan2")
ModifProfil = Frame(root, bg="LightCyan2")
ModifListe = Frame(root, bg="LightCyan2")
AboutPage = Frame(root, bg="LightCyan2")

for frame in (StartPage, Ajouter, Recherche, ResultatRecherche, ProfilEnfant, ModifProfil, ModifListe, AboutPage):
    frame.grid(row=0, column=0, sticky='news')


#StartPage
Label(StartPage, text="Accueil", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 20 bold').pack(pady=22)
Button(StartPage, image=addkid, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(Ajouter)).pack(pady=5)
Button(StartPage, image=look, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(Recherche)).pack()
Button(StartPage, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#Ajouter
Label(Ajouter, text='Ajouter un enfant', bg="LightCyan2", fg='DarkSlateGray4', font='Arial 20 bold').pack(pady=22)

Label(Ajouter, text="Nom", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 15').pack(pady=3)
var_nomEnfant = StringVar()
entryNom = Entry(Ajouter, textvariable=var_nomEnfant, width=30).pack()

Label(Ajouter, text="Date de fête", bg="LightCyan2", font='Arial 15', fg='DarkSlateGray4', justify='right').pack(pady=3)
var_dateDeFete = StringVar()
entryDate = Entry(Ajouter, textvariable=var_dateDeFete, width=30).pack()

Label(Ajouter, text="Adresse", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 15').pack(pady=3)
var_adresse = StringVar()
entryAdresse = Entry(Ajouter, textvariable=var_adresse, width=30).pack()

Button(Ajouter, image=enregistrer, bg="LightCyan2", borderwidth=0, command=AEnfant).pack(pady=50)
Button(Ajouter, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#Recherche
Label(Recherche, text="Rechercher un enfant", font='Arial 20 bold', fg='DarkSlateGray4', bg="LightCyan2").pack(pady=22)

Label(Recherche, text="Nom de l'enfant", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 15').pack()
var_nomEnfantRecherche= StringVar()
listeResultatRechercheEnfant = Listbox(ResultatRecherche, width=50, bd=1, height=10, font='Arial 14', fg='Turquoise4')
LabelAdresseProfil=StringVar()
LabelDateProfil=StringVar()
LabelNomProfil=StringVar()
LabelIDProfil=StringVar()
rechercheEntry = Entry(Recherche, textvariable=var_nomEnfantRecherche, width=30).pack()
Button(Recherche, image=lookmini, bg="LightCyan2", borderwidth=0, command=lambda:[ExecuterRechercheClient(var_nomEnfantRecherche.get(),listeResultatRechercheEnfant),raise_frame(ResultatRecherche)]).pack(pady=50)

Button(Recherche, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#ResultatRecherche
Label(ResultatRecherche, text="Quel enfant?", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 20 bold').pack(pady=22)
Label(ResultatRecherche, text="Reusltat", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 15').pack()
ListeCadeaux = Listbox(ProfilEnfant, width=75, bd=1, height=5, font='Arial 10', fg='DarkSlateGray4')
ListeCadeauxAcheter = Listbox(ProfilEnfant, width=75, bd=1, height=5, font='Arial 10', fg='salmon1')

Button(ResultatRecherche, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)
Button(ResultatRecherche, image=AProfil, bg="LightCyan2", borderwidth=0, command=lambda:[ExecuterRechercheProduitClient(listeResultatRechercheEnfant,ListeCadeaux,0,ListeCadeauxAcheter),raise_frame(ProfilEnfant)]).pack(side=BOTTOM)


#ProfilEnfant
Label(ProfilEnfant, text="Profil Enfant", font='Arial 20 bold', bg="LightCyan2", fg='DarkSlateGray4').pack(pady=22)
Label(ProfilEnfant, textvariable=LabelNomProfil, font='Arial 14', bg="LightCyan2", fg='DarkSlateGray4').pack()
Label(ProfilEnfant, textvariable=LabelDateProfil, font='Arial 14', bg="LightCyan2", fg='DarkSlateGray4').pack()
Label(ProfilEnfant, textvariable=LabelAdresseProfil, font='Arial 14', bg="LightCyan2", fg='DarkSlateGray4').pack()

Label(ProfilEnfant, text="Liste des cadeaux", font='Arial 12', bg="LightCyan2", fg='DarkSlateGray4').pack()
ListeCadeaux.pack()
Button(ProfilEnfant, text="Déjà Acheté", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 12', borderwidth=0, command=lambda:ChangerListeCadeau()).pack()
ListeCadeauxAcheter.pack()

Button(ProfilEnfant, image=MProfil, bg="LightCyan2", borderwidth=0, command=lambda:[ExecuterModificationsClient(ListeModifCadeaux),raise_frame(ModifProfil)]).pack(pady=5)
Button(ProfilEnfant, image=ACoffre, bg="LightCyan2", borderwidth=0, command=lambda:[ExecuterModificationsClient(ListeModifCadeaux),raise_frame(ModifListe)]).pack(pady=5)
Button(ProfilEnfant, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#ModifProfil
Label(ModifProfil, text="Modifier le profil", font='Arial 20 bold', bg="LightCyan2", fg='DarkSlateGray4').pack(pady=22)
Label(ModifProfil, text="Nom", font='Arial 15', bg="LightCyan2", fg='DarkSlateGray4').pack()
var_nomEnfantModif = StringVar(value=LabelNomProfil.get())
Entry(ModifProfil, textvariable=var_nomEnfantModif, width=30).pack(pady=5)
Label(ModifProfil, text="Date", font='Arial 15', bg="LightCyan2", fg='DarkSlateGray4').pack()
var_dateDeFeteModif = StringVar(value=LabelDateProfil.get())
Entry(ModifProfil, textvariable=var_dateDeFeteModif, width=30).pack(pady=5)
Label(ModifProfil, text="Adresse", font='Arial 15', bg="LightCyan2", fg='DarkSlateGray4').pack()
var_adresseModif = StringVar(value=LabelAdresseProfil.get())
Entry(ModifProfil, textvariable=var_adresseModif, width=30).pack(pady=5)

Button(ModifProfil, image=enregistrer, bg="LightCyan2", borderwidth=0, command=lambda:[ModifierProfilEnfant(var_nomEnfantModif.get(),var_dateDeFeteModif.get(),var_adresseModif.get(), ProfilEnfantSelectionne),raise_frame(Recherche)]).pack(pady=10)
Button(ModifProfil, image=Retour, bg="LightCyan2", borderwidth=0, command=lambda:[ExecuterModificationsClient(ListeCadeaux),raise_frame(ProfilEnfant)]).pack()
Button(ModifProfil, image=photo, bg="LightCyan2",  borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)

#ModifListe
Label(ModifListe, text="Modifier la liste", font='Arial 20 bold', bg="LightCyan2", fg='DarkSlateGray4').pack(pady=22)
ListeModifCadeaux = Listbox(ModifListe, width=60, bd=1, height=10, font='Arial 12', fg='DarkSlateGray4')
ListeModifCadeaux.pack()

BindAdd = Entry(ModifListe, textvariable=var_editListeCadeaux)
BindAdd.pack(pady=10)
BindAdd.focus_set()
Button(ModifListe, image=Supprimer, bg="LightCyan2", borderwidth=0, command=EffacerCadeaux).pack(pady=10)
Button(ModifListe, image=Retour, bg="LightCyan2", borderwidth=0, command=lambda:[ExecuterModificationsClient(ListeCadeaux),raise_frame(ProfilEnfant)]).pack(pady=5)
BindAdd.bind("<Return>", AddCadeaux)

Button(ModifListe, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Menu', menu=filemenu)
filemenu.add_command(label='Accueil', command=lambda:raise_frame(StartPage))
filemenu.add_separator()
filemenu.add_command(label='Ajouter', command=lambda:raise_frame(Ajouter))
filemenu.add_separator()
filemenu.add_command(label='Recherche', command=lambda:raise_frame(Recherche))
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Aide', menu=helpmenu)
helpmenu.add_command(label='About', command=lambda:raise_frame(AboutPage))


#AboutPage
Label(AboutPage, text="About", font='Arial 20 bold', bg="LightCyan2", fg='DarkSlateGray4').pack(pady=22)
Label(AboutPage, text="Crédit & Copyright By Alex Thibeault et Simon Lafortune", bg="LightCyan2").pack()
Button(AboutPage, image=photo, bg="LightCyan2",  borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)

jours = datetime.datetime.today().weekday()
if jours == 0:
    Label(AboutPage, text="Bonne semaine, nous sommes Lundi.", bg="LightCyan2").pack()
elif jours == 1:
    Label(AboutPage, text="Nous sommes Mardi.", bg="LightCyan2").pack()
elif jours == 2:
    Label(AboutPage, text="Mercredi, ben oui, MERCREDI!", bg="LightCyan2").pack()
elif jours == 3:
    Label(AboutPage, text="Jeudi!", bg="LightCyan2").pack()
elif jours == 4:
    Label(AboutPage, text="Vendredi, ouuuhh", bg="LightCyan2").pack()
elif jours == 5:
    Label(AboutPage, text="Samedi, Woupi!", bg="LightCyan2").pack()
elif jours == 6:
    Label(AboutPage, text="Bon Dimanche", bg="LightCyan2").pack()

Label(AboutPage, text="L'application est ouverte depuis :", bg="LightCyan2").pack()
leTemps = time.strftime('%H:%M:%S')
leTemps = Label(AboutPage, text=leTemps, compound=CENTER, bg="LightCyan2")
leTemps.pack()


raise_frame(StartPage)
root.mainloop()
