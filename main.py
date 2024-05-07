# equal
5 == 5

# not equal
3 != 5

# greater than
5 > 3

# greater than or equal to
5 >= 3

# less than
3 < 5

# less than or equal to
3 <= 5
myScore = int(input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")

myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")

score = int(input("What was your score on the test?"))
if score >= 80:
  print("Not too shabby")
elif score >= 70:
  print("Acceptable.")
else:
  print("Dude, you need to study more!")


birthYear = int(input("What year were you born?"))
if birthYear <= 1946:
  print("You are a Traditionalist.")
elif birthYear >= 1947 and birthYear <= 1964:
  print("Hey, Baby Boomer! How you doing?")
elif birthYear >= 1965 and birthYear <= 1981:
  print("Gen X! What's up?")
elif birthYear >= 1982 and birthYear <= 1995:
  print("Millenials! The age of tech!")
elif birthYear >= 1996:
  print("Hey, Gen Z! TikTok much?")
else: 
  print("Try again!")