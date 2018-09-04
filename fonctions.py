def question(question, reponse, chances):
    q = input(question)
    while q != reponse:
        if chances == 0:
            print("Oh non ! Tu as perdu le jeu...")
            break
        else:
            chances -= 1
            print("Dommage ! Il te reste {} chances".format(chances))
            q = input(question)

    else:
        print("Bonne réponse !")
        chances_restantes = chances
        return chances_restantes


print("Voici notre quiz, tu as trois chances !")
nb_de_chances = question("Quelle est la couleur du cheval blanc d'Henry IV ?", "blanc", 3)

if nb_de_chances > 0:
    nb_de_chances = question("Quand a été fondé Apple", "1976", nb_de_chances)

if nb_de_chances > 0:
    print("Bravo tu as gagné le jeu !")
