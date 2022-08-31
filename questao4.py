def le_numeros():
    numeros = []
    while(True):
      entrada = input()
      if len(numeros) == 2:
        break
      elif entrada == '':
        break
      else:
        numeros.append(entrada) 
    return numeros

def verifica_numeros(numeros):
  if len(numeros) == 0:
    print('Nenhum número lido!!') 
    return False
  elif not(numeros[0].isnumeric()) and not(numeros[1].isnumeric()):
    print('Base %s e expoente %s não estão no formato devido' %(numeros[0],numeros[1])) 
    return False
  elif not(numeros[0].isnumeric()):
    print('Base %s não está no formato devido' %(numeros[0]))
    return False
  elif not(numeros[1].isnumeric()):
    print('Expoente %s não está no formato devido' %(numeros[1]))
    return False
  else:
    return True

def calcula_expoente(base, expoente):
  return base**expoente

def imprime_expoente():
  numeros = le_numeros()
  if(verifica_numeros(numeros)):
    base, expoente = int(numeros[0]), int(numeros[1])
    print('%s elevado a %s é igual a %s' %(base, expoente, calcula_expoente(base, expoente)))
    
imprime_expoente()