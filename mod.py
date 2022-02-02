def elem(skaitļi, ntais):
  for i in range(0,ntais-2):
    skaitļi.append((skaitļi[i]+skaitļi[i+1])%10)
  print(skaitļi)
  return