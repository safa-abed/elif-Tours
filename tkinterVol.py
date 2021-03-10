from tkinter import *
from Vol import Vol
import tkinter.ttk as ttk

class GestionVol():
    def __init__(self,root):
        self.root = root
        self.root.geometry('700x700')
        self.root.minsize(600,600)
        self.root.title("Gestion Vol")
        self.root.configure(bg="#b0bec5")
        
        self.Id_vol=IntVar()
        self.compagnie_transport=StringVar()
        self.Type_billet=StringVar()
        self.date_depart=StringVar()
        self.ville_depart=StringVar()
        self.date_arrivee=StringVar()
        self.ville_arrivee=StringVar()
        
    #Formulaire ajout Reservation dans __init():
        #==============Id volTEXTFIELD AND LABEL
        Id_vol_lbl = Label(self.root,text = "Id vol",anchor='w',relief=RAISED)
        Id_vol_lbl.grid(row = 1,column = 0,padx = 40,pady = 40)
        Id_vol_field = Entry(self.root,textvariable = self.Id_vol)
        Id_vol_field.grid(row = 1,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #==============compagnie_transport TEXTFIELD AND LABEL
        compagnie_transport_lbl = Label(self.root,text = "compagnie transport",anchor='w',relief=RAISED)
        compagnie_transport_lbl.grid(row = 2,column = 0,padx = 40,pady = 40)
        compagnie_transport_field = Entry(self.root,textvariable = self.compagnie_transport)
        compagnie_transport_field.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #======================= Type_billet LABEL AND TEXTFIELD
        Type_billet_lbl = Label(self.root,text="Type billet",anchor='w',relief=RAISED)
        Type_billet_lbl.grid(row = 3,column = 0,pady = 40)
        Type_billet_field = Entry(self.root,textvariable = self.Type_billet)
        Type_billet_field.grid(row = 3,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================date_depart  LABEL AND TEXTFIELD
        date_depart_lbl = Label(self.root,text="date_depart",anchor='w',relief=RAISED)
        date_depart_lbl.grid(row = 4,column = 0,pady = 40)
        date_depart_field = Entry(self.root,textvariable = self.date_depart)
        date_depart_field.grid(row = 4,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================ville_depart  LABEL AND TEXTFIELD
        ville_depart_lbl = Label(self.root,text="ville depart",anchor='w',relief=RAISED)
        ville_depart_lbl.grid(row = 5,column = 0,pady = 40)
        ville_depart_field = Entry(self.root,textvariable = self.ville_depart)
        ville_depart_field.grid(row = 5,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================date_arrivee  LABEL AND TEXTFIELD
        date_arrivee_lbl = Label(self.root,text="date arrivee",anchor='w',relief=RAISED)
        date_arrivee_lbl.grid(row = 6,column = 0,pady = 40)
        date_arrivee_field = Entry(self.root,textvariable = self.date_arrivee)
        date_arrivee_field.grid(row = 6,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================ville arrivee  LABEL AND TEXTFIELD
        ville_arrivee_lbl = Label(self.root,text="ville arrivee",anchor='w',relief=RAISED)
        ville_arrivee_lbl.grid(row = 7,column = 0,pady = 40)
        ville_arrivee_field = Entry(self.root,textvariable = self.ville_arrivee)
        ville_arrivee_field.grid(row = 7,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=====================Boutton ajout
        ajou_Vol_btn = Button(self.root,text = "Ajouter",command = self.add,anchor='c',activebackground="yellow",fg="#512da8")
        ajou_Vol_btn.grid(row = 8,column = 0,ipady = 4,ipadx = 13,pady = 40)
          
        #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        affich_Vol_btn = Button(self.root,text = "Afficher",command = self.view,anchor='c',activebackground="yellow",fg="#512da8")
        affich_Vol_btn.grid(row = 8,column = 1,ipady = 4,ipadx = 13,pady = 40)
        
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_Vol_btn = Button(self.root,text = "Supprimer",command = self.remove,anchor='c',activebackground="yellow",fg="#512da8")
        supp_Vol_btn.grid(row = 8,column = 2,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton Modifier à ajouter après boutton "Supprimer" dans __init()__
        modif_Vol_btn = Button(self.root,text = "Modifier",command = self.update,anchor='c',activebackground="yellow",fg="#512da8")
        modif_Vol_btn.grid(row = 8,column =3,ipady = 4,ipadx = 13,pady = 40)
        
        #Fonction d'ajout d'une réservation (sera appelée dérière le boutton "Ajouter"
    def add(self):
        V = Vol(int(self.Id_vol.get()),self.compagnie_transport.get(),self.Type_billet.get(),self.date_depart.get(),self.ville_depart.get(),self.date_arrivee.get(),self.ville_arrivee.get())
        V.ajouterVol()
    def view(self):
        #self.root.title("Student Management(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('700x300')
        self.root.title("Gestion vol")
        show_frame = Frame(self.root)
        show_frame.place(width = 800,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage des vols")
        labl_show.pack()
        #========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 700,height = 300,x = 10,y = 60)
        tree = ttk.Treeview(main_frame,height = 300)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3","4","5","6","7")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.column('7',width=80)
        tree.heading("#0",text = "Id",anchor='c')
        tree.heading("1",text = "Id_vol",anchor='c')
        tree.heading("2",text = "compagnie_transport",anchor='w')
        tree.heading("3",text = "Type_billet",anchor='w')
        tree.heading("4",text = "date_depart",anchor='w')
        tree.heading("5",text = "ville_depart",anchor='w')
        tree.heading("6",text = "date_arrivee",anchor='w')
        tree.heading("7",text = "ville_arrivee",anchor='w')
    
        V=Vol()
        rows=V.afficherVols()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}',f'{i[6]}'))
            j+=1
    #Fonction dse suppression d'un étudiant sera appelée dans le boutton "Supprimer"  
    def remove(self):
        V = Vol()
        V.supprimerVol(self.Id_vol.get())
    def update(self):
        V = Vol(self.Id_vol.get(),self.compagnie_transport.get(),self.Type_billet.get(),self.date_depart.get(),self.ville_depart.get(),self.date_arrivee.get(),self.ville_arrivee.get())
        V.modifierVol(self.Id_vol.get())
        
#if __name__ == "__main__":
root = Tk()
l = GestionVol(root)
root.mainloop()
