def imprime_expoente():
  
  def le_numeros():
    numeros = []
    while(True):
      entrada = input()
      if len(numeros) == 2:
        break
      elif entrada == '':
        if len(numeros) == 0:
          print('Nenhum número lido!!') 
        break
      else:
        numeros.append(entrada) 
    return numeros

  entradas = le_numeros()

  if len(entradas) == 0:
    return
  elif not(entradas[0].isnumeric()) and not(entradas[1].isnumeric()):
    print('Base %s e expoente %s não estão no formato devido' %(entradas[0],entradas[1])) 
    return
  elif not(entradas[0].isnumeric()):
    print('Base %s não está no formato devido' %(entradas[0]))
    return
  elif not(entradas[1].isnumeric()):
    print('Expoente %s não está no formato devido' %(entradas[1]))
    return
  
  base, expoente = int(entradas[0]), int(entradas[1])

  def calcula_expoente(base, expoente):
    return base**expoente

  print('%s elevado a %s é igual a %s' %(base, expoente, calcula_expoente(base, expoente)))
    
imprime_expoente()