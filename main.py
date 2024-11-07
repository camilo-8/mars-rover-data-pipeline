import requests
import pandas as pd
import os
from datetime import datetime, timedelta

# Substitua 'SUA_CHAVE_DE_API_AQUI' pela sua chave de API da NASA
api_key = ''

def obter_dados_api(url):
    '''
    Função para fazer uma solicitação GET a uma API e retornar os dados em formato JSON.
    Parâmetros:
        url (str): URL da API para realizar a solicitação.
    Retorna:
        dict: Dados da resposta em formato JSON, ou None se houver erro.
    '''
    response = requests.get(url)
    if response.status_code == 200:
        # Convertendo a resposta para formato JSON
        return response.json()
    else:
        print("Erro ao acessar a API")
        return None

def gerar_datas_mes_corrente():
    '''
    Função para gerar uma lista de datas do primeiro dia do mês atual.
    Retorna:
        list: Lista de strings com as datas no formato 'YYYY-MM-DD'.
    '''
    hoje = datetime.now()
    data_final = hoje - timedelta(days=0)
    data_inicial = hoje.replace(day=1)
    datas = []
    while data_inicial <= data_final:
        datas.append(data_inicial.strftime('%Y-%m-%d'))
        data_inicial += timedelta(days=1)
    return datas

def salvar_dados_csv(dados, nome_arquivo):
    '''
    Função para salvar dados em um arquivo CSV.
    Parâmetros:
        dados (list): Lista de dicionários com os dados a serem salvos.
        nome_arquivo (str): Nome do arquivo CSV.
    '''
    df = pd.DataFrame(dados)
    if not df.empty:
        df.to_csv(nome_arquivo, index=False)
        print(f"Dados salvos em {nome_arquivo}")
    else:
        print("Nenhum dado para salvar.")

def baixar_fotos(dados, diretorio_base):
    '''
    Função para fazer o download das fotos e organizá-las em pastas com formato YYYYMMDD.
    Parâmetros:
        dados (list): Lista de dicionários com informações sobre as fotos.
        diretorio_base (str): Caminho do diretório base para salvar as fotos.
    '''
    if not os.path.exists(diretorio_base):
        os.makedirs(diretorio_base)

    for item in dados:
        # Criando o diretório com a data no formato YYYYMMDD
        data_pasta = item['earth_date'].replace('-', '')
        diretorio_data = os.path.join(diretorio_base, data_pasta)

        if not os.path.exists(diretorio_data):
            os.makedirs(diretorio_data)

        # URL da imagem e nome do arquivo
        img_url = item['img_src']
        nome_arquivo = os.path.join(diretorio_data, f"{item['photo_id']}.jpg")

        # Verificando se a imagem já foi baixada para evitar duplicatas
        if not os.path.exists(nome_arquivo):
            print(f"Baixando imagem {item['photo_id']} para a data {item['earth_date']}...")
            img_data = requests.get(img_url).content
            with open(nome_arquivo, 'wb') as handler:
                handler.write(img_data)
        else:
            print(f"Imagem {item['photo_id']} já existe para a data {item['earth_date']}.")

def main():
    '''
    Função principal que coordena a execução do script.
    '''
    # Gerar as datas desejadas para busca
    datas_para_busca = gerar_datas_mes_corrente()
    photo_data = []

    # Coletar dados de fotos do rover para cada data
    for data in datas_para_busca:
        url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/Perseverance/photos?earth_date={data}&api_key={api_key}"
        print(f"Buscando dados para a data: {data}")
        dados = obter_dados_api(url)

        if dados and 'photos' in dados:
            for photo in dados['photos']:
                photo_data.append({
                    'photo_id': photo['id'],
                    'sol': photo['sol'],
                    'camera_id': photo['camera']['id'],
                    'camera_name': photo['camera']['name'],
                    'camera_full_name': photo['camera']['full_name'],
                    'img_src': photo['img_src'],
                    'earth_date': photo['earth_date'],
                    'rover_id': photo['rover']['id'],
                    'rover_name': photo['rover']['name'],
                    'rover_landing_date': photo['rover']['landing_date'],
                    'rover_launch_date': photo['rover']['launch_date'],
                    'rover_status': photo['rover']['status'],
                })

    # Criar o DataFrame e exibi-lo
    df = pd.DataFrame(photo_data)

    # Salvar os dados em um arquivo CSV
    salvar_dados_csv(photo_data, 'dados_rover.csv')

    # Baixar as fotos e organizá-las em pastas
    baixar_fotos(photo_data, 'fotos_rover_marte')

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    main()
