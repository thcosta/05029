def imprime_menor_maior():
  
  try: 
    qtd_linhas = int(input())
  except ValueError:
    qtd_linhas = 0

  if (qtd_linhas) == 0:
    print('Nenhum número foi lido, portanto, sem mínimo e máximo!') 
  else:

    def le_numeros():
      numeros = []
      for _ in range(qtd_linhas):
        numeros_linha = input().split()
        numeros+=numeros_linha
      return numeros

    numeros = le_numeros()

    def busca_menor_maior(*numeros):
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

    menor, maior = busca_menor_maior(*numeros)
    print( 'Menor Número: %d e Maior Número: %d' %(menor, maior)) 

imprime_menor_maior()