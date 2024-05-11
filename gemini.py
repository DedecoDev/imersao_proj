from flask import Flask, render_template, request
import google.generativeai as genai
import re
from config import GOOGLE_API_KEY

# Substitua pela sua chave API
genai.configure(api_key=GOOGLE_API_KEY)

# Configuração do modelo Gemini
generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}
safety_settings = {
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL': 'BLOCK_NONE',
    'DANGEROUS': 'BLOCK_NONE'
}
model = genai.GenerativeModel(
    model_name='gemini-1.0-pro',
    generation_config=generation_config,
    safety_settings=safety_settings
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/perguntar", methods=["POST"])
def perguntar():
    pergunta = request.form["pergunta"].lower()  # Converter a pergunta para minúsculas

    # Adicionar instrução de logging
    app.logger.info("Recebida uma solicitação POST para a rota /perguntar")
    
    # Palavras-chave relacionadas a política e governo
    palavras_chave = [
        "política", 
        "governo", 
        "presidente", 
        "eleições", 
        "partido", 
        "democracia", 
        "constituição", 
        "ministério", 
        "deputado", 
        "senador", 
        "prefeito", 
        "vereador", 
        "congresso",
        "republica",
        "proclamação da republica",
        "independencia",
        "rio grande do sul"
        ]
    
    # Verificar se a pergunta contém alguma palavra-chave
    if any(palavra in pergunta for palavra in palavras_chave):
        response = model.generate_content(pergunta)
        resposta = response.text
        
        # Remover Markdown usando expressão regular
        resposta_sem_markdown = re.sub(r'[*`_#]', '', resposta)
        
        # Adicionar tags de parágrafo
        paragrafos = resposta_sem_markdown.split("\n\n")
        resposta_formatada = "".join([f"{p}" for p in paragrafos])
        
        return resposta_formatada
    
    else:
        return "Desculpe, mas essa pergunta não é pertinente ao assunto do site."

if __name__ == "__main__":
    app.run(debug=True)
