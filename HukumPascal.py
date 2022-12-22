from sympy import symbols, solve
from decimal import Decimal
import os,math,re,sys

def komatotitik(x):
  a = str(x)
  if "," in a:
    a = a.replace(",",".")
    return a
  else:
    return x

def converterunit(x):
  xunit = re.sub("[^a-zA-Z]", "", str(x))
  if "m" not in xunit:
    return float(eval(x))
  else:
    x = x.split("m")[0]
    
  if xunit == "m": 
    return float(eval(x))
  else:
    x = re.sub("[^0-9]", "", str(x))
    x = float(x)
    km2 = (10**3)**2
    hm2 = (10**2)**2
    dam2 = (10**1)**2
    dm2 = 1/10**2
    cm2 = 1/(10**2)**2
    mm2 = 1/(10**3)**2
    
    if "km" in xunit:
      return x*km2
    elif "hm" in xunit:
      return x*hm2
    elif "dam" in xunit:
      return x*dam2
    elif "dm" in xunit:
      return x*dm2
    elif "cm" in xunit:
      return x*cm2
    elif "mm" in xunit:
      return x*mm2

def luaslingkaran(x):
  a = converterunit(x)
  return math.pi*a*a

def bulat(num):
  a = str(num)
  a = a.split(".")[1]
  if len(a) == 1 and a == "0":
    return(round(num))
  else:
    dec = Decimal(num)
    adj = abs(dec.adjusted())+2
    return round(num, adj)
x = symbols('x')

while True:
  
  F1 = komatotitik(input("F1 (N): "))
  A1 = komatotitik(input("A1 (m2): ").replace("(", "('").replace(")","')"))
  F2 = komatotitik(input("F2 (N): "))
  A2 = komatotitik(input("A2 (m2): ").replace("(", "('").replace(")","')"))
  
  
  
  if "m" in A1 and "luaslingkaran" not in A1:
    A1 = converterunit(A1)
  if "m" in A2 and "luaslingkaran" not in A2:
    A2 = converterunit(A2)

  if len(str(F1)) != 0 :
    F1 = float(eval(str(F1)))
  else:
    nyari = "F1"
    F1 = x
  if len(str(A1)) != 0 :
    A1 = float(eval(str(A1)))
  else:
    nyari = "A1"
    A1 = x
  if len(str(F2)) != 0 :
    F2 = float(eval(str(F2)))
  else:
    nyari = "F2"
    F2 = x
  if len(str(A2)) != 0 :
    A2 = float(eval(str(A2)))
  else:
    nyari = "A2"
    A2 = x

  eq = F1/A1 - F2/A2
  
  solv = solve(eq)
  if len(solv) == 0:
    if F1/A1-F2/A2 == 0:
      print("Pernyataan benar")
    else:
      print("Pernyataan salah")
  else:
    if A2 == x or A1 == x:
      print(f"{nyari} = {bulat(float(solv[0]))}m2")
    else:
      print(f"{nyari} = {bulat(float(solv[0]))}")
  input("Enter to restart >>> ")
  os.system("clear")
  
    
  """
  Fisika Matematika SMA Negeri 2 Jember (fismatda)
  16 April 2022
  """
