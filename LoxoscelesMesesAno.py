#Análisando a relação entre acidentes loxoscélicos e a temperatura dos meses do ano
import matplotlib.pyplot as plt #importando a biblioteca para os gráficos
meses = ['Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'] #meses disponíveis de acidentes em CURITIBA na base do SUS de 2011-2021
acidentes = [1377,1248,1070,737,560,414,452,545,770,1006,1082,1198] #totais desses meses de acidentes
plt.plot(meses,acidentes) #plotando eixos x e y
plt.ylabel("Número de Acidentes") #legenda do eixo y
plt.xticks(rotation=45, ha="right") #aqui eu to girando 45º a escrita dos meses para melhor visualização
plt.show() #mostrando o gráfico
total = sum(acidentes) #somando todos os acidentes pra calcular em porcentagem cada mês
print(total) #vendo o total de acidentes desses 10 anos
for valor in acidentes: #para cada valor de Y, divida pelo total e * 100 = porcentagem
    porcentagem = (valor / total) * 100
    print(f'Porcentagens dos acidentes por mês: {porcentagem:.2f}%') #print a porcentagem com 2 casas decimais (2f)
    # meses com maiores índices de acidentes : Janeiro, Fevereiro, Novembro e Dezembro (teria relação com os meses mais quentes do ano?)
#catei do site clima tempo a temperatura dos útlimos 30 anos de Curitiba
meses = ['Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
tempMax = [25,25,25,23,20,19,18,20,20,22,23,25]
plt.plot(x,tempMax)
plt.ylabel("Temperatura Máxima")
plt.xticks(rotation=45, ha="right")
plt.show()
#sobrepondo as infos
plt.plot(meses, acidentes, label='Acidentes', marker='o')
plt.plot(meses, tempMax, label='Temperatura Máxima', marker='o')
plt.ylabel("Valores")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.show()
#preciso normalizar os dados, são valores mto diferentes os números de acidentes e a temp
#normalizando os dados
#pelo que entendi preciso de uma biblioteca chamada scikit-learn, ela ajusta meus dados nas posições entre 0-1
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
acidentes_normalizado = scaler.fit_transform([[x] for x in acidentes]) #normalizando os acidentes
tempMax_normalizado = scaler.fit_transform([[x] for x in tempMax]) #normalizando a temp

plt.plot(meses, acidentes_normalizado, label='Acidentes', marker='o')
plt.plot(meses, tempMax_normalizado, label='Temperatura Máxima', marker='o')

plt.ylabel("Valores Normalizados")
plt.xticks(rotation=45, ha="right")
plt.legend()

plt.show()
#primavera (setembro-dezembro) e verão (dezembro-março) são as épocas de maior índices de acidentes
