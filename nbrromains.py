def change(): #définir la fonction
    base=int(input("Nombre à transcrire ? (maximum 9999)")) #valeur demandée à l'utilisateur

    tab = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],[ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],[  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],[   1, 'I']] #tableau des nombres romains

    nombre = "" #variables qui contiendra le résultat final
    cpt = 0 #compteur

    while base != 0 : #décomposition du nombre entier, et pour chaque tranche retirée le symbole romain est ajouté
        while tab[cpt][0] > base:
            cpt+=1

        nombre += tab[cpt][1]
        base -= tab[cpt][0]

    print(nombre)

change() #on appelle la fonction
