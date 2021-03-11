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
mycursor.execute("CREATE TABLE IF NOT EXISTS client(code VARCHAR(255) PRIMARY KEY, nom VARCHAR(255), prenom VARCHAR(255) , adresse VARCHAR(255))")
mycursor.execute("SHOW TABLES")

class carteFidel:
    db=connect_BD()
    mycursor=db.cursor()
    def __init__(self,code="",nom="",prenom="",adresse=""):
        self.code =code
        self.nom=nom
        self.prenom=prenom
        self.adresse=adresse
        

    
    def ajouterCarteFidel (self):
        sql = "INSERT INTO carteFidel (code, nom, prenom, adresse) VALUES (%s, %s, %s, %s)"
        val = (self.code, self.nom, self.prenom, self.adresse)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "record inserted.")
    def afficherCarteFidel(self):
        self.mycursor.execute('SELECT * FROM carteFidel')
        result = self.mycursor.fetchall()
        return result
    
    def supprimerCarteFidel(self,Id):
        sql = "DELETE FROM carteFidel WHERE code = %s"
        val = (Id,)
        self.mycursor.execute(sql, val)
        self.db.commit()
    def modifierCarteFidel(self,other):
        sql="UPDATE carteFidel SET  nom=%s, prenom=%s, adresse=%s WHERE code=%s"
        val=(self.nom,self.prenom,self.adresse,other)
        self.mycursor.execute(sql, val)
        self.db.commit()
        
        
#Programme principal:
"""C3=carteFidel("102","nesrin","ben ammar","rue ibn khaldoun")
C3.ajouterCarteFidel()
C2=carteFidel("105","asma"," ben ali"," rue yasminet")
C2.ajouterCarteFidel()
C3.afficherCarteFidel()
C2.afficherCarteFidel()"""

"""Crt=carteFidel()
print("avant suppression.....")
Crt.afficherCarteFidel()
Crt.supprimerCarteFidel("00993161")
print("après suppression.....")
Crt.afficherCarteFidel()"""

"""Mod= carteFidel()
Mod.afficherCarteFidel()
Mod.modifierCarteFidel()
Mod.afficherCarteFidel()"""
