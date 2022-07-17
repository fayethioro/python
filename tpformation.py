#voici une liste de transaction
from os import device_encoding


transaction_list = [250, 12, 45, 32, 23, 25, 250, 12 ]

#Tache 1 :la somme des transaction
somme = sum(transaction_list)
print(f"la somme de la transaction est: {somme}")

#Tache 2:Afficher la transaction5
a = transaction_list[4]
print(f"la transaction 5 est: {a} ") 

#Tache 3: ordonner la liste
liste_ordonnee = sorted(transaction_list)
print(f"la liste ordonne est :\n{liste_ordonnee} ")

#tache 4: Transfomer une liste en tuple
print("Transfomer une liste en tuple")
nbre_tuple = tuple(transaction_list)
print(nbre_tuple)
    
#Tache 5:affiche la tansaction la plus petite
minimum = min(transaction_list)
print(f"la transaction la plus petites est: {minimum}")

#Tache 6 : affiche la derniere transaction
b = transaction_list[-1] 
print(f"la derniere transaction est: {b} ") 

#Tache 7: supprimer les transaction dulique et ordonner
apres = sorted(set(transaction_list))
print(f"la liste apres suppression des doublons est :\n{apres} ")

#Tache 8 : Supprimer la derniere transaction
'''transaction_list.pop(-1)
print(f"la liste apres suppression de la derniere transaction est :\n{transaction_list} ")'''

#Tache 9: Creer une copie de la transaction
liste_copy = transaction_list.copy()
print(f"la copie de la liste est:\n{liste_copy} ")

#Tache 10 : la moyenne des transaction
nombre_element = len(transaction_list)
moyenne = sum(transaction_list)/nombre_element
print(f"la moyenne de la transaction est: {moyenne} ")

#Tache 11 : convertir une liste en dictionnaire
print("Transfomer une liste en dictionnaire")
nbre_dict = dict(transaction_list)
print(nbre_dict)


