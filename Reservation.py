import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="safa2",password="safa123")
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("create database if not exists safabd")

def connection():
    mydb=mysql.connector.connect(host="localhost",user="safa2",password="safa123",database="safabd")
    return(mydb)
db=connection()
mycursor=db.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Reservation(num_reservation INT PRIMARY KEY, date_reservation VARCHAR(255) , status VARCHAR(255))")
mycursor.execute("SHOW TABLES")
class Reservation:
    db=connection()
    mycursor=db.cursor()
    def __init__(self,num_reservation=0,date_reservation="jj/mm/aaaa",status=""):
        self.num_reservation=num_reservation
        self.date_reservation=date_reservation
        self.status=status

    def ajouterReservation(self):
       sql="INSERT INTO Reservation (num_reservation,date_reservation,status) VALUES (%s, %s, %s)"
       val = (self.num_reservation, self.date_reservation, self.status)
       self.mycursor.execute(sql, val)
       self.db.commit()
       print(self.mycursor.rowcount, "record inserted.")
    def afficherReservations(self):
         self.mycursor.execute("SELECT * FROM Reservation")
         res=self.mycursor.fetchall()
         return res
    def supprimerReservation(self,num_reservation):
        sql = "DELETE FROM Reservation WHERE num_reservation = %s"
        val = (num_reservation,)
        self.mycursor.execute(sql, val)
        self.db.commit()
    def modifierReservation(self,other):
        sql="UPDATE Reservation SET date_reservation=%s,status= %s WHERE num_reservation=%s"
        val=(self.date_reservation, self.status, other)
        self.mycursor.execute(sql, val)
        self.db.commit()
        
         
"""tmp=Reservation()
print("avant suppression.....")
tmp.afficherReservations()
tmp.supprimerReservation(2)
print("après suppression.....")
tmp.afficherReservations()"""
"""m=Reservation()
m.afficherReservations()
m.modifierReservation(4)
m.afficherReservations()"""
"""R7=Reservation(7,"16/03/2021","rejete")
R7.ajouterReservation()
R7.afficherReservations()"""
"""R8=Reservation(8,"17/03/2021","rejete")
R8.ajouterReservation()
R8.afficherReservations()"""
"""R7=Reservation(7,"17/03/2021","rejete")
R7.modifierReservation(7)
R7.afficherReservations()"""







