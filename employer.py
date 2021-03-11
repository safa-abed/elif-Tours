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
mycursor.execute("CREATE TABLE IF NOT EXISTS employer(Id INT PRIMARY KEY, nom VARCHAR(255) , prenom VARCHAR(255) , categorie VARCHAR(255) , salaire INT)")
mycursor.execute("SHOW TABLES")
#Classe Employer
class employer:
    db=connect_BD()
    mycursor=db.cursor()
    def __init__(self,Id="",nm="",pr="",cat="",sal=0):
        self.identifien =Id
        self.nom=nm
        self.prenom=pr
        self.categorie=cat
        self.salaire=sal

    #fonction d'ajout dans la table employer
    def ajouterEmployer (self):
        sql = "INSERT INTO employer (Id, nom, prenom, categorie, salaire) VALUES (%s, %s, %s, %s, %s)"
        val = (self.identifien, self.nom, self.prenom, self.categorie, self.salaire)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "record inserted.")
    def afficherEmployer(self):
        self.mycursor.execute('SELECT * FROM employer')
        result = self.mycursor.fetchall()
        return result
            
    #fonction supprimer etudiant
    def supprimerEmployer(self,Id):
        sql = "DELETE FROM employer WHERE Id = %s"
        val = (Id,)
        self.mycursor.execute(sql, val)
        self.db.commit()
    def modifierEmployer(self,other):
        sql="UPDATE employer SET nom=%s, prenom=%s, categorie=%s, salaire=%s WHERE Id=%s" 
        val=(self.nom,self.prenom,self.categorie,self.salaire,other)
        self.mycursor.execute(sql, val)
        self.db.commit()
        
        
#Programme principal:
"""E3=employer("00991322","karim","grami","cadre",1000)
E3.ajouterEmployer()
E2=employer("00993161","olfa","hlel","agent",650)
E2.ajouterEmployer()
E3.afficherEmployer()
E2.afficherEmployer()"""

"""emp=employer()
print("avant suppression.....")
emp.afficherEmployer()
emp.supprimerEmployer("00993153")
print("après suppression.....")
emp.afficherEmployer()"""

"""md=employer()
md.afficherEmployer()
md.modifierEmployer("00993152")
md.afficherEmployer()"""



