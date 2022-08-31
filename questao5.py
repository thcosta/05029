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

def maior_menor_palavra(palavras):
  maior, menor = palavras[0], palavras[0]
  for palavra in palavras[1::-1]:
    if len(palavra) > len(maior):
      maior = palavra
    if len(palavra) < len(menor):
      menor = palavra
  return maior, menor

def busca_subcadeia(string, substring):
  def conta_caracteres(substring, subcadeia):
    total = 0
    for index, char in enumerate(substring):
      if char != subcadeia[index]:
        total += 1
    return total

  subindex = -1
  total_dist = -1
  for index, char in enumerate(string):
    if char == substring[0]:
      subcadeia = string[index:(len(substring)+index)]
      total = conta_caracteres(substring, subcadeia)
      if total_dist == -1 or total < total_dist:
        total_dist = total
        subindex = index
  return (total_dist, subindex) if subindex != -1 else (0, -1)

def imprime_subcadeia():
  palavras = le_palavras()

  if len(palavras) == 0:
    return
  
  string, substring = maior_menor_palavra(palavras)
  total_dist, subindex = busca_subcadeia(string, substring)
  if subindex == -1:
    print('Não existe subcadeia compatível')
  else:
    print('A subcadeia mais próxima tem %d caracteres distintos e começa na posição %d da cadeia %s' %(total_dist, subindex + 1, string))
    
imprime_subcadeia()