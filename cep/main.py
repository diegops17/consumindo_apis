import requests

def consumir_api():
    
    try:
        link = 'https://cep.awesomeapi.com.br/json/01001000'

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
    consumir_api()
