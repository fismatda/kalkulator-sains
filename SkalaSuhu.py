import os,re 

while True:
  suhu = input("Suhu : ")
  suhuvalue = float(re.sub("[^0-9]", "", suhu))
  
  if "C" in suhu or "c" in suhu:
    print("Celcius")
    kelvin = f"{suhuvalue + 273}K"
    fahrenheit = f"{(suhuvalue/100)*180+32}F"
    reamur = f"{suhuvalue*80/100}R"
    print(f"{kelvin}\n{fahrenheit}\n{reamur}")
  if "F" in suhu or "f" in suhu:
    print("Fahrenheit")
    suhuvalue = suhuvalue - 32
    celcius = f"{suhuvalue*100/180}C"
    kelvin = f"{suhuvalue*100/180+273}K"
    reamur = f"{suhuvalue*80/180}R"
    print(f"{celcius}\n{kelvin}\n{reamur}")
  if "R" in suhu or "r" in suhu:
    print("Reamur")
    celcius = f"{suhuvalue*100/80}C"
    kelvin = f"{suhuvalue*100/80+273}R"
    fahrenheit = f"{suhuvalue*180/80+32}F"
    print(f"{celcius}\n{kelvin}\n{fahrenheit}")
  if "K" in suhu or "k" in suhu:
    suhuvalue = suhuvalue - 273
    print("Kelvin")
    celcius = f"{suhuvalue}C"
    fahrenheit = f"{suhuvalue*180/100+32}F"
    reamur = f"{suhuvalue*80/100}R"
    print(f"{celcius}\n{fahrenheit}\n{reamur}")
  input("Enter to restart >> ")
  os.system("clear")
  
  """
  Fisika Matematika SMA Negeri 2 Jember (fismatda)
  15 April 2022
  """
