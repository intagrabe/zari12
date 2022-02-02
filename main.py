import math
import random
"""
a1=int(input("Ievadi virknes 1. skaitli: ")) #1
a2=int(input("Ievadi virknes 2. skaitli: ")) #7
ntais=int(input("Ievadi n elementu: ")) #12

def virkne(a,b,n):
  sk=[a,b]
  for i in range(1, n-1):
    p=sk[i-1]+sk[i]
    o=p%10
    sk.append(o)
  rez=sk[n-1]
  return rez
rezultats=virkne(a1,a2,ntais)
print(rezultats)
"""

naturals_sk=int(input("Ievadi naturālu skaitli, kuram ir ne vairāk kā 100 cipari lielāki par 0: "))
def sk(a,b):
  saraksts=[]
  stringots=str(a)
  garums=len(stringots)
  for i in range(garums):
    saraksts.append(b%(10**garums))
    garums-=1
  print(sum(saraksts))
  print(saraksts)
    
sk(naturals_sk,naturals_sk)
