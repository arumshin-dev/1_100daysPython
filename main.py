while(True):
  x = input("Choose a number: \n")
  y = input("Choose another one: \n")
  math = input("Choose an operation:\n \tOptions are: +, -, * or /.\n \tWrite 'exit' to finish.\n ")
  if math == "+":
    print("Result: ", int(x) + int(y))
  elif math =="-":
    print("Result: ", int(x) - int(y))
  elif math =="*":
    print("Result: ", int(x) * int(y))
  elif math =="/":
    print("Result: ", int(x) / int(y))
  elif math =="exit":
    break

  