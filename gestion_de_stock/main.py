    # Import des differents biblihotèques
from subprocess import call
from tkinter import *


    #Création de la fontion Achats & Ventes enfin de permettre l'ouverture des fichier Achats.py et Ventes.py
def Liste_produits():
    root.destroy()
    call(["python", "Produits.py"])

    # Création de variable Tkinter
root = Tk()

    # Attribution des paramètres Tkinter (Titre, dimensions et non modification de celle-ci, taille de fond)
root.title("GESTION DE STOCK")
root.geometry("600x200")
root.resizable(False, False)
root.configure(background="grey")

    # Création de la variable titre afin d'habiller ma fenêtre (Noms, Police et taille, Couleur de fond, couleur du titre)
titre = Label(root,borderwidth = 1, relief = SUNKEN ,
              text = "Stocks", font =("Sans Serif", 25), background = "#8080FF", foreground="white")
titre.place(x = 0, y = 0, width =600) # Attribution de paramètres pour placer l'ecriture sur la fenêtre

    #Ajout de la variable Buttons sur le menue (Achats, ventes)
enregistrer = Button(root, text = 'Produits', font =('Arial', 23), bg ='#8080FF', fg ='white', command=Liste_produits)
enregistrer.place(x=200, y=100, width=200)

root.mainloop()