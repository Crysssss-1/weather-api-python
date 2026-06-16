from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Obtener la API Key desde el archivo .env
API_KEY = os.getenv("API_KEY")

# Verificar que la API Key exista
if not API_KEY:
    raise ValueError("No se encontró la API_KEY. Verifica tu archivo .env")


@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API Weather funcionando"
    })


@app.route("/weather/<city>")
def weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
        f"&lang=es"
    )

    try:
        respuesta = requests.get(url, timeout=10)

        # Convertir la respuesta a JSON
        datos = respuesta.json()

        # Verificar si OpenWeather devolvió un error
        if respuesta.status_code != 200:
            return jsonify({
                "error": datos.get("message", "Ocurrió un error")
            }), respuesta.status_code

        return jsonify({
            "city": datos["name"],
            "country": datos["sys"]["country"],
            "temperature": datos["main"]["temp"],
            "feels_like": datos["main"]["feels_like"],
            "weather": datos["weather"][0]["description"],
            "humidity": datos["main"]["humidity"],
            "pressure": datos["main"]["pressure"],
            "wind": datos["wind"]["speed"]
        })

    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "No se pudo conectar con la API del clima",
            "detalle": str(e)
        }), 500

    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor",
            "detalle": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)