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



