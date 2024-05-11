import subprocess

# Executar os scripts em subprocessos separados
subprocess.Popen(["python", "gemini.py"])
subprocess.Popen(["python", "noticias.py"])