from tkinter import *
from carteFidel import carteFidel
import tkinter.ttk as ttk

class GestionCarteFidel():
    def __init__(self,root):
        self.root = root
        self.root.geometry('600x600')
        self.root.title("Gestion Carte Fidelité")
        self.code=StringVar()
        self.nom=StringVar()
        self.prenom=StringVar()
        self.adresse=StringVar()
        
    #Formulaire ajout Etudiant dans __init():
        #==============Num employer TEXTFIELD AND LABEL
        code_lbl = Label(self.root,text = "code ",anchor='w')
        code_lbl.grid(row = 1,column = 0,padx = 40,pady = 40)
        code_field = Entry(self.root,textvariable = self.code)
        code_field.grid(row = 1,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #==============Nom employer TEXTFIELD AND LABEL
        nom_lbl = Label(self.root,text = "Nom ",anchor='w')
        nom_lbl.grid(row = 2,column = 0,padx = 40,pady = 40)
        nom_field = Entry(self.root,textvariable = self.nom)
        nom_field.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================Prenom employer LABEL AND TEXTFIELD
        prenom_lbl = Label(self.root,text="Prénom ",anchor='w')
        prenom_lbl.grid(row = 3,column = 0,pady = 40)
        prenom_field = Entry(self.root,textvariable = self.prenom)
        prenom_field.grid(row = 3,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================categorie employer LABEL AND TEXTFIELD
        adresse_lbl = Label(self.root,text="adresse",anchor='w')
        adresse_lbl.grid(row = 4,column = 0,pady = 40)
        adresse_field = Entry(self.root,textvariable = self.adresse)
        adresse_field.grid(row = 4,column = 1,ipady = 7,ipadx = 20,padx = 20)
       
        #=====================Boutton ajout
        ajou_carteFidel_btn = Button(self.root,text = "Ajouter",command = self.add,anchor='c')
        ajou_carteFidel_btn.grid(row = 5,column = 0,ipady = 4,ipadx = 13,pady = 40)
          
        #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        affich_carteFidel_btn = Button(self.root,text = "Afficher",command = self.view,anchor='c')
        affich_carteFidel_btn.grid(row = 5,column = 1,ipady = 4,ipadx = 13,pady = 40)
        
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_carteFidel_btn = Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        supp_carteFidel_btn.grid(row = 5,column = 2,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton modifier à ajouter après boutton "Afficher" dans __init()__
        modif_carteFidel_btn = Button(self.root,text = "Modifier",command = self.update,anchor='c')
        modif_carteFidel_btn.grid(row = 5,column = 3,ipady = 4,ipadx = 13,pady = 40)

        
        #Fonction d'ajout (sera appelée dérière le boutton "Ajouter"
    def add(self):
        C = carteFidel (self.code.get(),self.nom.get(),self.prenom.get(),self.adresse.get())
        C.ajouterCarteFidel()
    def view(self):
        
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('700x300')
        self.root.title("Gestion des cartes ")
        show_frame = Frame(self.root)
        show_frame.place(width = 800,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage des cartes")
        labl_show.pack()
        #========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 600,height = 200,x = 8,y = 58)
        tree = ttk.Treeview(main_frame,height = 200)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3","4")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "Id",anchor='c')
        tree.heading("2",text = "Nom",anchor='w')
        tree.heading("3",text = "Prenom",anchor='w')
        tree.heading("4",text="adresse",anchor='w')
        C=carteFidel()
        rows=C.afficherCarteFidel()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}'))
            j+=1
     
    def remove(self):
        C = carteFidel()
        C.supprimerCarteFidel(self.code.get())
    
    def update(self):
        C = carteFidel(self.code.get(),self.nom.get(),self.prenom.get(),self.adresse.get())
        C.modifierCarteFidel(self.code.get())

#if __name__ == "__main__":
root = Tk()
l = GestionCarteFidel(root)
root.mainloop()

