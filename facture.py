import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="ahmedhm",password="116hm91")
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("create database if not exists ahmedbd")

def connect_BD():
    mydb=mysql.connector.connect(host="localhost",user="ahmedhm",password="116hm91",database="ahmedbd")
    return(mydb)
db=connect_BD()
mycursor=db.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS facture(Id INT PRIMARY KEY, destination VARCHAR(255) , quantite INT , prixUni INT , prixTot INT)")
mycursor.execute("SHOW TABLES")
#Classe Employer
class facture:
    db=connect_BD()
    mycursor=db.cursor()
    def __init__(self,Id="",destination="",quantite=0,prixUni=0,prixTot=0):
        self.Id =Id
        self.destination=destination
        self.quantite=quantite
        self.prixUni=prixUni
        self.prixTot=prixTot

    #fonction d'ajout dans la table employer
    def ajouterFacture (self):
        sql = "INSERT INTO facture (Id, destination, quantite, prixUni, prixTot) VALUES (%s, %s, %s, %s, %s)"
        val = (self.Id, self.destination, self.quantite, self.prixUni, self.prixTot)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "record inserted.")
    def afficherFacture(self):
        self.mycursor.execute('SELECT * FROM facture')
        result = self.mycursor.fetchall()
        return result
            
    #fonction supprimer etudiant
    def supprimerFacture(self,Id):
        sql = "DELETE FROM facture WHERE Id = %s"
        val = (Id,)
        self.mycursor.execute(sql, val)
        self.db.commit()
    def modifierFacture(self,other):
        sql="UPDATE facture SET destination=%s, quantite=%s, prixUni=%s, prixTot=%s WHERE Id=%s" 
        val=(self.destination,self.quantite,self.prixUni,self.prixTot,other)
        self.mycursor.execute(sql, val)
        self.db.commit()
        
        
#Programme principal:
"""F3=facture("00991322","japon",2,1000,2000)
F3.ajouterFacture()
F2=facture("00993161","italie",1,300,300)
F2.ajouterFacture()
F3.afficherFacture()
F2.afficherFacture()"""

"""fact=facture()
print("avant suppression.....")
fact.afficherFacture()
fact.supprimerFacture("00993153")
print("après suppression.....")
fact.afficherFacture()"""

"""md=facture()
md.afficherFacture()
md.modifierFacture("00991322")
md.afficherFacture()"""



