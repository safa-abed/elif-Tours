from tkinter import *
from departement import departement
import tkinter.ttk as ttk

class GestionDepartement():
    def __init__(self,root):
        self.root = root
        self.root.geometry('600x600')
        self.root.title("Gestion Departement")
        self.Id=StringVar()
        self.nomDep=StringVar()
        self.nomResp=StringVar()
        self.anciennete=StringVar()
        self.jourConj=StringVar()
    #Formulaire ajout Etudiant dans __init():
        #==============Num employer TEXTFIELD AND LABEL
        Id_departement_lbl = Label(self.root,text = "Id ",anchor='w')
        Id_departement_lbl.grid(row = 1,column = 0,padx = 40,pady = 40)
        Id_departement_field = Entry(self.root,textvariable = self.Id)
        Id_departement_field.grid(row = 1,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #==============Nom employer TEXTFIELD AND LABEL
        nomDep_departement_lbl = Label(self.root,text = "Nom Departement",anchor='w')
        nomDep_departement_lbl.grid(row = 2,column = 0,padx = 40,pady = 40)
        nomDep_departement_field = Entry(self.root,textvariable = self.nomDep)
        nomDep_departement_field.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================Prenom employer LABEL AND TEXTFIELD
        nomResp_lbl = Label(self.root,text="Nom Responsable",anchor='w')
        nomResp_lbl.grid(row = 3,column = 0,pady = 40)
        nomResp_field = Entry(self.root,textvariable = self.nomResp)
        nomResp_field.grid(row = 3,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================categorie employer LABEL AND TEXTFIELD
        anciennete_lbl = Label(self.root,text="anciennete",anchor='w')
        anciennete_lbl.grid(row = 4,column = 0,pady = 40)
        anciennete_field = Entry(self.root,textvariable = self.anciennete)
        anciennete_field.grid(row = 4,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================salaire employer LABEL AND TEXTFIELD
        jourConj_lbl = Label(self.root,text="jour congé",anchor='w')
        jourConj_lbl.grid(row = 5,column = 0,pady = 40)
        jourConj_field = Entry(self.root,textvariable = self.jourConj)
        jourConj_field.grid(row = 5,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=====================Boutton ajout
        ajou_departement_btn = Button(self.root,text = "Ajouter",command = self.add,anchor='c')
        ajou_departement_btn.grid(row = 6,column = 0,ipady = 4,ipadx = 13,pady = 40)
          
        #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        affich_departement_btn = Button(self.root,text = "Afficher",command = self.view,anchor='c')
        affich_departement_btn.grid(row = 6,column = 2,ipady = 4,ipadx = 13,pady = 40)
        
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_departement_btn = Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        supp_departement_btn.grid(row = 6,column = 1,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton modifier à ajouter après boutton "Afficher" dans __init()__
        modif_departement_btn = Button(self.root,text = "Modifier",command = self.update,anchor='c')
        modif_departement_btn.grid(row = 6,column = 3,ipady = 4,ipadx = 13,pady = 40)

        
        #Fonction d'ajout d'un departement (sera appelée dérière le boutton "Ajouter"
    def add(self):
        D = departement (self.Id.get(),self.nomDep.get(),self.nomResp.get(),self.anciennete.get(),self.jourConj.get())
        D.ajouterDepartement()
    def view(self):
        #self.root.title("Departement Management(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('700x300')
        self.root.title("Gestion des employers)")
        show_frame = Frame(self.root)
        show_frame.place(width = 800,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage Departement")
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
        tree.heading("2",text = "NomDep",anchor='w')
        tree.heading("3",text = "NomResp",anchor='w')
        tree.heading("4",text="Anciennete",anchor='w')
        tree.heading("5",text="JourConj",anchor='w')
        D=departement()
        rows=D.afficherDepartement()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}'))
            j+=1
    #Fonction dse suppression d'un departement sera appelée dans le boutton "Supprimer"  
    def remove(self):
        D = departement()
        D.supprimerDepartement(self.Id.get())
   
    def update(self):
        D = departement(self.nomDep.get(),self.nomResp.get(),self.anciennete.get(),self.jourConj.get())
        D.modifierDepartement(self.Id.get())

#if __name__ == "__main__":
root = Tk()
l = GestionDepartement(root)
root.mainloop()
