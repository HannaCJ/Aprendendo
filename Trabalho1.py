#O objetivo do trabalho era criar um programa que desse descontos em produtos a partir
#de 1000 reais
print ('Bem vindos e Bem vindas à empresa Hanna Câmara da Justa! ') #nome com as boas vindas
print ('Caixa de Parafusos = 35R$') #valor unitário da caixa de parafusos
qtidade = int(input('Quantas caixas de parafusos gostaria de comprar? ')) #quantas unidades o cliente deseja, convertendo para inteiro
pagarP = qtidade*35 #variável para o valor total da compra
if pagarP < 1000: #se a variável da compra for menor que 1000 reais
  print ('Valor total da compra: {}.'.format(pagarP)) #não ganha desconto
elif pagarP >= 1000 and pagarP < 3000: #se maior ou igual a 1000 e menor que 3000 reais
  desconto1 = pagarP - pagarP*3/100 #desconto numero 1 = 3%
  print ('Valor total da compra: {}. Com desconto: {}'.format(pagarP,desconto1)) #print valor total com e sem desconto1
elif pagarP >= 3000 and pagarP < 5000: #se maior ou igual a 3000 e menor que 5000 reais
  desconto2 = pagarP - pagarP*5/100 #desconto numero 2 = 5%
  print ('Valor total da compra: {}. Com desconto: {}'.format(pagarP,desconto2)) #print valor total com e sem desconto2
else: #se maior ou igual a 5000
  pagarP >= 5000
  desconto3 = pagarP - pagarP*8/100 #desconto numero 3 = 8%
  print ('Valor total da compra: {}. Com desconto: {}'.format(pagarP,desconto3)) #print valor total com e sem desconto3