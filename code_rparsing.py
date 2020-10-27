tokens = ["(","(","(","int",")",")",")"]
i=0
rollback = 0
def term(x):
  global i,rollback
  aux=i
  if (len(tokens)<=aux):
    i=i-rollback
    rollback=0
    return False
  else:
    i=i+1
    rollback=rollback+1
    if(tokens[aux]==x):
      rollback=0
      return True
    else:
      i=i-rollback
      rollback=0
      return False
def E_1():
  print("E_1")
  print(i)
  return T()
def E_2():
  print("E_2")
  print(i)
  return T() and term ("+") and E()
def E():
  print("E")
  print(i)
  return E_1() or E_2()
def T_1():
  print("T_1")
  print(i)
  return term("int")
def T_2():
  print("T_2")
  print(i)
  return term("int") and term("*") and T()
def T_3():
  print("T_3")
  print(i)
  return term("(") and E() and term(")")
def T():
  print("T")
  print(i)
  return T_1() or T_2() or T_3()

print(E())
print(i)