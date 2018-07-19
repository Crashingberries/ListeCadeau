from tkinter import *
import fonctions


root = Tk()

def raise_frame(frame):
    frame.tkraise()

def popup(msg):
    popup = Tk()

    popup.title("Erreur!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=20, padx=20)
    Button(popup, text="Ok", command=popup.destroy,takefocus=TRUE).pack()

    popup.mainloop()


def AEnfant():
    if not len(var_dateDeFete.get()):
        popup("La case nom de l'enfant est vide")
    elif not len(var_dateDeFete.get()):
        popup("La case date est vide")
    elif not len(var_adresse.get()):
        popup("La case adresse est vide")
    else:
        fonctions.AjoutClient(var_nomEnfant.get(), var_dateDeFete.get(), var_adresse.get())
        raise_frame(StartPage)

def ExecuterRechercheClient(TermeRecherche,Liste):
        Liste.delete(0,END)
        i=0
        for x in fonctions.RechercheClient(TermeRecherche): #Nontype
            Liste.insert(i, x)
            i=i+1
        Liste.pack()

def ExecuterRechercheProduitClient(ClientSelectionne,Liste):
        Liste.delete(0,END)
        Temp=ClientSelectionne.get(ClientSelectionne.curselection())
        ProfilEnfantSelectionne.insert(0,Temp[0])
        ProfilEnfantSelectionne.insert(1,Temp[1])
        AvantEffacer=ProfilEnfantSelectionne.get(1)
        ProfilEnfantSelectionne.insert(1,AvantEffacer)
        ProfilEnfantSelectionne.insert(2,Temp[2])
        ProfilEnfantSelectionne.insert(3,Temp[3])
        LabelNomProfil.set(Temp[1])
        LabelDateProfil.set(Temp[2])
        LabelAdresseProfil.set(Temp[3])
        i=0
        for x in fonctions.RechercheListe(ProfilEnfantSelectionne.get(0)): #Nontype
            Liste.insert(i,x)
            i=i+1
        Liste.pack()

def ExecuterModificationsClient(Liste):
    Liste.delete(0,END)
    i=0
    for x in fonctions.RechercheListe(ProfilEnfantSelectionne.get(0)): #Nontype
        Liste.insert(i, x)
        i=i+1
        Liste.pack()

def ModifierProfilEnfant(Nom,Date,Adresse,Enregistrement):
    Modification=[Nom,Date,Adresse]
    fonctions.ModifierClient(Enregistrement.get(0,END), Modification)
    LabelNomProfil.set(Modification[0])
    LabelDateProfil.set(Modification[1])
    LabelAdresseProfil.set(Modification[2])


def AddCadeaux(Liste):
    Message=fonctions.AjoutProduitListe(ProfilEnfantSelectionne.get(0), var_editListeCadeaux.get())
    if Message==None:
        ExecuterModificationsClient(ListeModifCadeaux)
        BindAdd.delete(0, END)
    else:
        popup(Message)

def EffacerCadeaux():
    Temp=ListeModifCadeaux.get(ListeModifCadeaux.curselection())
    fonctions.EffacerProduitListe(ProfilEnfantSelectionne.get(0),Temp[2])
    ExecuterModificationsClient(ListeModifCadeaux)

root.title("Le Coffre à Jouets")
root.wm_iconbitmap('icone.ico')

photo = PhotoImage(file='logo.png')
addkid = PhotoImage(file='addkid3.png')
look = PhotoImage(file='look.png')
lookmini = PhotoImage(file='lookmini.png')
enregistrer = PhotoImage(file='enregistrer2.png')

EnregistrementClient=[]

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
Label(StartPage, text="Accueil", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 25 bold').pack(pady=22)
Button(StartPage, image=addkid, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(Ajouter)).pack(pady=5)
Button(StartPage, image=look, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(Recherche)).pack()
Button(StartPage, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)

#Ajouter
Label(Ajouter, text='Ajouter un enfant', bg="LightCyan2", fg='DarkSlateGray4', font='Arial 25 bold').pack(pady=22)

Label(Ajouter, text="Nom", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 15').pack(pady=3)
var_nomEnfant = StringVar()
Entry(Ajouter, textvariable=var_nomEnfant, width=30).pack()

Label(Ajouter, text="Date de fête", bg="LightCyan2", font='Arial 15', fg='DarkSlateGray4', justify='right').pack(pady=3)
var_dateDeFete = StringVar()
Entry(Ajouter, textvariable=var_dateDeFete, width=30).pack()

Label(Ajouter, text="Adresse", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 15').pack(pady=3)
var_adresse = StringVar()
Entry(Ajouter, textvariable=var_adresse, width=30).pack()

Button(Ajouter, image=enregistrer, bg="LightCyan2", borderwidth=0, command=AEnfant).pack(pady=50)
Button(Ajouter, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#Recherche
Label(Recherche, text="Rechercher un enfant", font='Arial 25 bold', fg='DarkSlateGray4', bg="LightCyan2").pack(pady=22)

Label(Recherche, text="Nom de l'enfant", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 15').pack()
var_nomEnfantRecherche= StringVar()
listeResultatRechercheEnfant = Listbox(ResultatRecherche, width=50, bd=1, height=10, font='Arial 14', fg='Turquoise4')
LabelAdresseProfil=StringVar()
LabelDateProfil=StringVar()
LabelNomProfil=StringVar()
Entry(Recherche, textvariable=var_nomEnfantRecherche, width=30).pack()
Button(Recherche, image=lookmini, bg="LightCyan2", borderwidth=0, command=lambda:[ExecuterRechercheClient(var_nomEnfantRecherche.get(),listeResultatRechercheEnfant),raise_frame(ResultatRecherche)]).pack(pady=50)

Button(Recherche, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#ResultatRecherche

Label(ResultatRecherche, text="Qui?", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 25 bold').pack(pady=22)
Label(ResultatRecherche, text="Résultat", bg="LightCyan2", fg='DarkSlateGray4', font='Arial 15').pack()
ListeCadeaux = Listbox(ProfilEnfant, width=50, bd=1, height=10, font='Arial 12')
ProfilEnfantSelectionne=Listbox()

Button(ResultatRecherche, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)
Button(ResultatRecherche, text="Aller au profil", font='Arial 15', bg="Orange", fg="black", command=lambda:[ExecuterRechercheProduitClient(listeResultatRechercheEnfant,ListeCadeaux),raise_frame(ProfilEnfant)]).pack(side=BOTTOM)



#ProfilEnfant
Label(ProfilEnfant, text="Profil Enfant", font='Arial 25 bold', bg="LightCyan2").pack(pady=22)
Label(ProfilEnfant, textvariable=LabelNomProfil, bg="LightCyan2").pack()
Label(ProfilEnfant, textvariable=LabelDateProfil, bg="LightCyan2").pack()
Label(ProfilEnfant, textvariable=LabelAdresseProfil, bg="LightCyan2").pack()

Label(ProfilEnfant, text="Liste des cadeaux", font='Arial 15', bg="LightCyan2").pack()
ListeCadeaux.pack()

Button(ProfilEnfant, text="Modifier le profil", bg="Orange", fg="black", font='Arial 15',command=lambda:[ExecuterModificationsClient(ListeModifCadeaux),raise_frame(ModifProfil)]).pack(pady=5)
Button(ProfilEnfant, text="Modifier le Coffre à jouet", bg="Yellow", fg="black", font='Arial 15', command=lambda:[ExecuterModificationsClient(ListeModifCadeaux),raise_frame(ModifListe)]).pack(pady=5)
Button(ProfilEnfant, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#ModifProfil
Label(ModifProfil, text="Modifier le profil", font='Arial 25 bold', bg="LightCyan2").pack(pady=22)
Label(ModifProfil, text="Nom", font='Arial 15', bg="LightCyan2").pack()
var_nomEnfantModif = StringVar(value=LabelNomProfil.get())
Entry(ModifProfil, textvariable=var_nomEnfantModif, width=30).pack(pady=5)
Label(ModifProfil, text="Date", font='Arial 15', bg="LightCyan2").pack()
var_dateDeFeteModif = StringVar(value=LabelDateProfil.get())
Entry(ModifProfil, textvariable=var_dateDeFeteModif, width=30).pack(pady=5)
Label(ModifProfil, text="Adresse", font='Arial 15', bg="LightCyan2").pack()
var_adresseModif = StringVar(value=LabelAdresseProfil.get())
Entry(ModifProfil, textvariable=var_adresseModif, width=30).pack(pady=5)


Button(ModifProfil, text="Enregistrer", bg="Orange", fg="black", font='Arial 15', command=lambda:[ModifierProfilEnfant(var_nomEnfantModif.get(),var_dateDeFeteModif.get(),var_adresseModif.get(), ProfilEnfantSelectionne),raise_frame(Recherche)]).pack(pady=10)

Button(ModifProfil, text="Retour", bg="Yellow", fg="black", font='Arial 15', command=lambda:[ExecuterModificationsClient(ListeCadeaux),raise_frame(ProfilEnfant)]).pack()


#ModifListe
Label(ModifListe, text="Modifier la liste", font='Arial 25 bold', bg="LightCyan2").pack(pady=22)
ListeModifCadeaux = Listbox(ModifListe, width=50, bd=1, height=10, font='Arial 12')
ListeModifCadeaux.pack()

BindAdd = Entry(ModifListe, textvariable=var_editListeCadeaux)
BindAdd.pack(pady=10)
Button(ModifListe, text="Supprimer le cadeau sélectionné", bg="Orange", fg="black", font='Arial 15', command=EffacerCadeaux).pack(pady=10)
Button(ModifListe, text="Retour", bg="Yellow", fg="black", font='Arial 15', command=lambda:[ExecuterModificationsClient(ListeCadeaux),raise_frame(ProfilEnfant)]).pack(pady=5)
BindAdd.focus_set()
BindAdd.bind("<Return>",AddCadeaux)

Button(ModifListe, image=photo, bg="LightCyan2", borderwidth=0, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)



#Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Menu', menu=filemenu)
filemenu.add_command(label='Accueil', command=lambda:raise_frame(StartPage))
filemenu.add_command(label='Ajouter', command=lambda:raise_frame(Ajouter))
filemenu.add_command(label='Recherche', command=lambda:raise_frame(Recherche))
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Aide', menu=helpmenu)
helpmenu.add_command(label='About', command=lambda:raise_frame(AboutPage))


#AboutPage
Label(AboutPage, text="Crédit & Copyright By Alex Thibeault et Simon Lafortune", bg="LightCyan2").pack()
Button(AboutPage, image=photo, bg="LightCyan2", command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


raise_frame(StartPage)


root.mainloop()
