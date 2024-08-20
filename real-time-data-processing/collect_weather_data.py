import requests
from kafka import KafkaProducer
import json
import time

API_KEY = ''  # Insira sua API key aqui
CITY = 'Natal'
KAFKA_TOPIC = 'weather_data'
KAFKA_BROKER = 'localhost:9092'

# Configuração do Kafka Producer
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def get_weather_data():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

while True:
    weather_data = get_weather_data()
    producer.send(KAFKA_TOPIC, weather_data)
    print(f"Enviado: {weather_data}")
    time.sleep(10)  # Faz a consulta a cada 60 segundos
