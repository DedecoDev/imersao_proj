# -*- coding: utf-8 -*-
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

def raspador_camarasp():
    # URL da página
    url = 'https://www.camara.leg.br/noticias'

    # Requisição à página
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parse do conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar as notícias na página
        camarasp = soup.find_all('h3', class_='g-chamada__titulo')

        # Limite de 6 notícias
        camarasp = camarasp[:10]

        # Criar uma lista para armazenar os dados HTML formatados
        html_camarasp = []

        # Iterar sobre as chamadas
        for chamada in camarasp:
            # Extrair título e link da notícia
            titulo = chamada.find('a').find('span').text.strip()
            link = chamada.find('a')['href']

            # Obter a data e hora da última atualização
            data_hora_atualizacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            # Formatar a string HTML e adicioná-la à lista
            html_noticia = f"""
                    <div class="LinhaDaNoticia">
                        <span>Câmara dos Deputados</span>
                        <h3>{titulo}</h3>
                        <h4></h4>
                        <h5>{data_hora_atualizacao}</h5>
                        <div class="LinkLerMateria"><a href="{link}" target="_blank">Ler Matéria</a></div>
                    </div>
                  """
            
            html_camarasp.append(html_noticia)

        # Criar o HTML final unindo todas as notícias
        html_final = '\n'.join(html_camarasp)

        # Adicionar ao bloco da notícia com o ID específico
        html_camarasp = f"""
            <div class="BlocoLinhaDaNoticia" id="CamaraSP">
                <div class="LinhaDaNoticia ChamaBoxNoticia">Câmara dos Deputados</div>
                {html_final}
            </div>
        """

        return html_camarasp, "CamaraSP"
