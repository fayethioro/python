import random
#Ecrire un algorithme qui demande à l’utilisateur un nombre compris entre 1 et 3 jusqu’à ce #
#que la réponse convienne#
input("****************Exercice 5.1  taper entre svp ********************")
nombre=int (input("donner un nombre : "))
while nombre < 1 or nombre > 3 :
    print(f"le nombre doit etre compris entre {1} et {3} " )
    nombre=int (input("donner un nombre : "))

 
#exercice 5.2#
input("****************Exercice 5.2 taper entre svp ********************")
nombre1=int (input("donner un nombre : "))
while nombre1 < 10 or nombre1 > 20 :
    if nombre1 > 20 :
        print(f"donner un nombre plus petit que {nombre1}  ou un nombre  inferieur ou egal a {20}")
    if nombre1 < 10 :
         print(f"donner un nombre plus grand que {nombre1} et inferieur ou egal a {10} ")
    print(f"le nombre doit etre compris entre {10} et {20} " )
    nombre1 =int (input("donner un nombre : "))
#exercice 5.3#
input("****************Exercice 5.3 taper entre svp ********************")
nombre2 = int (input("donner un nombre : ")) 
arret = nombre2 + 10 
print(f" le {10} nomnbres qui suivent son : ")
while nombre2 < arret :
    nombre2 =nombre2 + 1
    print( f" {nombre2}  ")
#exercice 5.4#
input("****************Exercice 5.3 taper entre svp ********************")
nb1=int(input( "donner un nombre : " ))
for i in range(10) :
    nb1=nb1+1
    print( f" {nb1}  ")

#exercice 5.5#
input("****************Exercice 5.4 taper entre svp ********************")
nb=int(input( "donner un nombre : " ))
for i in range(11):
        print(nb, " * ", i, " = ", nb * i)
#exercice 5.6#
input("****************Exercice 5.6 taper entre svp ********************")
nb2=int(input( "donner un nombre : " ))
somme=0
for i in range ( 1, nb2+1 ):
    somme+=i
print(f" La somme est {somme} ")
#exercice 5.7#
input("****************Exercice 5.7 taper entre svp ********************")
nb3=int(input( "donner un nombre : " ))
fac=1
for i in range ( 2, nb3+1 ):
    fac*=i
print(f" la factorielle de {nb3} est {fac} ")
#exercice 5.8#
input("****************Exercice 5.8 taper entre svp ********************")
max=0
for i in range(1,5):
  nombres=int(input("Saisissez un nombre"))
  if  nombres >  max:
     max= nombres
     compteur=i
print(f"le plus grand nombre est", max)
print("la position est", compteur)
#exercice 5.9#
input("****************Exercice 5.9 taper entre svp ********************")
maxbis=0
compeurbis=0
i=0
print ( f" Taper {0}  si vous voulez arreter la saisie" )
nombrebis= int(input("Donner un nombre :") )
while  nombrebis != 0 :
  nombrebis= int(input("Donner un nombre :") )
  i+=1
  if nombrebis > max :
    maxbis = nombrebis
    compteurbis = i
print("le plus grand nombre est", maxbis)
print("la position est", compteurbis)
#exercice 5.10#
input("****************Exercice 5.10 taper entre svp ********************")
prix = 0
sommedue=0
print ( f" Taper {-1}  si vous voulez arreter la saisie" )
while prix != -1:
    prix=int(input(" Entrez le prix : "))
    sommedue += prix
print (f" Vous  nous devez : {sommedue} euros ")
sommeverse= int (input (" Entrez le montant verse:  "))
reste= sommeverse - sommedue
Nb10E=0
while reste >= 10 :
    Nb10E += 1
    reste -= 10
Nb5E = 0
if reste >= 5 :
    Nb5E = 1
    reste -= 5
print(" le montant rendue est :")
print(f" Billets de 10 euros :{Nb10E} ")
print(f" Billets de 5 euros :{Nb5E} ")
print(f" pieces de 1 euros :{reste} ")