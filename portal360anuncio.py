# -*- coding: utf-8 -*-
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

def raspador_portal360anuncio():
    # URL do site
    url = 'https://www.poder360.com.br/anuncios-do-governo/'

    # Requisição à página
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parse do conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

        # Encontrar as notícias na página
        portall360 = soup.find_all('div', class_='box-queue__data')

        # Obter a data e hora da atualização
        data_hora_atualizacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        # Limite de 5 notícias
        portall360 = portall360[:10]

        # Criar uma lista para armazenar os dados HTML formatados
        html_portall360 = []

        # Iterar sobre as notícias
        for noticia in portall360:
            # Extrair título e link da notícia
            titulo = noticia.find('h3', class_='box-queue__subhead').text.strip()
            link = noticia.find('h3', class_='box-queue__subhead').find('a')['href']

            # Formatar a string HTML e adicioná-la à lista
            html_noticia = f"""
                    <div class="LinhaDaNoticia">
                    <span>Portal 360 | Anúncio Governo</span>
                    <h3>{titulo}</h3>
                    <h5>{data_hora_atualizacao}</h5>
                    <div class="LinkLerMateria"><a href="{link}" target="_blank">Ler Matéria</a></div>
                    </div>
                  """
            
            html_portall360.append(html_noticia)

        # Criar o HTML final unindo todas as notícias
        html_final = '\n'.join(html_portall360)

        # Adicionar ao bloco da notícia com o ID específico
        html_portall360 = f"""
            <div class="BlocoLinhaDaNoticia" id="Portal360Anuncio">
                <div class="LinhaDaNoticia ChamaBoxNoticia">Portal 360 | Anúncio Governo</div>
                {html_final}
            </div>
        """

        return html_portall360, "Portal360Anuncio"



    


