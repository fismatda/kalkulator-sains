import os


while True:
  tambah = 0
  cek_angka_awal = 0
  angka_awal = []
  adaawal = 0
  stop = 0
  backnum = 0
  angkapenting = input("Angka : ")
  if ',' in str(angkapenting) or '.' in str(angkapenting):
    if ',' in str(angkapenting):
      angkapecah = angkapenting.split(",")
    elif '.' in str(angkapenting):
      angkapecah = angkapenting.split(".")
  
  # Angka Awal
  
    angka_awal = list(angkapecah[0])
    if "1" in angka_awal or "2" in angka_awal or '3' in angka_awal or '4' in angka_awal or '5' in angka_awal or '6' in angka_awal or '7' in angka_awal or '8' in angka_awal or '9' in angka_awal:
      adaawal = 1
    while len(angka_awal) != 0 and angka_awal[0] == "0" :
      del(angka_awal[0])
  
  # Angka Akhir
    angka_akhir = list(angkapecah[1])
    if adaawal == 1:
      angka_akhir = list(angkapecah[1])
    elif adaawal == 0:
      while len(angka_akhir) != 0 and angka_akhir[0] == "0":
        del(angka_akhir[0])
      
    angkapenting_int = angka_awal + angka_akhir
    angkapenting_str = str(str(angkapenting_int).replace('[','').replace(']',''))
    print(f"Terdapat {len(angkapenting_int)} angka penting, yaitu {angkapenting_str}")
  
  else:
    angkapenting = list(str(angkapenting))
    while len(angkapenting) != 0 and angkapenting[0] == "0":
      del(angkapenting[0])
    backnum = len(angkapenting) - 1
  
    while len(angkapenting) !=0 and angkapenting[backnum] == "0":
      del(angkapenting[backnum])
      backnum = backnum -1
      
    angkapenting_str = str(str(angkapenting).replace('[','').replace(']',''))
    
    print(f"Terdapat {len(angkapenting)} angka penting, yaitu {angkapenting_str}")
  input("Enter To Restart >>>>")
  os.system("clear")
  
  """
  Fisika Matematika SMA Negeri 2 Jember (fismatda)
  8 April 2022
  """
