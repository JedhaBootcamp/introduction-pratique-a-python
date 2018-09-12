# Introduction Pratique à Python

Bienvenue dans cette introduction pratique à Python. Dans ce workshop, nous allons apprendre ce qu'est un éditeur de texte, une console et apprendre les concepts fondamentaux liés au langage Python. Tout ceci à travers une application simple mais rigolote : un quiz !


Si préférez regarder la vidéo du workshop, n'hésitez pas à cliquer sur ce lien :

[Vidéo Workshop](https://www.youtube.com/watch?v=UCQYUPgqrB8&t=183s)


## Téléchargeons Python

Pour ceux qui voudraient suivre en même temps que le prof, n'hésitez pas à télécharger Anaconda qui est un logiciel pour les Data Scientists à l'origine mais qui inclue aussi la dernière version de Python.

Voici le lien de téléchargement :

[Télécharger Python](https://www.anaconda.com/download)


## De quoi va-t-on avoir besoin pour coder ?

Impatient de coder ? On a presque finit la préparation. Pour pouvoir coder, vous aurez besoin d'un éditeur de texte et d'une console.

### Un éditeur de texte

Un éditeur de texte est l'endroit où vous allez mettre tout votre *script*. Vous avez différent types d'éditeurs de texte comme Sublime, Pycharm ou Notepad++. Si vous avez déjà un éditeur de prédilection, utilisez celui que vous aimez. Pour notre part, nous allons utiliser Atom.

Voici le lien pour télécharger l'éditeur :

[Télécharger Atom](https://atom.io/)


### Une console

Bonne nouvelle ! Votre console, vous l'avez déjà sur votre ordinateur donc vous n'avez rien d'autre à télécharger. Cependant, la console est souvent cachée dans votre ordinateur. Voyons comment y accéder en fonction des différents appareils :

#### Sur Mac

Allez dans Applications > Utilitaire > Terminal

#### Sur Windows

Ouvrir l'explorateur Windows ou le raccourci Poste de Travail.

Aller dans le répertoire `c:\windows\system32`

Cliquer sur le fichier cmd.exe avec le bouton droit et choisir “Exécuter en tant qu'administrateur”

Dans la fenêtre qui s'ouvre, saisir un nom de compte et le mot de passe d'un administrateur.
Cliquer sur OK

#### A quoi cela sert ?

La console est ce qui va vous permettre d'executer votre code. Alors que l'éditeur de texte vous permet simplement de l'écrire, la console est ce qui va interpréter votre code et sortir un résultat.

#### Comment l'utiliser ?

Une fois que vous avez ouvert votre console, vous devrez aller dans le dossier où vous allez mettre votre fichier script python. Pour ceci il vous faut connaître deux commandes principales :

* Sur Mac :

```
cd
```
et

```
ls
```

* Sur Windows :

```
cd
```
et

```
dir
```


Pour aller dans le dossier dans lequel va se trouver votre fichier python, vous pouvez taper sur votre console :

```
cd chemin_vers_votre_fichier
```

Ceci est la structure générale. Prenons un exemple, si nous voulons aller dans notre dossier Téléchargements, on écrirait :

```
cd Downloads
```

Une fois que vous serez dans le bon dossier, vous pouvez exécuter votre code en tapant dans votre console :

`python nom_de_votre_fichier.py`


Par exemple, si nous avons un fichier nommé *hello_world.py*, on taperait pour l'exécuter :

`python hello_world.py`


Maintenant que l'on sait tout cela, écrivons un premier programme.

## Hello World

Tentons un premier programme dans notre éditeur de texte.

```Python
prenom = input("Quel est votre nom ? ")
print("Bonjour {}, comment allez vous aujourd'hui ?".format(prenom))
```

Ce programme demande à l'utilisateur votre nom et le stocke dans ce qu'on appelle une *variable*. En l'occurence, celle-ci s'appelle `prenom`

Ensuite, nous demandons au programme de dire bonjour au prénom qui a été renseigné dans la variable `prenom` grâce à la fonction `print()`

Ceci est le programme le plus simple du monde mais il nous permet de voir quelques concepts utiles. Créeons maintenant une application complète qui va, au passage, vous enseigner les concepts fondamentaux du langage Python.


## Un quiz pour apprendre Python

Rien de tel que de programmer un quiz pour apprendre. L'idée de cette application est de répondre à trois questions. L'utilisateur aura 3 "chances" pour répondre à toutes les questions.

Ceci n'est pas facile pour une première application, donc faisons le par étapes

### Faire une condition

Un premier concept à maîtriser est la façon dont on construit une condition. En effet, nous allons avoir besoin de vérifier si l'utilisateur a donné, ou non, la bonne réponse à la question.

Voici comment cela se structure :

```python
question = input("Quelle est la couleur du cheval blanc d'Henry IV ? ")

if question == "blanc":
  print("bravo ! c'est la bonne réponse")
else:
  print("Dommage... Ce n'était pas la bonne réponse")

```

Voici le principe pour formuler une condition. Elle commence par un `if` suivi de la condition que vous souhaitez vérifier. Si la condition n'est pas vérifiée, il faut que votre programme sache quoi faire. C'est ici que le `else` entre en jeu. Il va vous permettre de dire ce que le programme doit faire si la condition n'est pas remplie.

ATTENTION : l'indentation est hyper importante en Python. Si vous ne la respectez pas, le programme ne va pas fonctionner.


### Les boucles

Maintenant que l'on sait vérifier la réponse à une question posée, il faudrait qu'on ne passe pas à la question d'après si la réponse donnée est fausse. On peut le faire grâce à une boucle.

Il existe deux types de boucles

#### FOR

La boucle *for* permet d'itérer sur un nombre fini d'éléments. Pour notre cas, on pourrait dire par exemple que la personne a 3 chances avant de perdre le quiz et donc de sortir de la boucle

```Python
for i in range(0, 3):
  print("il vous reste {} chances".format(3 - i))
  question = input("Quelle est la couleur du cheval blanc d'Henry IV ?")
  if question == "blanc":
    print("Bravo, vous avez trouvé")
    break
  else:
    print("Dommage, vous n'avez pas la bonne réponse")
    if i == 2:
      print("Ah, vous avez perdu le jeu...")
```

Ici, nous comptons le nombre d'itérations grâce à la fonction `range()` qui permet de donner une valeur à `i` à chaque itération.

Ceci n'est pas la manière la plus élégante d'arriver à nos fins cependant. On peut voir un autre type de boucle qui devrait pouvoir nous aider

NB : Nous avons utilisé la notation `break` qui permet de sortir d'une boucle même si les itérations ne sont pas finies. Ceci est assez utile bien que pas forcément une best practice que d'utiliser ceci.

### While

La boucle *while* permet d'itérer tant qu'une condition est vraie. Ceci a l'avantage de ne pas avoir à spécifier le nombre d'itérations nécessaires dans la boucle. Réécrivons donc le même code avec une boucle *while*

```Python
question = input("Quelle est la couleur du cheval blanc d'Henry IV ?")
while question != "blanc":
  print("Dommage, ceci n'est pas la bonne réponse")
  question = input("Quelle est la couleur du cheval blanc d'Henry IV ?")

print("Bravo ! Tu as trouvé la réponse")

```
## Tout assembler

Maintenant que nous savons comment faire des boucles et des conditions, on a tout ce qu'il nous faut pour construire notre application quiz. Il faudra simplement réfléchir à la façon dont nous allons construire le code.

Nous pouvons construire notre application avec des boucles *for* ou des boucles *while*. Dans ce cas présent, nous avons choisi des boucles *while*

Nous avons posé trois questions à l'utilisateur

1) Combien de fois la France a gagné la coupe du monde
2) Quand a été fondé Apple
3) Qui a fondé SpaceX

```Python
nb_de_chances = 3

print("Voici notre quiz, tu as trois chances !")
question1= input("Combien de fois la France a gagné la coupe du monde ?")

while question1 != "2":
    if nb_de_chances == 0:
        print("Oh non ! Tu as perdu le jeu...")
        break
    else:
        nb_de_chances -= 1
        print("Dommage ! Il te reste {} chances".format(nb_de_chances))
        question1 = input("Combien de fois la France a gagné la coupe du monde ?")

if nb_de_chances > 0:
    question2 = input("Quand a été fondé Apple")
    while question2 != "1976":
        if nb_de_chances == 0:
            print("Oh non ! Tu as perdu le jeu...")
            break
        else:
            nb_de_chances -=1
            print("Dommage ! Il te reste {} chances".format(nb_de_chances))
            question2 = input("Quand a été fondé Apple ?")


if nb_de_chances >0:
    question3 = input("Qui a fondé SpaceX")
    question3 = question3.lower()
    while question3 != "elon musk":
        if nb_de_chances == 0:
            print("Oh non ! Tu as perdu le jeu...")
            break
        else:
            nb_de_chances -=1
            print("Dommage ! Il te reste {} chances".format(nb_de_chances))
            question3 = input("Qui a fondé SpaceX")
            question3 = question3.lower()
    if question3 == "elon musk":
        print("Bravo ! Tu as gagné le quiz !")
```

## Pour aller plus loin : Les fonctions

Lorsque l'on code, on essaie de respecter le plus possible le principe DRY : Don't Repeat Yourself. Le but est de ne jamais écrire deux fois le même code. Dans notre quiz plus haut, on peut voir que nous nous répétons souvent.

Un bon moyen de contracarer cela est de créer des *fonctions*. Une fonction est un bout de code que vous pouvez réutiliser à souhait dans votre script. Voici la structure générale

```
def nom_de_fonction(paramètre1, paramètre2,...,paramètreN):
  Votre code
```

Appliquons le donc pour notre quiz :

```Python
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
```

L'avantage ici, c'est que vous pouvez ajouter autant de questions que vous le souhaitez sans avoir à ajouter un paquet de code en plus !


## Conclusion

Ceci conclue donc notre workshop sur Python, n'hésitez pas à demander notre livre d'introduction à Python complet pour que vous puissiez reprendre les exercices et continuer de pratiquer. N'oubliez pas, c'est la pratique qui fera de vous un bon codeur !

Si vous êtes intéressé à l'idée d'apprendre les Data Sciences, regardez notre Bootcamp : [Jedha.co](https://jedha.co)
