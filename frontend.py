from tkinter import *
import fonctions

def raise_frame(frame):
    frame.tkraise()

def AEnfant():
    fonctions.AjoutClient(var_nomEnfant.get(), var_dateDeFete.get(), var_adresse.get())

def ExecuterRechercheClient(TermeRecherche,Liste):
        Liste.delete(0,END)
        i=0
        for x in fonctions.RechercheClient(TermeRecherche): #Nontype
            Liste.insert(i, x)
            i=i+1
        Liste.pack()

def ExecuterRechercheProduit(ClientSelectionne,Liste):
        Liste.delete(0,END)
        Temp=ClientSelectionne.get(ClientSelectionne.curselection())
        ProfilEnfantSelectionne.insert(1,Temp[1])
        ProfilEnfantSelectionne.insert(2,Temp[2])
        ProfilEnfantSelectionne.insert(3,Temp[3])
        ProfilEnfantSelectionne.insert(0,Temp[0])
        LabelNomProfil.set(Temp[1])
        LabelDateProfil.set(Temp[2])
        LabelAdresseProfil.set(Temp[3])
        i=0
        for x in fonctions.RechercheListe(Temp[0]): #Nontype
            Liste.insert(i, x)
            i=i+1
        Liste.pack()

def ModifierProfilEnfant(Nom,Date,Adresse,Enregistrement):
    Modification=[Nom,Date,Adresse]
    fonctions.ModifierClient(Enregistrement.get(0,END), Modification)
    LabelNomProfil.set(Modification[0])
    LabelDateProfil.set(Modification[1])
    LabelAdresseProfil.set(Modification[2])

#def AddCadeaux():


root = Tk()
root.title("Liste Cadeaux")
photo = PhotoImage(file='logo.png')
addkid = PhotoImage(file='addkid.png')
look = PhotoImage(file='look.png')
EnregistrementClient=[]

StartPage = Frame(root)
Ajouter = Frame(root)
Recherche = Frame(root)
ResultatRecherche = Frame(root)
ProfilEnfant = Frame(root)
ModifProfil = Frame(root)
AboutPage = Frame(root)

for frame in (StartPage, Ajouter, Recherche, ResultatRecherche, ProfilEnfant, ModifProfil, AboutPage):
    frame.grid(row=0, column=0, sticky='news')

#StartPage
Label(StartPage, text="Accueil", font='Courier 25 bold').pack()
Button(StartPage, image=addkid, bg="Orange", command=lambda:raise_frame(Ajouter)).pack()
Button(StartPage, image=look, bg="yellow", command=lambda:raise_frame(Recherche)).pack()
Button(StartPage, image=photo, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)

#Ajouter
Label(Ajouter, text='Ajouter un enfant', font='Courier 25 bold').pack()

Label(Ajouter, text="Nom de l'enfant").pack()
var_nomEnfant = StringVar()
Entry(Ajouter, textvariable=var_nomEnfant, width=30).pack()

Label(Ajouter, text="Date de fête").pack()
var_dateDeFete = StringVar()
Entry(Ajouter, textvariable=var_dateDeFete, width=30).pack()

Label(Ajouter, text="Adresse").pack()
var_adresse = StringVar()
Entry(Ajouter, textvariable=var_adresse, width=30).pack()

Button(Ajouter, text="Enregistrer", font='Courier 12 bold', bg="Orange", fg="black", command=AEnfant).pack()
Button(Ajouter, image=photo, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#Recherche
Label(Recherche, text="Rechercher un enfant", font='Courier 25 bold').pack()

Label(Recherche, text="Nom de l'enfant").pack()
var_nomEnfantRecherche= StringVar()
listeResultatRechercheEnfant = Listbox(ResultatRecherche)
LabelAdresseProfil=StringVar()
LabelDateProfil=StringVar()
LabelNomProfil=StringVar()
Entry(Recherche, textvariable=var_nomEnfantRecherche, width=30).pack()
Button(Recherche, text="Rechercher", bg="Orange", fg="black", command=lambda:[ExecuterRechercheClient(var_nomEnfantRecherche.get(),listeResultatRechercheEnfant),raise_frame(ResultatRecherche)]).pack()

Button(Recherche, image=photo, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#ResultatRecherche

Label(ResultatRecherche, text="Quel enfant", font='Courier 25 bold').pack()
Label(ResultatRecherche, text="Résultat").pack()
ListeCadeaux = Listbox(ProfilEnfant)
ProfilEnfantSelectionne=Listbox()
Button(ResultatRecherche, text="Aller au profil", bg="Orange", fg="black", command=lambda:[ExecuterRechercheProduit(listeResultatRechercheEnfant,ListeCadeaux),raise_frame(ProfilEnfant)]).pack()
Button(ResultatRecherche, image=photo, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#ProfilEnfant
Label(ProfilEnfant, text="Profil Enfant", font='Courier 25 bold').pack()
Label(ProfilEnfant, textvariable=LabelNomProfil).pack()
Label(ProfilEnfant, textvariable=LabelDateProfil).pack()
Label(ProfilEnfant, textvariable=LabelAdresseProfil).pack()

ListeCadeaux.pack()

Button(ProfilEnfant, text="Modifier le profil", bg="Orange", fg="black", command=lambda:raise_frame(ModifProfil)).pack()
Button(ProfilEnfant, image=photo, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)



#ModifProfil
Label(ModifProfil, text="Profil Enfant", font='Courier 25 bold').pack()
Label(ModifProfil, text="Nom").pack()
var_nomEnfantModif = StringVar(value=LabelNomProfil.get())
Entry(ModifProfil, textvariable=var_nomEnfantModif, width=30).pack()
Label(ModifProfil, text="Date").pack()
var_dateDeFeteModif = StringVar(value=LabelDateProfil.get())
Entry(ModifProfil, textvariable=var_dateDeFeteModif, width=30).pack()
Label(ModifProfil, text="Adresse").pack()
var_adresseModif = StringVar(value=LabelAdresseProfil.get())
Entry(ModifProfil, textvariable=var_adresseModif, width=30).pack()

Button(ModifProfil, text="Enregistrer", bg="Orange", fg="black", command=lambda:[ModifierProfilEnfant(var_nomEnfantModif.get(),var_dateDeFeteModif.get(),var_adresseModif.get(),ProfilEnfantSelectionne),raise_frame(ProfilEnfant)]).pack()
Button(ModifProfil, text="Retour", bg="Yellow", fg="black", command=lambda:raise_frame(ProfilEnfant)).pack()
#ButtonCadeaux = Button(ModifProfil, text="Ajouter Cadeaux", bg="Orange", fg="black").pack()
#ButtonCadeaux.bind("<Return>", AddCadeaux)

#Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Menu', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Aide', menu=helpmenu)
helpmenu.add_command(label='About', command=lambda:raise_frame(AboutPage))


#AboutPage
Label(AboutPage, text="Crédit & Copyright By Alex Thibeault et Simon Lafortune").pack()
Button(AboutPage, image=photo, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)

raise_frame(StartPage)


root.mainloop()
