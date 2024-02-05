# Import des differents biblihotèques
import tkinter
import mysql.connector
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox

def Retour():
    root.destroy()
    call(["python", "main.py"])
    
def Ajouter():
    nom = txtName.get()
    prix_achat = txtPrix.get()
    quantite_achat = txtQuantite.get()
    id_category = txtid_category.get()
    description = txtdescription.get()

    BaseMysql = mysql.connector.connect(host="localhost", user="root", password="Azertyuiop123", database="store")
    Mysql = BaseMysql.cursor()

    try:
        sql = "INSERT INTO product (name, price, quantity, id_category, description) VALUES (%s, %s, %s, %s, %s)"
        val = (nom, prix_achat, quantite_achat, id_category, description)
        Mysql.execute(sql, val)
        BaseMysql.commit()
        messagebox.showinfo("information", "Produit ajouter")
        root.destroy()
        call(["python", "Achats.py"])

    except Exception as e:
        print(e)
        BaseMysql.rollback()

def Modifier():
    nom = txtName.get()
    prix_achat = txtPrix.get()
    quantite_achat = txtQuantite.get()
    id_category = txtid_category.get()
    description = txtdescription.get()

    BaseMysql = mysql.connector.connect(host="localhost", user="root", password="Azertyuiop123", database="store")
    Mysql = BaseMysql.cursor()

    try:
        sql = "UPDATE product SET name=%s, price=%s, quantity=%s, id_category=%s, description=%s"
        val = (nom, prix_achat, quantite_achat, id_category, description)
        Mysql.execute(sql, val)
        BaseMysql.commit()
        messagebox.showinfo("information", "Produit modifier")
        root.destroy()
        call(["python", "Achats.py"])

    except Exception as e:
        print(e)
        BaseMysql.rollback()

def Supprimer():
    nom = txtName.get()
    
    BaseMysql = mysql.connector.connect(host="localhost", user="root", password="Azertyuiop123", database="store")
    Mysql = BaseMysql.cursor()

    try:
        sql = "DELETE FROM product"
        val = (nom)
        Mysql.execute(sql, val)
        BaseMysql.commit()
        messagebox.showinfo("Information", "Produit supprimer")
        root.destroy()
        call(["python", "Achats.py"])

    except Exception as e:
        print(e)
        BaseMysql.rollback()
#--------------------------------------------------

root = Tk()

   # Attribution des paramètres Tkinter (Titre, dimensions et non modification de celle-ci, taille de fond)
root.title("ACHATS")
root.geometry("800x450")
root.resizable(False, False)
root.configure(background="#808080")

#-----------------------------------------
   # Création de la variable titre afin d'habiller ma fenêtre (Noms, Police et taille, Couleur de fond, couleur du titre)
titre = Label(root,borderwidth = 1, relief = SUNKEN ,
              text = "GESTION DES ACHATS", font =("Sans Serif", 25), background = "#8080FF", foreground="white")
titre.place(x = 100, y = 0, width =600) # Attribution de paramètres pour placer l'ecriture sur la fenêtre

    #Création de plusieurs variables afin d'afficher les informations de la base (Mac,Prix,Quantité,télephone)
nom = Label(root, text="Nom", font=("Arial", 18), background="#808080", foreground="White")
nom.place(x=0, y=50, width=100)
txtName = Entry(root, bd=4, font=("Arial", 14))
txtName.place(x = 90, y = 50, width =200)

prix_achat = Label(root, text="Prix", font=("Arial", 18), background="#808080", foreground="White")
prix_achat.place(x=0, y=90, width=90)
txtPrix = Entry(root, bd=4, font=("Arial", 14))
txtPrix.place(x =80, y =90, width =100)

quantite_achat = Label(root, text="Quantité", font=("Arial", 18), background="#808080", foreground="White")
quantite_achat.place(x=0, y=130, width=100)
txtQuantite = Entry(root, bd=4, font=("Arial", 14))
txtQuantite.place(x =110, y =130, width =60)

id_category = Label(root, text="Categorie", font=("Arial", 18), background="#808080", foreground="white")
id_category.place(x =15, y =170, width=100)
txtid_category = Entry(root, bd=4, font=("Arial", 14))
txtid_category.place(x  =130, y =170, width=100)

description = Label(root, text="Description", font=("Arial", 18), background="#808080", foreground="white")
description.place(x =0, y =210, width=190)
txtdescription = Entry(root, bd=4, font=("Arial", 14))
txtdescription.place(x  =160, y =210, width=300)

#-----------------------------------------

    #Buttons 

Ajoutproduit = Button(root, text ="Ajouter", font = ("Arial", 16), background="#8080FF", foreground="White", command=Ajouter)
Ajoutproduit.place(x=600, y=150, width=200)

SupprimerProduits = Button(root, text ="Supprimer", font = ("Arial", 16), background="#8080FF", foreground="White", command=Supprimer)
SupprimerProduits.place(x=600, y=50, width=200)

ModifierProduits = Button(root, text ="Modifier", font = ("Arial", 16), background="#8080FF", foreground="White", command=Modifier)
ModifierProduits.place(x=600, y=100, width=200)

bRetour = Button(root, text ="Retour", font = ("Arial", 16), background="Red", foreground="White", command=Retour)
bRetour.place(x=600, y=200, width=200)

#------------------------------------------

    #Variable tableau

table = ttk.Treeview(root, columns= (0, 1, 2, 3, 4, 5), height= 10, show ='headings')
table.place(x =0,y = 250, width= 800, height= 450)

    #Permets de nomée les colonnes
table.heading(0, text ='ID')
table.heading(1, text ='Nom')
table.heading(3, text ='Prix')
table.heading(4, text ='Quantite')
table.heading(2, text ='Description')
table.heading(5, text ='Categorie')

    #Permets d'établir la largeur des colonnes
table.column(0, width= 2)
table.column(1, width= 10)
table.column(2, width= 40)
table.column(3, width= 10)
table.column(4, width= 5)
table.column(5, width= 30)
#----------------------------------

    #affiche les informations de la table
BaseMysql = mysql.connector.connect(host="localhost", user="root", password="Azertyuiop123", database="store")
Mysql = BaseMysql.cursor()
Mysql.execute("SELECT * FROM product;")
for row in Mysql:
    table.insert("", END, value = row)
BaseMysql.close()


    #Execution 
root.mainloop()