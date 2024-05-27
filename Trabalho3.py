#O objetivo do trabalho era criar um programa de copiadora, com serviços diferentes, quantidades de páginas e com extras, mostrando ao final o valor total a ser pago
def escolha_servico(): #DEFININDO A FUNÇÃO DOS SERVIÇOS
    while True:
        servicos = (input('Entre com o tipo de serviços: Digitalização (DIG), IMpressão Colorida (ICO), Impressão Preto e Branco (IBO) ou Fotocópia (FOT) '))
        servicos = servicos.upper()
        if servicos == 'DIG':
            return 1.10
        elif servicos == 'ICO':
            return 1.0
        elif servicos == 'IBO':
            return 0.40
        elif servicos == 'FOT':
            return 0.20
        else:
            print ('Opção inválida. Tente novamente com DIG, ICO, IBO, FOT')
            continue #retorna para linha 24 #Se digitar algo além das opções volta ao menu

def copiadora_desconto(): #DEFININDO OS DESCONTOS
    while True:
        try:  #tente fazer isso, pode gerar uma exceção
            num_pagina = int(input('Entre com a quantidade de páginas: '))
            if num_pagina < 10: #se for menor que 10
                return 0 #essa função me devolve o valor 40 reais
            elif num_pagina >= 10 and num_pagina < 100:
                return 0.10
            elif num_pagina >= 100 and num_pagina <1000:
                return 0.15
            elif num_pagina  >= 1000 and num_pagina <10000:
                return 0.20
            else: #páginas acima de 10000 não aceitas
                print ('Não aceitamos acima de 10000 páginas')
                continue #retorna para linha do codigo
        except ValueError:  #usuario digitou um valor não numérico para páginas
            print ('Por favor entre com um número inteiro')
            continue #retorna para linha
def servico_extra(): #DEFININDO VALORES EXTRAS
    acumulador = 0 # O acumulador tem q vir antes do while, acumula os valores adicionais
    while True:
        adicional = input ('Entre com o adicional desejado:\n'
        '1 - Encadernação simples \n'
        '2 - Encadernação capa dura \n'
        '3 - Não desejo mais nada \n') # O \n É para pular linha
        if adicional == '1':
            acumulador = acumulador + 10
        elif adicional == '2':
            acumulador = acumulador + 25
        elif adicional =='3':
            acumulador = acumulador + 0
            return acumulador
        else :
            print ('Opção inválida')
#MAIN
print ('Bem vindo a copiadora de Hanna Câmara da Justa')
return_servico = escolha_servico() #chamada das funções
return_desconto = copiadora_desconto()
return_extra = servico_extra ()
total = return_servico*return_desconto + return_extra
print (f'O total a pagar é : R$ {total} ({return_servico} * {return_desconto} + {return_extra}) ')
