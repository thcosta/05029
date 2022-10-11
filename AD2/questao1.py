def mostrar(nome):
  print(f'Conteúdo do Arquivo: {nome}')
  arquivo = open(nome, 'r')
  for linha in arquivo:
    print(linha.strip('\n'))
  arquivo.close()
  return None

def calcularMedia(nome):
  arquivo = open(nome, 'r')
  soma = 0
  tamanho = 0
  for linha in arquivo:
    soma += float(linha.strip('\n'))
    tamanho += 1
  media = soma/tamanho
  print(f'Média dos números contidos no arquivo: {media}')
  return media

def removerMenores(nome, valor):
  import os
  arquivo = open(nome, 'r')
  novo_arquivo = open(f'{nome}.temp', 'w')
  print(f'Conteúdo do Arquivo: {nome}')
  for linha in arquivo:
    numero = linha.strip('\n')
    if float(numero) >= valor:
      novo_arquivo.write(f'{numero}\n')
      print(numero)
  arquivo.close()
  novo_arquivo.close()
  os.rename(f'{nome}.temp', nome)

def main():
  try: 
    nome_arquivo = input()
    mostrar(nome_arquivo)
    media = calcularMedia(nome_arquivo)
    removerMenores(nome_arquivo, media)
  except IOError:
    print('Arquivo não encontrado!')
  except ValueError:
    print('Arquivo com conteúdo inválido!')

main()
  