def imprime_subcadeia():
  
  def le_palavras():
    palavras = []
    while(True):
      entrada = input()
      if len(palavras) == 2:
        break
      elif entrada == '' and len(palavras) == 0:
        palavras = []
        print('Nenhuma palavra lida!!') 
        break
      elif len(entrada.split()) == 0:
        palavras = []
        print('Mais de uma palavra na linha!!') 
        break
      else:
        palavras.append(entrada) 
    return palavras

  palavras = le_palavras()

  if len(palavras) == 0:
    return
  
  def maior_menor(*palavras):
    maior, menor = None, None
    for palavra in palavras:
      if not(maior) or len(palavra) >= len(maior):
        maior = palavra
      if not(menor) or len(palavra) <= len(menor):
        menor = palavra
    return maior, menor
  
  string, substring = maior_menor(*palavras)

  def busca_subcadeia(string, substring):
    subindex = -1
    total_dist = -1
    for index, char in enumerate(string):
      if char == substring[0]:
        subcadeia = string[index:(len(substring)+index)]

        def conta_caracteres(substring, subcadeia):
          total = 0
          for index, char in enumerate(substring):
            print(subcadeia[index])
            if char != subcadeia[index]:
              total += 1
          return total

        total = conta_caracteres(substring, subcadeia)
        if total_dist == -1 or total < total_dist:
          total_dist = total
          subindex = index
    return (total_dist, subindex) if subindex != -1 else (0, -1)

  total_dist, subindex = busca_subcadeia(string, substring)

  print('A subcadeia mais próxima tem %d caracteres distintos e começa na posição %d da cadeia %s' %(total_dist, subindex + 1, string))
    
imprime_subcadeia()