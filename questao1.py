def imprime_soma_media():
  
  def le_numeros():
    numeros = []
    while(True):
      try: 
        numeros.append(float(input())) 
      except ValueError:
        if len(numeros) == 0:
          print('Nenhuma linha lida com conteúdo, portanto não há soma nem média!') 
        break
    return numeros
  
  numeros = le_numeros()

  def soma_numeros(*numeros):
    total = 0
    for num in numeros:
      total+=num
    return total   

  def media_numeros(*numeros):
    return soma_numeros(*numeros)/len(numeros)

  if(len(numeros) > 0): 
    print('Soma dos Números: %.2f' %(soma_numeros(*numeros)))      
    print('Média dos Números: %.2f' %(media_numeros(*numeros))) 

  
imprime_soma_media()