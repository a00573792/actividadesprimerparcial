def calculadora_IMC():
  
  
  print ("Dame tu peso en kilos")
  imc1 = input()
  print ("Dame tu altura en metros")
  imc2 = input()
  imc = (int(imc1) / int(imc2)**2)
  print ("Tu IMC es",imc)
  
calculadora_IMC()  
