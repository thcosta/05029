def lerArquivo(nome):
  arquivo = open(nome, 'r', encoding='utf-8')
  conteudo = []
  for linha in arquivo:
    conteudo.append(linha.strip('\n'))
  arquivo.close()
  return conteudo

def verificarVogal(letra):
  vogais = ['a', 'e', 'i', 'o', 'u']
  if letra.lower() in vogais:
    return True
  return False

def contarVogais(conteudo):
  dicionario = {}
  for linha in conteudo:
    palavras = linha.split()
    for palavra in palavras:
      letra = palavra[0]
      if verificarVogal(letra):
        if dicionario.get(palavra):
          dicionario[palavra] += 1
        else:
          dicionario[palavra] = 1
  return dicionario

def ordenarMetodoSelecao(valores):
  for index in range(len(valores)-1):
    posicao_menor = 0
    for posicao in range(index + 1, len(valores)):
      if ord(valores[posicao]) < ord(valores[posicao_menor]):
        posicao_menor = posicao
    temp = valores[index]
    valores[index] = valores[posicao_menor]
    valores[posicao_menor] = temp
  return None

def mostraOcorrencias(dicionario):
  print('Conteúdo Ordenado das Palavras e Respectivas Ocorrências:')
  chaves = list(dicionario.keys())
  chaves.sort()
  for chave in chaves:
    if dicionario[chave] > 1:
        print(f'{chave} ocorre {dicionario[chave]} vezes')
    else:
        print(f'{chave} ocorre 1 vez')
  return None

def main():
  try: 
    nome_arquivo = input()
    conteudo = lerArquivo(nome_arquivo)
    dicionario = contarVogais(conteudo)
    mostraOcorrencias(dicionario)
  except IOError:
    print('Arquivo não encontrado!')
  except ValueError:
    print('Arquivo com conteúdo inválido!')

main()
  