#Generate random passwords


import random 

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

length = int(input("Enter the length of your password: "))

password = []
for i in range(length): 
    character = "char(random.randint(65,122))" + "char(random.randint(35, 57))"
    password.append(random.choice(character))
password = shuffle(password)
print(password)




