<h1>Busca na Política</h1>
Projeto de um raspador de noticias em Python que tem a função de responder tambem perguntas referentes a politica.
A idéia é trazer um facilitador para os jornalistas, onde jornais selecionados são raspados para trazer as ultimas noticias pertinentes ao tema.

![image](https://github.com/DedecoDev/imersao_proj/assets/137828839/4a47e530-66ed-44dc-9a9a-976d29cb906c)

<h2>Desenvolvimento</h2>
Foi desenvolvido totalmente em LocalHost, usando Visual Studio, Bibliotecas Bootstrap, Python, Css, Javascript e HTML.
Um projeto responsivo!

<h2>Atualizações Futuras</h2>
Como não foi possivel rodas ambos os arquivos "py" juntos, optei por roda-los separadamente. Assim irei melhorar gradativamente o projeto para ser usado de forma definitiva.

<h2>Instalação</h2>
<ul>
  <li>Baixar o pacote do Projeto</li>
  <li>Baixar o Python no https://www.python.org/downloads/</li>
  <li>Instalar Python.exe ( Marcar add PATH )</li>
</ul>

<h2>VS Code</h2>
<ul>
  <li>Instalar o Python by Microsoft </li>
  <li>pip install requests</li>
  <li>pip install flask</li>
  <li>pip install google.generativeai</li>
  <li>pip install beautifulsoup4</li>
  <li>Ter uma conta google e acessar <a href="https://aistudio.google.com/app/apikey">AISTUDIO</a> para gerar uma API KEY <strong>(fig.01)</strong></li>
  <li>Acessar arquivo "config.py" e aplicar EM "minhaKEY" sua API KEY copiada no AI STUDIO para rodar projeto</li>
</ul>

<h5>(fig.01)</h5>
![image](https://github.com/DedecoDev/imersao_proj/assets/137828839/d083cdfb-7256-48dc-b307-c7d910a32235)

<h2>RODAR ARQUIVOS</h2>
<h3>Necessário rodar arquivos separados</h3>
<ul>
  <li>Python noticias.py ( Roda o raspador + Busca interna)</li>
  <li>Python gemini.py (Roda o API do Gemini)</li>
</ul>

<h2>Caracteristicas do Projeto</h2>
<ul>
<li>"Raspa" e exibe as últimas notícias dos principais sites do Brasil</li>
<li>Tem um campo de Busca para encontrar por palavras chaves as ultimas noticias "raspadas" <strong>(fig.02)</strong></li>
<li>Possui um campo de pergunta com filtro de palavras relacionadas a politica <strong>(fig.03) e (fig.04)</strong></li>
<li>Projeto responsivo</li>  
</ul>


