from tkinter import *
from Reservation import Reservation
import tkinter.ttk as ttk

class GestionReservation():
    def __init__(self,root):
        self.root = root
        self.root.geometry('700x700')
        self.root.minsize(600,600)
        self.root.title("Gestion Reservation")
        self.root.configure(bg="#b2dfdb")
        
        self.num_reservation=IntVar()
        self.date_reservation=StringVar()
        self.status=StringVar()
        
    #Formulaire ajout Reservation dans __init():
        #==============Num Reservation TEXTFIELD AND LABEL
        num_reservation_lbl = Label(self.root,text = "Num reservation",anchor='w',relief=RAISED)
        num_reservation_lbl.grid(row = 1,column = 0,padx = 40,pady = 40)
        num_reservation_field = Entry(self.root,textvariable = self.num_reservation)
        num_reservation_field.grid(row = 1,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #==============date reservation TEXTFIELD AND LABEL
        date_reservation_lbl = Label(self.root,text = "date reservation",anchor='w',relief=RAISED)
        date_reservation_lbl.grid(row = 2,column = 0,padx = 40,pady = 40)
        date_reservation_field = Entry(self.root,textvariable = self.date_reservation)
        date_reservation_field.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================Status reservation LABEL AND TEXTFIELD
        status_lbl = Label(self.root,text="Status",anchor='w',relief=RAISED)
        status_lbl.grid(row = 3,column = 0,pady = 40)
        status_field = Entry(self.root,textvariable = self.status)
        status_field.grid(row = 3,column = 1,ipady = 7,ipadx = 20,padx = 20)
       
        #=====================Boutton ajout
        ajou_reservation_btn = Button(self.root,text = "Ajouter",command = self.add,anchor='c',activebackground="yellow",fg="orange")
        ajou_reservation_btn.grid(row = 5,column = 0,ipady = 4,ipadx = 13,pady = 40)
          
        #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        affich_reservation_btn = Button(self.root,text = "Afficher",command = self.view,anchor='c',activebackground="yellow",fg="orange")
        affich_reservation_btn.grid(row = 5,column = 1,ipady = 4,ipadx = 13,pady = 40)
        
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_reservation_btn = Button(self.root,text = "Supprimer",command = self.remove,anchor='c',activebackground="yellow",fg="orange")
        supp_reservation_btn.grid(row = 5,column = 2,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton Modifier à ajouter après boutton "Supprimer" dans __init()__
        modif_reservation_btn = Button(self.root,text = "Modifier",command = self.update,anchor='c',activebackground="yellow",fg="orange")
        modif_reservation_btn.grid(row = 6,column =1,ipady = 4,ipadx = 13,pady = 40)
        
        #Fonction d'ajout d'une réservation (sera appelée dérière le boutton "Ajouter"
    def add(self):
        R = Reservation(int(self.num_reservation.get()),self.date_reservation.get(),self.status.get())
        R.ajouterReservation()
    def view(self):
        #self.root.title("Student Management(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('700x300')
        self.root.title("Gestion des reservations)")
        show_frame = Frame(self.root)
        show_frame.place(width = 800,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage des reservations")
        labl_show.pack()
        #========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 600,height = 200,x = 10,y = 60)
        tree = ttk.Treeview(main_frame,height = 200)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "num_reservation",anchor='c')
        tree.heading("2",text = "date_reservation",anchor='w')
        tree.heading("3",text = "Status",anchor='w')
        R=Reservation()
        rows=R.afficherReservations()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}'))
            j+=1
    #Fonction dse suppression d'un étudiant sera appelée dans le boutton "Supprimer"  
    def remove(self):
        R = Reservation()
        R.supprimerReservation(self.num_reservation.get())
    def update(self):
        R = Reservation( self.num_reservation.get(),self.date_reservation.get(), self.status.get())
        R.modifierReservation(self.num_reservation.get())
#if __name__ == "__main__":
root = Tk()
l = GestionReservation(root)
root.mainloop()
