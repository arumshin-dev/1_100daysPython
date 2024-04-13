  tvShow = input("What is your favorite tv show? ")
  if tvShow == "peppa pig":
    print("Ugh, why?")
    faveCharacter = input("Who is your favorite character? ")
    if faveCharacter == "daddy pig":
      print("Right answer")
    else:
      print("Nah, Daddy Pig's the greatest")
  elif tvShow == "paw patrol":
    print("Aww, sad times")
  else:
    print("Yeah, that's cool and all…")

  order = input("What would you like to order: pizza or hamburger? ")
  if order == "hamburger":
    print("Thank you.")
    cheese = input("Do you want cheese?")
    if cheese == "yes":
      print("You got it.")
    else: 
      print("No cheese it is.")
  elif order == "pizza":
    print("Pizza coming up.")
    toppings = input("Do you want pepperoni on that?")
    if toppings == "yes":
      print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")

  print ("Are you a superfan of 'The Big Bang Theory' or a fake fan?")
  print()
  print("Answer these questions to find out.")

  Glasses = input("Does someone wear glasses?")
  if Glasses == "yes":
    print("Correct!")
  else:
    print("Wrong!")
    WhoGlasses = input("And who wears glasses?")
    if WhoGlasses == "Leonard":
      print("You got it")
    else:
      print("Try again!")