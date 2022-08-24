VOGAIS_SEM_ACENTO = ['a', 'e', 'i', 'o', 'u']

def imprime_dados():
  
  def le_linhas():
    linhas = []
    while(True):
      entrada = input()
      if entrada == '':
        if len(linhas) == 0:
          print('Nenhuma linha não vazia foi lida!!') 
        break
      else:
        linhas.append(entrada)         
    return linhas
  
  linhas = le_linhas()
  if len(linhas) > 0:

    def imprime_sem_acentos():
      
      def mais_sem_acentos(*linhas):
        qtd_maior = 0
        maior = None
        for linha in linhas:

          def busca_vogais_sem_acento(linha):
            vogais_sem_acento = ''
            for char in linha:
              if(char.lower() in VOGAIS_SEM_ACENTO):
                vogais_sem_acento += char
            return vogais_sem_acento

          vogais_sem_acento = busca_vogais_sem_acento(linha)
          if(len(vogais_sem_acento) > qtd_maior):
            maior = linha
            qtd_maior = len(vogais_sem_acento)
        return maior, qtd_maior
      
      palavra, qtd_vogais = mais_sem_acentos(*linhas)
      print('Linha com mais vogais sem acento: %s' %(palavra))
      print('Quantidade de vogais sem acento: %d' %(qtd_vogais))

    imprime_sem_acentos()

    def imprime_maior_comprimento():
      todas_palavras = ' '.join(linhas)
      todas_palavras = todas_palavras.split()
      def busca_maior_palavra(*todas_palavras):
        maior = ''
        for palavra in todas_palavras:
          if len(palavra) > len(maior):
            maior = palavra
        return maior
      
      print('Palavra de maior comprimento lida: %s' %(busca_maior_palavra(*todas_palavras)))
  
    imprime_maior_comprimento()

    def imprime_mais_palindromos():
      def eh_palindromo(palavra):
        return palavra == palavra[::-1]

      def busca_palindromos(palavras):
        palindromos = []
        for palavra in palavras:
          if eh_palindromo(palavra):
            palindromos.append(palavra)
        return palindromos

      def busca_mais_palindromos(*linhas):
        maior = None
        qtd_maior = 0
        for linha in linhas:
          palindromos = busca_palindromos(linha.split())
          if len(palindromos) > qtd_maior:
            maior = linha
            qtd_maior = len(palindromos)
        return maior, qtd_maior

      palavra, qtd_palindromos = busca_mais_palindromos(*linhas)
      print('Linha com mais Palíndromos: %s' %(palavra))
      print('Quantidade de palavras Palíndromas: %d' %(qtd_palindromos))
    
    imprime_mais_palindromos()

imprime_dados()