def le_linhas():
  try: 
    qtd_linhas = int(input())
  except ValueError:
    qtd_linhas = 0
  return qtd_linhas

def le_numeros(qtd_linhas):
  numeros = []
  for _ in range(qtd_linhas):
    numeros_linha = input().split()
    numeros+=numeros_linha
  return numeros

def busca_menor_maior(numeros):
  menor, maior = -1, -1
  for num in numeros:
    atual = int(num)
    if menor == -1 and maior == -1:
      menor, maior = atual, atual
    elif atual < menor:
      menor = atual
    elif atual > maior:
      maior = atual
  return menor, maior

def imprime_menor_maior():
  qtd_linhas = le_linhas()
  if (qtd_linhas) == 0:
    print('Nenhum número foi lido, portanto, sem mínimo e máximo!') 
  else:
    numeros = le_numeros(qtd_linhas)
    menor, maior = busca_menor_maior(numeros)
    print( 'Menor Número: %d e Maior Número: %d' %(menor, maior)) 

imprime_menor_maior()