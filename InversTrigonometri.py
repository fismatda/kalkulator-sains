import math,os
from math import sqrt as akar
from decimal import Decimal

def bulat(num):
  a = str(num)
  a = a.split(".")[1]
  if len(a) == 1 and a == "0":
    return(round(num))
  else:
    dec = Decimal(num)
    adj = abs(dec.adjusted())+2
    b = str(round(num, adj))
    b = b.split(".")[1]
    if  len(b) == 1 and int(b) == 0:
      return(round(num))
    else:
      return round(num, adj)

while True:
  select = input("invers dari (sin/cos/tan) : ")
  
  if select.replace(" ","") == "sin" :
    arcsin = input("sin : ")
    arcsin = math.asin(eval(arcsin))*180/math.pi
    print(f"{bulat(arcsin)}°")
  
  if select.replace(" ","") == "cos" :
    arccos = input("cos : ")
    arccos = math.acos(eval(arccos))*180/math.pi
    print(f"{bulat(arccos)}°")
  
  if select.replace(" ","") == "tan" :
    arctan = input("tan : ")
    arctan = math.atan(eval(arctan))*180/math.pi
    print(f"{bulat(arctan)}°")
  input("Enter >>>")
  os.system("clear")

"""
Fisika Matematika SMA Negeri 2 Jember (fismatda)
17 Februari 2022
"""
