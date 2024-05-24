#O objetivo do trabalho era criar um menu de Cupuaçu e Açai
print ('-- Bem vindo a loja de açai e cupuaçu da Hanna Câmara da Justa! --')
print ('---  Veja nossas opções no cardápio abaixo:  ---')
print ('________________________________________')
print ('|Tamanho do Copo| Cupuaçu   |  Açai  |')
print ('|     P         | R$ 10,00  | R$12,00|')
print ('|     M         | R$ 15,00  | R$17,00|')
print ('|     G         | R$ 19,00  | R$21,00|')
print ('________________________________________')
valor_total = 0 #esse vai ser o meu contador, começa a partir daqui a acumulação dos valores dos pedidos

while True: #começo do laço para retornar o menu para o usuário escrever opção que não existe ou fazer mais pedidos

#Açai ou Cupuaçu (sabor)
  sabor = input(' Qual o sabor, Açai (AC) ou Cupuaçu (CP) ?')
  sabor = sabor.upper()
  if sabor != 'AC' and sabor != 'CP' :
    print ('Escolha AC ou CP! ')
    continue
#Tamanhos dos copos
  tamanho_copo = input(' Qual o tamanho do copo? (P, M ou G)? ')  #Qual tamanho?
  tamanho_copo = tamanho_copo.upper() #recebo sempre em letra maiuscula
  if tamanho_copo != 'P' and tamanho_copo != 'M' and tamanho_copo != 'G':
    print ('Esse tamanho não existe, favor tentar novamente com P,M ou G! ') #e agora pra voltar pro menu?
    continue #retorna ao menu se o if ali de cima for verdadeiro

#Açais
  if tamanho_copo == 'P' and sabor == 'AC':
    print('Você selecionou um copo P do sabor Açai: R$: 12,00')
    valor_total = valor_total + 12
  elif tamanho_copo == 'M' and sabor == 'AC':
    print('Você selecionou um copo M do sabor Açai: R$: 17,00')
    valor_total = valor_total + 17
  elif tamanho_copo == 'G' and sabor == 'AC':
    print('Você selecionou um copo G do sabor Açai: R$: 21,00')
    valor_total = valor_total + 21
#Cupuaçu
  elif tamanho_copo == 'P' and sabor == 'CP':
    print('Você selecionou um copo P do sabor Cupuaçu: R$: 10,00')
    valor_total = valor_total + 10
  elif tamanho_copo == 'M' and sabor == 'CP':
    print('Você selecionou um copo P do sabor Cupuaçu: R$: 15,00')
    valor_total = valor_total + 15
  elif tamanho_copo == 'G' and sabor == 'CP':
    print('Você selecionou um copo P do sabor Cupuaçu: R$: 19,00')
    valor_total = valor_total + 19

  pedir_mais = input ('Deseja algo mais? Digite S para sim, ou qualquer outra tecla para NÃO: ') #Perguntar se deseja mais algo
  pedir_mais = pedir_mais.upper() #garantir que a entrada fique em maiúscula
  if pedir_mais == 'S' :
    continue #retorna lá pro menu
  else:
    print('Valor total da sua compra é: R${:.2f}'.format(valor_total))
  break
