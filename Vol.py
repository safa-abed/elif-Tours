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
mycursor.execute("CREATE TABLE IF NOT EXISTS Vol(Id_vol INT PRIMARY KEY,compagnie_transport VARCHAR(255),Type_billet VARCHAR(255),date_depart VARCHAR(255) ,ville_depart VARCHAR(255),date_arrivee VARCHAR(255) ,ville_arrivee VARCHAR(255))")
mycursor.execute("SHOW TABLES")
class Vol:
    db=connection()
    mycursor=db.cursor()
    def __init__(self,Id_vol=0,compagnie_transport="",Type_billet="",date_depart="jj/mm/aaaa",ville_depart="",date_arrivee="jj/mm/aaaa",ville_arrivee=""):
        self.Id_vol=Id_vol
        self.compagnie_transport=compagnie_transport
        self.Type_billet=Type_billet
        self.date_depart=date_depart
        self.ville_depart=ville_depart
        self.date_arrivee=date_arrivee
        self.ville_arrivee=ville_arrivee
        
    def ajouterVol(self):
       sql="INSERT INTO Vol (Id_vol,compagnie_transport,Type_billet,date_depart,ville_depart,date_arrivee,ville_arrivee) VALUES (%s, %s, %s,%s,%s,%s,%s)"
       val = (self.Id_vol, self.compagnie_transport, self.Type_billet,self.date_depart,self.ville_depart,self.date_arrivee,self.ville_arrivee)
       self.mycursor.execute(sql, val)
       self.db.commit()
       print(self.mycursor.rowcount, "record inserted.")
    def afficherVols(self):
        self.mycursor.execute("SELECT * FROM Vol")
        res=self.mycursor.fetchall()
        return res
    def supprimerVol(self,Id_vol):
        sql = "DELETE FROM Vol WHERE Id_vol = %s"
        val = (Id_vol,)
        self.mycursor.execute(sql, val)
        self.db.commit()
    def modifierVol(self,other):
        sql="UPDATE Vol SET compagnie_transport=%s,Type_billet=%s,date_depart=%s,ville_depart=%s,date_arrivee=%s,ville_arrivee=%s WHERE Id_vol=%s"
        val=( self.compagnie_transport,self.Type_billet,self.date_depart,self.ville_depart,self.date_arrivee,self.ville_arrivee,other)
        self.mycursor.execute(sql, val)
        self.db.commit()

       
"""V1=Vol(11,"TunisAir","Aller Simple","01/06/2021","Tunis","01/06/2021","France")
V1.ajouterVol()"""
"""V2=Vol(12,"Qatar Air","Retour Simple","22/06/2021","Qatar","22/06/2021","Tunis")
V2.ajouterVol()"""
"""V3=Vol(13,"TunisAir","Aller Simple","30/06/2021","Tunis","30/06/2021","Canada")
V3.ajouterVol()"""
"""V4=Vol(14,"TunisAir","Retour Simple","05/07/2021","Tunis","05/06/2021","Allemagne")
V4.ajouterVol()"""
"""V5=Vol(15,"TunisAir","Aller Simple","02/06/2021","Tunis","02/06/2021","France")
V5.ajouterVol()"""
"""V6=Vol(16,"TunisAir","Aller Simple","01/06/2021","Tunis","01/06/2021","France")
V6.ajouterVol()"""
"""tmp=Vol()
print("avant suppression.....")
tmp.afficherVols()
tmp.supprimerVol(16)
print("après suppression.....")
tmp.afficherVols()"""
"""V11=Vol(19,"TunisAir","Aller Simple","01/06/2021","Tunis","01/06/2021","France")
V11.ajouterVol()"""
"""V12=Vol(12,"TunisAir","Aller + Retour","02/06/2021","Tunis","02/06/2021","France")
V12.ajouterVol()"""
"""V13=Vol(12,"Air","Aller + Retour","02/06/2021","Tunis","02/06/2021","France")
V13.modifierVol(12)
V13.afficherVols()"""
