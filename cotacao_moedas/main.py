import requests

moeda = 'USD'
data = '2026-04-10'

def consumir_api_cotacao(moeda: str, data):
    try:
        link = f'https://brasilapi.com.br/api/cambio/v1/cotacao/{moeda}/{data}'

        resposta = requests.get(link)
        
        if resposta.status_code == 200:
            
            dados = resposta.json()
            cotacao_dolar = dados['cotacoes'][0]['cotacao_compra']

            print(dados['cotacoes'][0]['cotacao_compra'])

            return cotacao_dolar

        else:
            print(f'Error: Cód {resposta.status_code}')
    except:
        print('Não foi possível conectar')
    
    finally:
        print('fim')


if __name__=='__main__':
    consumir_api_cotacao(moeda, data)
