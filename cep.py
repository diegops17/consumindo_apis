import requests

def consumir_api(cep):
    
    try:
        #link = f'https://cep.awesomeapi.com.br/json/{cep}'
        link = f'https://brasilapi.com.br/api/cep/v1/{cep}'

        resposta = requests.get(link)
        
        if resposta.status_code == 200:
            print(resposta.json())
        else:
            print(f'Cep não localizado. CÓD: {resposta.status_code}.')

    except:
        print('Não foi possivel se conectar com a base de dados')
    finally:
        print('Fim')


if __name__=='__main__':
    cep = int(input('Informe o CEP, apenas números, ex: 01001000: '))
    consumir_api(cep)
