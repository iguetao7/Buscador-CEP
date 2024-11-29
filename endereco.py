import requests
import pprint



#Informações para busca
uf = str(input('Qual abreviação do estado: '))
cidade = str(input('Qual cidade: '))
rua = str(input('Qual a rua: '))

#Fazendo requisição no link de consulta
link = f'https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/'
requisicao = requests.get(link)
print(requisicao)

#Extraindo os resultados
dic_requisicao = requisicao.json()
pprint.pprint(dic_requisicao)
