import math, os

while True:
  a = input("a : ")
  b = input("b : ")
  c = input("c : ")
  
  number = ["",""]
  urut = 0
  miring = 0
  
  if a.isdigit() == True:
          number[urut] = a
          urut = urut + 1
  
  if b.isdigit() == True:
          number[urut] = b
          urut = urut + 1
  
  if c.isdigit() == True:
          number[urut] = c
          miring = 1
  
  if miring == 1:
      print(math.sqrt(int(number[1])**2-int(number[0])**2))
  else:
      print(math.sqrt(int(number[0])**2+int(number[1])**2))
  input("Enter To Restart >>>>")
  os.system("clear")
  
    
  """
  Fisika Matematika SMA Negeri 2 Jember (fismatda)
  8 April 2022
  """
