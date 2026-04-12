import requests
from datetime import datetime, timedelta



#print(date.today())
#moeda = 'USD'
#hoje = datetime.now().date()
hoje = datetime.now().date() - timedelta(days=1) #Parz esse ex tive que usar assim


def consumir_api_cotacao(moeda: str):
    data = hoje
    try:
        link = f'https://brasilapi.com.br/api/cambio/v1/cotacao/{moeda}/{data}'

        resposta = requests.get(link)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            #print(dados)
            
            cotacao_moeda = dados['cotacoes'][0]['cotacao_compra']
            #print(dados['cotacoes'][0]['cotacao_compra'])

            return cotacao_moeda
        else:
            print(f'Error: Cód {resposta.status_code}')
    except:
        print('Não foi possível conectar')
    finally:
        pass




def converter_real_dolar(real, moeda):
    cotacao = consumir_api_cotacao(moeda)
    valor_convertido = real / cotacao
    
    return valor_convertido, cotacao


def solicitar_dados():
    real = float(input('Informe quanto reais deseja converter R$ '))
    moeda = str(input('Informe a moeda para conversão [USD, EUR, JPY]: ')).strip().upper()

    valor_convertido, cotacao = converter_real_dolar(real, moeda)
    return real, cotacao, valor_convertido, moeda

if __name__=='__main__': 
    #cotacao = consumir_api_cotacao(moeda, hoje)

    resultado = solicitar_dados()
    
    print(f'''
          Com R$ {resultado[0]:.2f} reais; 
          Cotação dia á R$ {resultado[1]} reais; 
          Valor convertido foi de {resultado[2]:.2f} {resultado[3]}.
          ''')