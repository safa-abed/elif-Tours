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
mycursor.execute("CREATE TABLE IF NOT EXISTS departement(Id VARCHAR(255) PRIMARY KEY, nomDep VARCHAR(255), nomResp VARCHAR(255) , anciennete VARCHAR(255) , jourConj INT)")
mycursor.execute("SHOW TABLES")
#Classe Employer
class departement:
    db=connect_BD()
    mycursor=db.cursor()
    def __init__(self,Id="",nomD="",nomR="",anc="",jrC=0):
        self.identifien =Id
        self.nomDep=nomD
        self.nomResp=nomR
        self.anciennete=anc
        self.jourConj=jrC

    #fonction d'ajout dans la table departement
    def ajouterDepartement (self):
        sql = "INSERT INTO departement (Id, nomDep, nomResp, anciennete, jourConj) VALUES (%s, %s, %s, %s, %s)"
        val = (self.identifien, self.nomDep, self.nomResp, self.anciennete, self.jourConj)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "record inserted.")
    def afficherDepartement(self):
        self.mycursor.execute('SELECT * FROM departement')
        result = self.mycursor.fetchall()
        return result
    #fonction supprimer departement
    def supprimerDepartement(self,Id):
        sql = "DELETE FROM departement WHERE Id = %s"
        val = (Id,)
        self.mycursor.execute(sql, val)
        self.db.commit()
    def modifierDepartement(self,other):
        sql="UPDATE departement SET nomDep=%s, nomResp=%s, anciennete=%s, jourConj=%s WHERE Id=%s"
        val=(self.nomDep,self.nomResp,self.anciennete,self.jourConj,other)
        self.mycursor.execute(sql, val)
        self.db.commit()
        
        
#Programme principal:
"""D3=departement("00991322","Rh","grami moez"," 2ans et 6 mois",15)
D3.ajouterDepartement()
D2=departement("00993161","commercial","hlel faten","4 ans",5)
D2.ajouterDepartement()
D3.afficherDepartement()
D2.afficherDepartement()"""

"""Dep=departement()
print("avant suppression.....")
Dep.afficherDepartement()
Dep.supprimerDepartement("00993153")
print("après suppression.....")
Dep.afficherDepartement()"""

"""ModD=departement()
ModD.afficherDepartement()
ModD.modifierDepartement("00993152")
ModD.afficherDepartement()"""
