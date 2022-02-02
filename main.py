virkne=[]
for i in range(2):
  virkne.append(int(input("Ievadi virknes skaitli:  ")))
n=int(input("Kuru virknes elementu tu vēlies: "))
for i in range (n-2):
  num=virkne[i]+virkne[i+1]
  if num>=10:
    virkne.append(num%10)
  else:
    virkne.append(num)
print("Virknes",n,"elements ir",virkne[n-1])


tot=0
num=int(input("Ievadi skaitli:  "))
tot+=num
num1=str(num)
pak=len(num1)
for i in range (len(num1)):
  pak-=1
  tot+=(num%10**pak)
print(tot)


num1=int(input("Ievadi skaitli:  "))
pak=len(str(num1))
digits=[]
for i in range (pak):
  pak-=1
  new=num1//(10**pak)
  digits.append(new)
  num1=num1%(10**pak)
smallest=0
digits.sort()
for i in range(len(digits)-1):
  if not digits[i]==0:
    if smallest==0:
      smallest=digits[i]
      digits.pop(digits[i])
number=''
smallest=str(smallest)
number+=smallest
for i in range(len(digits)):
  changed=str(digits[i])
  number+=changed
print(number)