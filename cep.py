import requests



#CEP que vai buscar
cep = 'CEP A CONSULTAR'
#Tratando o cep para não dar erro
cep = cep.replace('-', '').replace('.', '').replace(' ', '')
if len(cep) == 8:
    #Fazendo requisição no link de consulta
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)

    #Extraindo os resultados
    dic_requisicao = requisicao.json()
    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']

    print(uf, cidade, bairro)

else:
    print('CEP inválido')
