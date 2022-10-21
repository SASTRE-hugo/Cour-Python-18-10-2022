import random
import math

# FICHIER DE SASTRE HUGO
#Voila un commentaire python
"""
Commentaire
multiligne
"""
#x = 5 #automatiquement le type int
#y = "salut" #automatiquement le type string
#print(y)
#if x > 2:
#   print('Hello')


#Casting :
#x= str(5)
#y = int(5)
#z = float(5)

#print(x)
#print(y)
#print(z)
#print(type(x))
#print(type(y))
#print(type(z))

#a = 'Vincent'
#b = "Hugo"
#print(a)
#print(b)

#d, e, f = "Fruit", "legumes", "ballon"
#print(d,e,f)

#fruits = {"Pomme", "Bannane", "Coco"}
#x, y, z=fruits
#print(x+y+z)

#x= 10
#y = 20
#print(x+y)

#p = "Python"
#def fonction_test():
#    global p
#    p = "Pycharm"
#    print(p,"est génial")

#fonction_test()
#print(p)

# x=1
# y=3.5
# z=1j
#
# a=float(x)
# b=int(y)
# c=complex(x)
#
# print(a)
# print(b)
# print(c)
# print("--------------------------------")
# print(type(a))
# print(type(b))
# print(type(c))

# Génération d'un nombre aléatoire entre 1 et 10
#print(random.randrange(1,10))

#for x in "Vincent" :
#    print(x)

a = "Hello ca va ?"
#print(len(a))

# Structure de conditions
# if "va" in a :
#     print("Trouvé")
# if "vy" not in a :
#     print("Non présent")

# x = "Salut les amis !! "
# print(x[-2:4])

def exo_1():
    prenom = "Pierre"
    age = 20
    majeur = True
    compte_en_banque = 20135.384
    amis =['Marc','Julien','Adrien']
    parents=('Marc','Caroline')
    print(prenom,' a ',age,' ans et il est riche : ',compte_en_banque,' mais son amis :',amis [1], 'est pauvres. Mais',parents[1], 'et' ,parents[0], 'sont la pour payer')

#exo_1()

def exo_2():
    nombre = 15 # ou "15" lors de la déclaration mais pas super car la variables devient donc un string et non plus un int
    print('Le nombre est ' + str(nombre))
#exo_2()

def exo_3():
    a = 2
    b = 6
    c = 3
    #print(a,"+",b,"+",c)
    print(a, b, c, sep=" + ")
#exo_3()

def exo_4():
    list1 = range(3) # changement du nom de la variable pour pas que cela écrase la méthone list()
    list2 = range(5)
    print((list(list2),'||',list((list1)))) # list est un mot réservé ...
#exo_4()

def exo_5():
    prenom = 'hugo'
    if type(prenom)==str:
        print('La variable est une chaine de caractére')
    elif type(prenom) != str:
        print ('La variable est pas une chaine')
#exo_5()
#prenom = 0
#if isinstance(prenom,int):
#    print('La variable est un entier')


# a = 'hello'
# print(a.upper())
#
# b="voila"
# print(b.lower())
#
# c="je test les espaces"
# print(c.strip())
#
# d="je remplace les éléments"
# print(d.replace("e","P"))
#
# e="Voici un exemple de phrase"
# x=(e.find("exemple"))
# print(x)
#
# print(5>8)

#print(bool("Hello"))
#
# a=2
# b=14
# c= b%a
# b = a ** 10
# print(b)
# print(c)

# x = 5
# print(not(x>3 and x<10))
#
# x = ["fruits","legumes"]
# y = ["fruits","legumes"]
# z=x
# print(y is z)
# print(y==z)

def exo_6():
    phrase = "Bonjour"
    print(phrase.replace("Bonjour","Bonsoir"))
#exo_6()

def exo_7():
    prenom ='Hugo'
    if type(prenom)==str:
        print('La variable est une chaine ')
    prenom = 0
    if isinstance(prenom,int):
        print('La variable est un entier ')
#exo_7()
def exo_8():
    phrase = "Bonjour tout le monde. Je répéte Bonjour"
    newPhrase = phrase.replace("Bonjour", "Bonsoir", 1)
    print(newPhrase)
#exo_8()

def exo_9():
    chaine = "Pierre, Julien, Anne, Marie, Lucien"
    chaine_split = chaine.split(', ')
    chaine_split.sort()
    print(chaine_split)
#exo_9()

# maListe1 = ["Pierre","Hugo"]
# maListe2 = ["Anne","Marie"]
# maListe1.extend(maListe2)
# print(maListe1)
# maListe1.pop(1)
# print(maListe1)
#maListe1.pop() #supprimer le dernier élément de la liste

def exo_10():
    Ma_spehre_rayon = float(input('Quel est le rayon de votre sphere en cm : '))
    Volume_sphere = (4*(math.pi)/3)*Ma_spehre_rayon**3
    print('Le volume de votre sphere de ', Ma_spehre_rayon, 'centimétre est de : ',Volume_sphere,' centimétre cube')
#exo_10()

def exo_11():
    try:
        P_Nombre= int(input('Veuillez entrez un nombre pour le comparer : '))
    except:
        print('Veuillez entrez un nombre !')
        exo_11()
    if P_Nombre > 10:
            print('Votre nombre est supérieur a 10 ! ')
    elif P_Nombre ==10 :
            print('Votre nombre est égal a 10 !')
    elif P_Nombre <10 :
            print('Votre nombre est inférieur a 10 !')
#exo_11()

def exo_11_V2():
    P_Nombre_random = random.randint(0,11)
    try:
        P_Nombre= int(input('Veuillez entrez un nombre pour le comparer : '))
    except:
        print('Veuillez entrez un nombre !')
        exo_11()
    if P_Nombre > P_Nombre_random:
            print('Votre nombre est supérieur a 10 ! ')
    elif P_Nombre == P_Nombre_random :
            print('Votre nombre est égal a 10 !')
    elif P_Nombre < P_Nombre_random :
            print('Votre nombre est inférieur a 10 !')
#exo_11_V2()

def exo_12():
    Malist = []
    Num_1 = 5
    Num_2 = 15
    while (Num_1 <= Num_2):
        Malist.append(Num_1)
        Num_1 += 1
    print(Malist)
#exo_12()

#----------------------------------------------------------------------------------
# COUR DU 21/10/2022

# Ma_Liste = ["fraise","orange","banane"]
# Ma_Liste.sort()
# print(Ma_Liste)

# Ma_Liste_num = [1, 30, 12, 14,18 ,47 ,4 ,6]
# Ma_Liste_num.sort()
# print(Ma_Liste_num)

# Ma_Liste_num = [1, 30, 12, 14,18 ,47 ,4 ,6]
# Ma_Liste_num.sort(reverse=True)
# print(Ma_Liste_num)

# def myfunc(x):
#     return abs(x-50)
# la_liste = [100, 50, 65, 82, 23]
# la_liste.sort(key=myfunc)
# print(la_liste)
# attention a la case elle compte aussi pour le sort

#faire une copie d'une liste
# la_liste2 = [100, 50, 65, 82, 23]
# la_liste2c = la_liste2.copy()
# print(la_liste2c)

# faire une jointure de liste
# liste1 = ["x", "y", "z"]
# liste2 = [1,2,3]
# liste3 = liste1 + liste2
# print(liste3)

# autre methode
# liste1 = ["x", "y", "z"]
# liste2 = [1,2,3]

# for x in liste2:
#     liste1.append(x)
# print(liste1)

#autre methode bis
# liste1.extend(liste2)
# print(liste1)

#clear() va vider la liste
# liste1 = ["x", "y", "z"]
# liste1.clear()
# print(liste1)

# LES TUPLES
# montuple = ('Pomme','Kiwi','Citron')
# print(montuple)
# print(type(montuple))
# print(len(montuple))

# crée un tuple avec un objet
# mon_tuple = ("poire",) # si on enleve la virgule on recoit un string et non plus un string
# print(type(mon_tuple))

# On peut mélanger les types et avoir des tuples constitués de booléen, chaine, entier ....
# Le tuple est une classe comme les autres types en python
#faire appel au constructeur du tuple
# montuple =  tuple(("Pomme", "Banane", "Fraise"))
# print(montuple)
# print(montuple[1])
# print(montuple[-1]) # retourne le dernier élément de mon tuple

# My_tuple = ("Pomme","Kiwi","Citron","Banane","Fraise","Melon","Cerise")
# print(My_tuple[2:5]) #On accede aux élément de 2 a 4 !!

# My_tuple = ("Pomme","Kiwi","Citron","Banane","Fraise","Melon","Cerise")
# print(My_tuple[2:]) #On accede aux élément de Citron a la fin de notre tuple

# My_tuple = ("Pomme","Kiwi","Citron","Banane","Fraise","Melon","Cerise")
# if "Citron" in My_tuple: # RECHERCHE DE CITRON DANS MA LISTE
#     print("Présent !!! ")

# montuple = ("Pomme","Kiwi","Citron")
# a = list(montuple)
# a.append("Ballon") # ajout de ballon a la fin de mon tuple
# a[1]="fraise"
# montuple=tuple(a)
# print(montuple) # modification de mon tuple

#Ajouter un tuple à un tuple
# montuple = ("Pomme", "Kiwi", "Citron")
# a =("Fraise",)
# montuple+=a
# print(montuple)
#
# #Supprimer un élément
# montuple = ("Pomme", "Kiwi", "Citron")
# a =list(montuple)
# a.remove("Pomme")
# montuple = tuple(a)
# print(montuple)

# montuple = ("Pomme", "Kiwi", "Citron")
# del montuple
# print(montuple) # erreur car mon tuple n'existe plus

#montuple = ("Pomme", "Kiwi", "Citron")
# (a,b,*c) = montuple # récupérer des variables d'un tuple mais pour le c on récupere une list
# print(a)
# print(b)
# print(c) # recupere une liste

# Parcourir un tuple via une boucle
# for x in montuple:
#     print(x)


# Parcrourir un tuple utilisant le numéro d'index
# for x in range(len(montuple)):
#     print(montuple[x])

# parcourir avec un while
# x=0
# while x < len(montuple):
#     print(montuple[x])
#     x = x+1

# montuple1 = ("Pomme", "Kiwi","Fraise")
# montuple2 = (4, 12, 6)
# montuple3 = montuple1 + montuple2
# print(montuple3)
# montuple4 = montuple1 * 2
# print(montuple4)

def Affiche_Nombre_Pairs():
    Ma_liste = []
    x=1
    while x < 101 :
        if x % 2 ==0:
            Ma_liste.append(x)
            x = x+1
        else :
            x=x+1
    print(Ma_liste)
#Affiche_Nombre_Pairs()

def Lancer_Des_Aleatoires():
    Lancer_Des = 0
    Liste_Des = []
    while Lancer_Des <=6 :
        Mon_Des = random.randrange(1,7)
        Liste_Des.append(Mon_Des)
        Lancer_Des = Lancer_Des +1
    print(Liste_Des)
#Lancer_Des_Aleatoires()

def Lancer_Des_Aleatoires_V2():
    Lancer_Des = int(input('Veuillez entrer votre nombre de lancé :'))
    Liste_Des = []
    x=0
    Somme_Des =0
    while x <Lancer_Des :
        Mon_Des = random.randrange(1,7)
        Liste_Des.append(Mon_Des)
        Somme_Des = Somme_Des + Liste_Des[x]
        x = x+1
    Moy_Des = Somme_Des / Lancer_Des
    print('Voici la liste de vos lancés : ', Liste_Des)
    print('Votre moyenne de lancé est de : ', Moy_Des)
#Lancer_Des_Aleatoires_V2()

def Compteur_Lettre():
    Mon_String = str(input("Entrez une phrase "))
    Lettre = str(input('Veuillez entrez une lettre afin de la compter : '))
    Compteur = 0
    for x in range(len(Mon_String)):
        if Lettre in Mon_String[x].lower():
            Compteur = Compteur +1
    print('Il y a :', Compteur, Lettre,'dans votre phrase')
#Compteur_Lettre()

def Compteur_lettre_V2():
    Mon_Alpahbet =[['a'],['b'],'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Mon_String = str(input("Entrez une phrase "))
    Compteur = 0
    for x in range(len(Mon_String)):
        if Mon_Alpahbet[x] in Mon_String:
            Compteur = Compteur +1
    print('Il y a :', Compteur,'dans votre phrase')
Compteur_lettre_V2()




