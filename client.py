import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="nessrine",password="Nesrin123")
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("create database if not exists nessrinebd")

def connect_BD():
    mydb=mysql.connector.connect(host="localhost",user="nessrine",password="Nesrin123",database="nessrinebd")
    return(mydb)
db=connect_BD()
mycursor=db.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS client(Id VARCHAR(255) PRIMARY KEY, nom VARCHAR(255), prenom VARCHAR(255) , adresse VARCHAR(255) , numTel INT)")
mycursor.execute("SHOW TABLES")

class client:
    db=connect_BD()
    mycursor=db.cursor()
    def __init__(self,Id="",nom="",prenom="",adresse="",numTel=0):
        self.Id =Id
        self.nom=nom
        self.prenom=prenom
        self.adresse=adresse
        self.numTel=numTel

    
    def ajouterClient (self):
        sql = "INSERT INTO client (Id, nom, prenom, adresse, numTel) VALUES (%s, %s, %s, %s, %s)"
        val = (self.Id, self.nom, self.prenom, self.adresse, self.numTel)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "record inserted.")
    def afficherClient(self):
        self.mycursor.execute('SELECT * FROM client')
        result = self.mycursor.fetchall()
        return result
    
    def supprimerClient(self,Id):
        sql = "DELETE FROM client WHERE Id = %s"
        val = (Id,)
        self.mycursor.execute(sql, val)
        self.db.commit()
    def modifierClient(self,other):
        sql="UPDATE client SET  nom=%s, prenom=%s, adresse=%s, numTel=%s WHERE Id=%s"
        val=(self.nom,self.prenom,self.adresse,self.numTel,other)
        self.mycursor.execute(sql, val)
        self.db.commit()
        
        
#Programme principal:
""""C3=client("001215","ameni","ben ammar","rue ibn khaldoun",22662256)
C3.ajouterClient()
C2=client("00993161","asma"," ben ali"," rue yasminet",21554466)
C2.ajouterClient()
C3.afficherClient()
C2.afficherClient()"""

"""Clt=client()
print("avant suppression.....")
Clt.afficherClient()
Clt.supprimerClient("00993161")
print("après suppression.....")
Clt.afficherClient()"""

"""ModC= client()
ModC.afficherClient()
ModC.modifierClient("00993152")
ModC.afficherClient()"""
