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
