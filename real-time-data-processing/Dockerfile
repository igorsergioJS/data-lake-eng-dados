# Usando uma imagem base do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho no container
WORKDIR /app

# Copiando o arquivo de script para o diretório de trabalho
COPY collect_weather_data.py /app/collect_weather_data.py

# Instalando as dependências necessárias
RUN pip install --no-cache-dir requests kafka-python

# Comando para executar o script
CMD ["python", "collect_weather_data.py"]
