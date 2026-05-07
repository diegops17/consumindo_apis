import requests
import urllib3
import pandas as pd
from tqdm import tqdm
import time


def consumir_api():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        headers = {
            'oUser': 'admin',
            'Content-Type': 'application/json'
        }

        payload = {
            'cod_usuario':'*',
            'login':'*',
            'order': 'login',
            'limit':'*'
        }

        url = f'https://192.168.00.00/app/outux/user/query?'
        #url_2 = f'https://192.168.00.00/app/outux/user/query?cod_usuario=*&login=*&order=login&limit=*'

        retorno = requests.get(url, params=payload, headers=headers, verify=False)

        if retorno.status_code == 200:
            #print(dict(retorno.json()))
            for i in tqdm(range(100), desc="Salvando"):
                time.sleep(0.03)
            
            try:
                dicionario_dados = {}
                dicionario_dados = retorno.json()
                df = pd.DataFrame(dicionario_dados)
                df.to_csv('codigos/usuarios_printer.csv', index=False, encoding='utf-8')

                print('Arquivo .csv salvo com sucesso!')

            except Exception as e:
                print(f'ERRO Não foi possível salvar .csv: {e}')  
        else:
            print(f'Cód diferente de 200 {retorno.status_code}')

    except Exception as e:
        print(f'Não foi possível conectar na API CÓD: {retorno.status_code}')
        print(f'ERRO: {e}')
    
    finally:
        print('*******Fim da consulta*******')

if __name__ == '__main__':
    consumir_api()