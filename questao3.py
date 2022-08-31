VOGAIS_SEM_ACENTO = ['a', 'e', 'i', 'o', 'u']

def le_linhas():
  linhas = []
  while(True):
    entrada = input()
    if entrada == '':
      break
    else:
      linhas.append(entrada)         
  return linhas

def com_mais_vogais_sem_acentos(frases):
  def busca_vogais_sem_acento(frase):
    vogais_sem_acento = ''
    for char in frase:
      if(char.lower() in VOGAIS_SEM_ACENTO):
        vogais_sem_acento += char
    return vogais_sem_acento

  qtd_maior = 0
  maior = None
  for frase in frases:
    vogais_sem_acento = busca_vogais_sem_acento(frase)
    if(len(vogais_sem_acento) > qtd_maior):
      maior = frase
      qtd_maior = len(vogais_sem_acento)
  return maior, qtd_maior
  
def com_maior_palavra(frases):
  palavras = ' '.join(frases).split()
  maior = ''
  for palavra in palavras:
    if len(palavra) > len(maior):
      maior = palavra
  return maior

def com_mais_palindromos(frases):
  def busca_palindromos(palavras):
    def eh_palindromo(palavra):
      return palavra == palavra[::-1]
  
    palindromos = []
    for palavra in palavras:
      if eh_palindromo(palavra):
        palindromos.append(palavra)
    return palindromos

  maior = None
  qtd_maior = 0
  for frase in frases:
    palindromos = busca_palindromos(frase.split())
    if len(palindromos) > qtd_maior:
      maior = frase
      qtd_maior = len(palindromos)
  return maior, qtd_maior

def imprime_dados():
  linhas = le_linhas()
  if len(linhas) == 0:
    print('Nenhuma linha não vazia foi lida!!')
    return
  else:
    palavra_vogais, qtd_vogais = com_mais_vogais_sem_acentos(linhas)
    print('Linha com mais vogais sem acento: %s' %(palavra_vogais))
    print('Quantidade de vogais sem acento: %d' %(qtd_vogais))

    
    print('Palavra de maior comprimento lida: %s' %(com_maior_palavra(linhas)))

    palavra_palindromos, qtd_palindromos = com_mais_palindromos(linhas)
    print('Linha com mais Palíndromos: %s' %(palavra_palindromos))
    print('Quantidade de palavras Palíndromas: %d' %(qtd_palindromos))

imprime_dados()