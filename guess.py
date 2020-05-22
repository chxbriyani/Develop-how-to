import random

hidden = random.randrange(1,100)
i=0
print(hidden)
while i<10:
 guess=int(input("input number"))
 if (guess==hidden):
  print("right")
  break
 elif(guess<hidden):
  print("low")
 else:
  print("high")
 i+=1
