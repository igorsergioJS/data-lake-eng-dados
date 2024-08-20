from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Enviar uma mensagem de teste
producer.send('teste', value={'mensagem': 'teste kafka'})
producer.flush()
producer.close()

print("Mensagem enviada com sucesso")
