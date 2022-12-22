import math, os
from decimal import Decimal

konstanta = 0

def bulat(num):
  a = str(num)
  a = a.split(".")[1]
  if len(a) == 1 and a == "0":
    return(round(num))
  else:
    dec = Decimal(num)
    adj = abs(dec.adjusted())+2
    return round(num, adj)

while True:
  titik1 = input("x1,y1 : ")
  titik2 = input("x2,y2 : ")
  #gradien = input("gradien : ")
  gradien = ""
  
  if len(gradien) == 0 and (len(titik1) and len(titik2)) != 0:
    titik1 = titik1.split(",")
    x1 = float(titik1[0])
    y1 = float(titik1[1])
    
    titik2 = titik2.split(",")
    x2 = float(titik2[0])
    y2 = float(titik2[1])
    
    gradien = (y2-y1)/(x2-x1)
    print(f"Gradien : {bulat(gradien)}")
    konstanta = bulat(y1 - gradien*x1)
    if konstanta == 0:
      konstanta = ""
    elif konstanta > 0:
      konstanta = f"+ {abs(konstanta)}"
    elif konstanta < 0:
      konstanta = f"- {abs(konstanta)}"
    print(f"Persamaan : y = {bulat(gradien)}x {konstanta}")
  input("Enter To Restart >>>>")
  os.system("clear")
  
  """
  Fisika Matematika SMA Negeri 2 Jember (fismatda)
  3 Desember 2021
  """
