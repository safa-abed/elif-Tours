from tkinter import *
from facture import facture
import tkinter.ttk as ttk

class GestionFacture():
    def __init__(self,root):
        self.root = root
        self.root.geometry('600x600')
        self.root.title("Gestion Facture")
        self.Id=StringVar()
        self.destination=StringVar()
        self.quantite=StringVar()
        self.prixUni=StringVar()
        self.prixTot=StringVar()
    #Formulaire ajout Etudiant dans __init():
        #==============Num employer TEXTFIELD AND LABEL
        Id_lbl = Label(self.root,text = "Id client",anchor='w')
        Id_lbl.grid(row = 1,column = 0,padx = 40,pady = 40)
        Id_field = Entry(self.root,textvariable = self.Id)
        Id_field.grid(row = 1,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #==============Nom employer TEXTFIELD AND LABEL
        destination_lbl = Label(self.root,text = "Destination",anchor='w')
        destination_lbl.grid(row = 2,column = 0,padx = 40,pady = 40)
        destination_field = Entry(self.root,textvariable = self.destination)
        destination_field.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================Prenom employer LABEL AND TEXTFIELD
        quantite_lbl = Label(self.root,text="Quantité",anchor='w')
        quantite_lbl.grid(row = 3,column = 0,pady = 40)
        quantite_field = Entry(self.root,textvariable = self.quantite)
        quantite_field.grid(row = 3,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================categorie employer LABEL AND TEXTFIELD
        prixUni_lbl = Label(self.root,text="Prix Unitaire",anchor='w')
        prixUni_lbl.grid(row = 4,column = 0,pady = 40)
        prixUni_field = Entry(self.root,textvariable = self.prixUni)
        prixUni_field.grid(row = 4,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================salaire employer LABEL AND TEXTFIELD
        prixTot_lbl = Label(self.root,text="Prix Total",anchor='w')
        prixTot_lbl.grid(row = 5,column = 0,pady = 40)
        prixTot_field = Entry(self.root,textvariable = self.prixTot)
        prixTot_field.grid(row = 5,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=====================Boutton ajout
        ajou_employer_btn = Button(self.root,text = "Ajouter",command = self.add,anchor='c')
        ajou_employer_btn.grid(row = 6,column = 0,ipady = 4,ipadx = 13,pady = 40)
          
        #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        affich_facture_btn = Button(self.root,text = "Afficher",command = self.view,anchor='c')
        affich_facture_btn.grid(row = 6,column = 1,ipady = 4,ipadx = 13,pady = 40)
        
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_facture_btn = Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        supp_facture_btn.grid(row = 6,column = 2,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton modifier à ajouter après boutton "Afficher" dans __init()__
        modif_facture_btn = Button(self.root,text = "Modifier",command = self.update,anchor='c')
        modif_facture_btn.grid(row = 6,column = 3,ipady = 4,ipadx = 13,pady = 40)

        
        #Fonction d'ajout d'un étudiant (sera appelée dérière le boutton "Ajouter"
    def add(self):
        F = facture (self.Id.get(),self.destination.get(),self.quantite.get(),self.prixUni.get(),self.prixTot.get())
        F.ajouterFacture()
    def view(self):
        #self.root.title("Student Management(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('700x300')
        self.root.title("Gestion des factures)")
        show_frame = Frame(self.root)
        show_frame.place(width = 800,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage des factures")
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
        tree.heading("2",text = "Destination",anchor='w')
        tree.heading("3",text = "Quantite",anchor='w')
        tree.heading("4",text="PrixUni",anchor='w')
        tree.heading("5",text="PrixTot",anchor='w')
        F=facture()
        rows=F.afficherFacture()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}'))
            j+=1
    #Fonction dse suppression  sera appelée dans le boutton "Supprimer"  
    def remove(self):
        F = facture()
        F.supprimerFacture(self.Id.get())
    #Fonction dse suppression  sera appelée dans le boutton "Supprimer"  
    def update(self):
        F = facture(self.Id.get(),self.destination.get(),self.quantite.get(),self.prixUni.get(),self.prixTot.get())
        F.modifierFacture(self.Id.get())

#if __name__ == "__main__":
root = Tk()
l = GestionFacture(root)
root.mainloop()
