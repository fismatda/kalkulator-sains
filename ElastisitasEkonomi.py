import os

while True:
  
  lanjut = 1
  
  p1 = int(input("Harga 1 : "))
  q1 = int(input("Jumlah 1 : "))
  p2 = int(input("Harga 2 : "))
  q2 = int(input("Jumlah 2 : "))
  
  p_avrg = ((p2-p1)/p1)*100
  q_avrg = (((q2-q1))/q1)*100
  
  if q_avrg == 0:
      elastisitas = "0" 
      sifat = " inelastis sempurna"
      lanjut = 0
  if p_avrg == 0:
      elastisitas = "∞"
      sifat = " elastis sempurna"
      lanjut = 0
  
  if lanjut == 1:
      elastisitas = str(abs(q_avrg/p_avrg))
  
      if float(elastisitas) > 1:
          sifat = " elastis"
      if float(elastisitas) == 1:
          sifat = " elastis uniter"
      if float(elastisitas) < 1:
          sifat = " inelastis"
  
  print(elastisitas+sifat)
  input("Enter To Restart >>>>")
  os.system("clear")
  
  """
  Fisika Matematika SMA Negeri 2 Jember (fismatda)
  8 April 2022
  """
