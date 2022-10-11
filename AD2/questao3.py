def leNumeros():
  numeros = []
  numeros += input().split()
  return numeros

def imprimirLista(numeros):
  print(f'A entrada é: {" ".join(numeros)}')
  return None

def menorValor(valores, inicio):
  posicao_menor = inicio
  for posicao in range(inicio + 1, len(valores)):
    if int(valores[posicao]) <= int(valores[posicao_menor]):
      posicao_menor = posicao
  return posicao_menor

def imprimirMenorValor(valores):
  menor_index = int(menorValor(valores, 0))
  print(f'O menor elemento da sequência é {valores[menor_index]}, ele está na posição {menor_index + 1}')

def trocarPosicao(valores, posicao1, posicao2):
  temp = valores[posicao1]
  valores[posicao1] = valores[posicao2]
  valores[posicao2] = temp
  return None

def ordenarMetodoSelecao(numeros):
  for index in range(len(numeros)-1):
    posicao_menor = menorValor(numeros, index)
    trocarPosicao(numeros, index, posicao_menor)
  print(f'Ordenando a sequêncica, temos: {" ".join(numeros)}')
  return None

def leBusca():
  print('Qual elemento você quer buscar?')
  return int(input())

def buscaBinaria(elemento, valores):
  inicio, fim = 0, len(valores) - 1
  while inicio <= fim:
      meio = (inicio + fim)//2
      if int(valores[meio]) == elemento:
        return meio
      elif int(valores[meio]) < elemento:
        inicio = meio + 1
      else:
        fim = meio - 1

def buscaSimples(elemento, valores, posicao_inicial=0):
  index = posicao_inicial
  while index < len(valores):
    if int(valores[index]) == elemento:
      return index
    else:
      index += 1
  return None

def buscarTodos(elemento, valores):
  posicoes, inicio = [], 0
  while inicio < len(valores) - 1:
    posicao = buscaSimples(elemento, valores, inicio)
    if posicao:
      posicoes.append(str(posicao))
      inicio = posicao + 1
    else:
      break
  return posicoes


def buscarElementos(numeros):
  elemento = leBusca()
  posicao_binaria = buscaBinaria(elemento, numeros)
  if posicao_binaria:
    print(f'Elemento {elemento} está na posicao {posicao_binaria + 1}')
    posicoes = buscarTodos(elemento, numeros)
    if len(posicoes) > 1:
      print(f'Além da posição {posicao_binaria + 1}, todas as posições que contém o {" ".join(posicoes)}')
  else:
    print(f'Elemento {elemento} não se encontra na sequência')
  return None

def main():
  try: 
    numeros = leNumeros()
    imprimirLista(numeros)
    imprimirMenorValor(numeros)
    ordenarMetodoSelecao(numeros)
    buscarElementos(numeros)
  except ValueError:
    print('Entrada inválida!')

main()