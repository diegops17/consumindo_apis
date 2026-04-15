import requests

def consumir_api(cod):
    try:
        link = f'https://http.dog/{cod}.json'

        resultado = requests.get(link)
    
        if resultado.status_code == 200:
            print(resultado.json())  
        else:
            print(f'Erro, cód: {resultado.status_code}')

    except:
        print('Não foi possível consumir API')
    
    finally:
        print('FIM')


if __name__ == '__main__':
    cod = int(input('Informe um código: '))
    resultado = consumir_api(404)

    print(resultado)