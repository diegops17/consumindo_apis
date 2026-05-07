import requests
import urllib3

def consumir_api():

    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        #SALVADOR
        URL_BASE = 'https://192.168.00.00'


        URL_AUTENTICACAO = f"{URL_BASE}/login.fcgi"

        headers = {
            'Content-Type': 'application/json'
        }

        resposta_autenticacao = requests.post(URL_AUTENTICACAO, headers=headers, 
            json={ "login": "admin", "password": "admin"}, verify=False
        )
        
        if resposta_autenticacao.status_code == 200:
            cod_sessao = resposta_autenticacao.json()['session']
            #print("Código da Sessão:", cod_sessao)

            if not cod_sessao:
                print('Sessão não foi iniciada!')
            

            #CHAMADA LISTAGEM FUNCIONÁRIOS

            '''try:
                URL_USUARIOS = f'{URL_BASE}/load_users.fcgi?session={cod_sessao}'
            
                payload = {
                    "limit": 100,
                    "offset": 300
                }

                resposta_usuarios = requests.post(URL_USUARIOS, json=payload, headers=headers, verify=False)

                if resposta_usuarios.status_code == 200:

                    print('============ LISTA DE USUÁRIOS ============')
                    print(f'Quantidade restante de bobina: {resposta_usuarios.json()}')
                else:
                    print(f'Cód diferente de 200 na requisição o tamanho da bobina CÓD: {resposta_usuarios.status_code }')              
            except:
                print(f'Erro na requisição do tamanho da bobina:, {resposta_usuarios.status_code}. ERRO: {e}')'''


            try:
                tamanho_bobina = requests.post(f"{URL_BASE}/get_coil_paper.fcgi?session={cod_sessao}",
                    headers=headers, json={}, verify=False
                )
            
                if tamanho_bobina.status_code == 200:
                    print('============ TAMANHO BOBINA ============')
                    print(f'Quantidade restante de bobina: {tamanho_bobina.json()['coil_paper']}m')
                else:
                    print(f'Cód diferente de 200 na requisição o tamanho da bobina CÓD: {tamanho_bobina.status_code }')
            except Exception as e:
                print(f'Erro na requisição do tamanho da bobina:, {tamanho_bobina.status_code}. ERRO: {e}')
            
        else:
            print('Status diferente de 200 na requisição de logon')

    except Exception as e:
        print(f'Não foi possível conectar ao relógio, ERRO: {e}')

    finally:
        print('============ FIM DA CONSULTA ============')
        try:
            url_sair = f"{URL_BASE}/logout.fcgi?session={cod_sessao}"
            payload={}
            headers = {}

            resposta_sair = requests.request("POST", url_sair, headers=headers, data=payload, verify=False)
            #print(resposta_sair.json())
            print('Logoff realizado...')

        except Exception as e:
            print(f'Logoff não realizado, ERRO: {e}')

if __name__ == '__main__':
    consumir_api()
