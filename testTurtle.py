
import random

def lotto (num):
     list =[]
     randloto = random.randint(0,45)
     for i in range(0,num,1):
          for i in range(0,6,1):
               while randloto in list:
                    randloto = random.randint(0,45)
               list.append(randloto)
               
          print(list)
          list =[]

select = int(input('몇번 뽑을건가여?'))
lotto(select)