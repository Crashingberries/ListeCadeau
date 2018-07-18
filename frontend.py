from tkinter import *
import fonctions


root = Tk()

def raise_frame(frame):
    frame.tkraise()

def popup(msg):
    popup = Tk()

    popup.title("Erreur!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=20, padx=20) #Il faudrait le placer en focus au milieu de l'écran #Ont peut pas avec tkinter sa depend de chaques écran #well #TA DLAIRE DUN MARTEAU
    Button(popup, text="Ok", command=popup.destroy,takefocus=TRUE).pack()

    popup.mainloop()


def AEnfant():
    if not len(var_dateDeFete.get()):
        popup("Tu dois rentrer quelque chose dans la case nom de l'enfant")
    elif not len(var_dateDeFete.get()):
        popup("Tu dois rentrer quelque chose dans la case date de l'enfant")
    elif not len(var_adresse.get()):
        popup("Tu dois rentrer quelque chose dans la case l'adresse de l'enfant")
    else:
        fonctions.AjoutClient(var_nomEnfant.get(), var_dateDeFete.get(), var_adresse.get())

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
    fonctions.EffacerProduitListe(ProfilEnfantSelectionne.get(0),Temp[0])
    ExecuterModificationsClient(ListeModifCadeaux)

root.title("Liste Cadeaux")
photo = PhotoImage(file='logo.png')
addkid = PhotoImage(file='addkid.png')
look = PhotoImage(file='look.png')
EnregistrementClient=[]

var_editListeCadeaux = StringVar()

StartPage = Frame(root)
Ajouter = Frame(root)
Recherche = Frame(root)
ResultatRecherche = Frame(root)
ProfilEnfant = Frame(root)
ModifProfil = Frame(root)
ModifListe = Frame(root)
AboutPage = Frame(root)

for frame in (StartPage, Ajouter, Recherche, ResultatRecherche, ProfilEnfant, ModifProfil, ModifListe, AboutPage):
    frame.grid(row=0, column=0, sticky='news')

#StartPage
Label(StartPage, text="Accueil", font='Arial 25 bold').pack(pady=22)
Button(StartPage, image=addkid, bg="Orange", command=lambda:raise_frame(Ajouter)).pack()
Button(StartPage, image=look, bg="yellow", command=lambda:raise_frame(Recherche)).pack()
Button(StartPage, image=photo, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)

#Ajouter
Label(Ajouter, text='Ajouter un enfant', font='Arial 25 bold').pack(pady=22)

Label(Ajouter, text="Nom de l'enfant", font='Arial 15 bold').pack(pady=3)
var_nomEnfant = StringVar()
Entry(Ajouter, textvariable=var_nomEnfant, width=30).pack()

Label(Ajouter, text="Date de fête", font='Arial 15 bold', justify='right').pack(pady=3)
var_dateDeFete = StringVar()
Entry(Ajouter, textvariable=var_dateDeFete, width=30).pack()

Label(Ajouter, text="Adresse", font='Arial 15 bold').pack(pady=3)
var_adresse = StringVar()
Entry(Ajouter, textvariable=var_adresse, width=30).pack()

Button(Ajouter, text="Alex Suce", font='Arial 15 bold', bg="Orange", fg="black", command=AEnfant).pack(pady=50)
Button(Ajouter, image=photo, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#Recherche
Label(Recherche, text="Rechercher un enfant", font='Arial 25 bold').pack(pady=22)

Label(Recherche, text="Nom de l'enfant", font='Arial 15 bold').pack()
var_nomEnfantRecherche= StringVar()
listeResultatRechercheEnfant = Listbox(ResultatRecherche, width=50, bd=1, height=10, font='Arial 12')
LabelAdresseProfil=StringVar()
LabelDateProfil=StringVar()
LabelNomProfil=StringVar()
Entry(Recherche, textvariable=var_nomEnfantRecherche, width=30).pack()
Button(Recherche, text="Rechercher", bg="Orange", fg="black", font='Arial 15 bold', command=lambda:[ExecuterRechercheClient(var_nomEnfantRecherche.get(),listeResultatRechercheEnfant),raise_frame(ResultatRecherche)]).pack(pady=50)

Button(Recherche, image=photo, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#ResultatRecherche

Label(ResultatRecherche, text="Quel enfant", font='Arial 25 bold').pack(pady=22)
Label(ResultatRecherche, text="Résultat", font='Arial 15').pack()
ListeCadeaux = Listbox(ProfilEnfant, width=50, bd=1, height=10, font='Arial 12')
ProfilEnfantSelectionne=Listbox()

Button(ResultatRecherche, image=photo, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)
Button(ResultatRecherche, text="Aller au profil", font='Arial 15', bg="Orange", fg="black", command=lambda:[ExecuterRechercheProduitClient(listeResultatRechercheEnfant,ListeCadeaux),raise_frame(ProfilEnfant)]).pack(side=BOTTOM)



#ProfilEnfant
Label(ProfilEnfant, text="Profil Enfant", font='Arial 25 bold').pack(pady=22)
Label(ProfilEnfant, textvariable=LabelNomProfil).pack()
Label(ProfilEnfant, textvariable=LabelDateProfil).pack()
Label(ProfilEnfant, textvariable=LabelAdresseProfil).pack()

ListeCadeaux.pack()

Button(ProfilEnfant, text="Modifier le profil", bg="Orange", fg="black", font='Arial 15',command=lambda:[ExecuterModificationsClient(ListeModifCadeaux),raise_frame(ModifProfil)]).pack()
Button(ProfilEnfant, text="Modifier le Coffre à jouet", bg="Yellow", fg="black", font='Arial 15', command=lambda:[ExecuterModificationsClient(ListeModifCadeaux),raise_frame(ModifListe)]).pack()
Button(ProfilEnfant, image=photo, command=lambda:raise_frame(StartPage)).pack(side=BOTTOM)


#ModifProfil
Label(ModifProfil, text="Modifier le profil", font='Arial 25 bold').pack(pady=22)
Label(ModifProfil, text="Nom").pack()
var_nomEnfantModif = StringVar(value=LabelNomProfil.get())
Entry(ModifProfil, textvariable=var_nomEnfantModif, width=30).pack()
Label(ModifProfil, text="Date").pack()
var_dateDeFeteModif = StringVar(value=LabelDateProfil.get())
Entry(ModifProfil, textvariable=var_dateDeFeteModif, width=30).pack()
Label(ModifProfil, text="Adresse").pack()
var_adresseModif = StringVar(value=LabelAdresseProfil.get())
Entry(ModifProfil, textvariable=var_adresseModif, width=30).pack()


Button(ModifProfil, text="Enregistrer", bg="Orange", fg="black", font='Arial 15', command=lambda:[ModifierProfilEnfant(var_nomEnfantModif.get(),var_dateDeFeteModif.get(),var_adresseModif.get(), ProfilEnfantSelectionne),raise_frame(Recherche)]).pack()

Button(ModifProfil, text="Retour", bg="Yellow", fg="black", font='Arial 15', command=lambda:[ExecuterModificationsClient(ListeCadeaux),raise_frame(ProfilEnfant)]).pack()


#ModifListe
Label(ModifListe, text="Modifier la liste", font='Arial 25 bold').pack(pady=22)
ListeModifCadeaux = Listbox(ModifListe, width=50, bd=1, height=10, font='Arial 12')
ListeModifCadeaux.pack()

BindAdd = Entry(ModifListe, textvariable=var_editListeCadeaux)
BindAdd.pack(pady=10)
Button(ModifListe, text="Supprimer le cadeau sélectionné", bg="Orange", fg="black", font='Arial 15', command=EffacerCadeaux).pack(pady=10)
Button(ModifListe, text="Retour", bg="Yellow", fg="black", font='Arial 15', command=lambda:[ExecuterModificationsClient(ListeCadeaux),raise_frame(ProfilEnfant)]).pack(pady=5)
BindAdd.focus_set()
BindAdd.bind("<Return>",AddCadeaux)



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
