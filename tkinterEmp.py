from tkinter import *
from employer import employer
import tkinter.ttk as ttk

class GestionEmployer():
    def __init__(self,root):
        self.root = root
        self.root.geometry('600x600')
        self.root.title("Gestion Employer")
        self.Id=StringVar()
        self.nom=StringVar()
        self.prenom=StringVar()
        self.categorie=StringVar()
        self.salaire=StringVar()
    #Formulaire ajout Etudiant dans __init():
        #==============Num employer TEXTFIELD AND LABEL
        Id_employer_lbl = Label(self.root,text = "Id employer",anchor='w')
        Id_employer_lbl.grid(row = 1,column = 0,padx = 40,pady = 40)
        Id_employer_field = Entry(self.root,textvariable = self.Id)
        Id_employer_field.grid(row = 1,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #==============Nom employer TEXTFIELD AND LABEL
        nom_employer_lbl = Label(self.root,text = "Nom employer",anchor='w')
        nom_employer_lbl.grid(row = 2,column = 0,padx = 40,pady = 40)
        nom_employer_field = Entry(self.root,textvariable = self.nom)
        nom_employer_field.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================Prenom employer LABEL AND TEXTFIELD
        prenom_lbl = Label(self.root,text="Prénom employer",anchor='w')
        prenom_lbl.grid(row = 3,column = 0,pady = 40)
        prenom_field = Entry(self.root,textvariable = self.prenom)
        prenom_field.grid(row = 3,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================categorie employer LABEL AND TEXTFIELD
        categorie_lbl = Label(self.root,text="Catégorie",anchor='w')
        categorie_lbl.grid(row = 4,column = 0,pady = 40)
        categorie_field = Entry(self.root,textvariable = self.categorie)
        categorie_field.grid(row = 4,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================salaire employer LABEL AND TEXTFIELD
        salaire_lbl = Label(self.root,text="Salaire",anchor='w')
        salaire_lbl.grid(row = 5,column = 0,pady = 40)
        salaire_field = Entry(self.root,textvariable = self.salaire)
        salaire_field.grid(row = 5,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=====================Boutton ajout
        ajou_employer_btn = Button(self.root,text = "Ajouter",command = self.add,anchor='c')
        ajou_employer_btn.grid(row = 6,column = 0,ipady = 4,ipadx = 13,pady = 40)
          
        #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        affich_employer_btn = Button(self.root,text = "Afficher",command = self.view,anchor='c')
        affich_employer_btn.grid(row = 6,column = 1,ipady = 4,ipadx = 13,pady = 40)
        
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_employer_btn = Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        supp_employer_btn.grid(row = 6,column = 2,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton modifier à ajouter après boutton "Afficher" dans __init()__
        modif_employer_btn = Button(self.root,text = "Modifier",command = self.update,anchor='c')
        modif_employer_btn.grid(row = 6,column = 3,ipady = 4,ipadx = 13,pady = 40)

        
        #Fonction d'ajout d'un étudiant (sera appelée dérière le boutton "Ajouter"
    def add(self):
        E = employer (self.Id.get(),self.nom.get(),self.prenom.get(),self.categorie.get(),self.salaire.get())
        E.ajouterEmployer()
    def view(self):
        #self.root.title("Student Management(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('700x300')
        self.root.title("Gestion des employers)")
        show_frame = Frame(self.root)
        show_frame.place(width = 800,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage des employer")
        labl_show.pack()
        #========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 600,height = 200,x = 8,y = 58)
        tree = ttk.Treeview(main_frame,height = 200)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3","4","5")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "Id",anchor='c')
        tree.heading("2",text = "Nom",anchor='w')
        tree.heading("3",text = "Prenom",anchor='w')
        tree.heading("4",text="Categorie",anchor='w')
        tree.heading("5",text="salaire",anchor='w')
        E=employer()
        rows=E.afficherEmployer()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}'))
            j+=1
    #Fonction dse suppression d'un étudiant sera appelée dans le boutton "Supprimer"  
    def remove(self):
        E = employer()
        E.supprimerEmployer(self.Id.get())
    #Fonction dse suppression d'un étudiant sera appelée dans le boutton "Supprimer"  
    def update(self):
        E = employer(self.Id.get(),self.nom.get(),self.prenom.get(),self.categorie.get(),self.salaire.get())
        E.modifierEmployer(self.Id.get())

#if __name__ == "__main__":
root = Tk()
l = GestionEmployer(root)
root.mainloop()
