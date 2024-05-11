# -*- coding: utf-8 -*-
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

def raspador_oglobo():
    # URL do site
    url = 'https://oglobo.globo.com/politica/'

    # Requisição à página
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parse do conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

        # Encontrar as notícias na página
        oglobo_noticias = soup.find_all('div', class_='feed-post-body')

        # Limite de 5 notícias
        oglobo_noticias = oglobo_noticias

        # Criar uma lista para armazenar os dados HTML formatados
        html_oglobo = []

        # Iterar sobre as notícias
        for noticia in oglobo_noticias:
            # Extrair título e link da notícia
            titulo = noticia.find('div', class_='feed-post-body-title').find('h2').text.strip()
            link = noticia.find('div', class_='feed-post-body-title').find('h2').find('a')['href']

            # Extrair resumo se disponível
            resumo_tag = noticia.find('p', class_='feed-post-body-resumo')
            resumo = resumo_tag.text.strip() if resumo_tag else ''

            # Obter a data e hora da atualização
            data_hora_atualizacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            # Formatar a string HTML e adicioná-la à lista
            html_noticia = f"""
                   <div class="LinhaDaNoticia">
                    <div class="BoxComLinhaDaNoticia">
                        <h3>{titulo}</h3>
                        <h4>{resumo}</h4>
                        <h5>{data_hora_atualizacao}</h5>
                    </div>
                    <div class="LinkLerMateria"><a href="{link}" target="_blank">Ler Matéria</a></div>
                    </div>
                  """
            
            html_oglobo.append(html_noticia)

        # Criar o HTML final unindo todas as notícias
        html_final = '\n'.join(html_oglobo)

        # Adicionar ao bloco da notícia com o ID específico
        html_oglobo = f"""
            <div class="ListaDeTodasNoticias" id="oGlobo">             
                {html_final}
            </div>
        """

        return html_oglobo, "oGlobo"
