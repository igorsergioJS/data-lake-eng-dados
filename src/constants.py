import os

# API params
PATH_LAST_PROCESSED = "./data/last_processed.json"
CITY = "Natal"
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY", "api-key")
URL_API = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# POSTGRES PARAMS
user_name = os.getenv("POSTGRES_DOCKER_USER", "localhost")
POSTGRES_URL = f"jdbc:postgresql://localhost:5432/postgres"
POSTGRES_PROPERTIES = {
    "user": "postgres",
    "password": "postgres",
    "driver": "org.postgresql.Driver",
}

# Columns to keep
WEATHER_COLUMNS = [
    "main.temp",
    "main.humidity",
    "main.pressure",
    "weather[0].description",
    "wind.speed",
]
