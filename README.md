# 🌦️ Weather API + Weather App

## 📌 Descripción del proyecto

Este proyecto consiste en el desarrollo de una **API REST del clima** utilizando **Flask y Python**, la cual consume información meteorológica en tiempo real desde **OpenWeatherMap**. Además, se implementó una **interfaz gráfica con Tkinter** para consultar el clima de cualquier ciudad de forma amigable.

La aplicación fue contenerizada utilizando **Docker** y se realizaron pruebas funcionales mediante **Postman**.

---

## 🎯 Objetivos

* Desarrollar una API REST utilizando Flask.
* Consumir datos desde una API externa (OpenWeatherMap).
* Gestionar variables de entorno para proteger la API Key.
* Dockerizar la aplicación para facilitar su despliegue.
* Realizar pruebas de funcionamiento con Postman.
* Implementar una interfaz gráfica utilizando Tkinter.

---

## 🛠️ Tecnologías utilizadas

* Python 3
* Flask
* Requests
* Python Dotenv
* Tkinter
* Pillow
* Docker
* Docker Compose
* Postman
* OpenWeatherMap API

---

## 📂 Estructura del proyecto

```text
weather-api/
│
├── app.py
├── weather_gui.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .env
├── weather_icon.png
└── venv/
```

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd weather-api
```

### 2. Crear el entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la API Key

Crear un archivo `.env` con el siguiente contenido:

```env
API_KEY=TU_API_KEY_DE_OPENWEATHERMAP
```

---

## 🐳 Ejecutar la API con Docker

Construir y ejecutar el contenedor:

```bash
docker compose up --build
```

La API estará disponible en:

```text
http://localhost:5000
```

---

## 🔗 Endpoints disponibles

### Inicio

```http
GET /
```

Respuesta:

```json
{
    "mensaje": "API Weather funcionando"
}
```

---

### Consultar clima por ciudad

```http
GET /weather/<city>
```

Ejemplo:

```http
GET /weather/Toluca
```

Respuesta:

```json
{
    "city": "Toluca",
    "country": "MX",
    "temperature": 19.5,
    "feels_like": 18.7,
    "weather": "muy nuboso",
    "humidity": 55,
    "wind": 0.72
}
```

---

## 🧪 Pruebas realizadas

Se realizaron pruebas utilizando **Postman** para verificar:

* Consulta exitosa de una ciudad válida.
* Manejo de errores cuando la ciudad no existe.
* Disponibilidad de la API.
* Respuestas en formato JSON.

---

## 🖥️ Interfaz gráfica

Se desarrolló una aplicación de escritorio utilizando **Tkinter**, la cual permite:

* Consultar el clima de cualquier ciudad.
* Visualizar temperatura y sensación térmica.
* Mostrar humedad y velocidad del viento.
* Indicar la fecha y hora de la consulta.
* Presentar emojis dinámicos según el estado del clima.
* Incorporar una imagen decorativa relacionada con el clima.

---

## 📸 Evidencias

Se anexan capturas de pantalla de:

* Ejecución de Docker Compose.
* Pruebas realizadas con Postman.
* Funcionamiento de la interfaz gráfica.
* Consulta exitosa del clima.

---

## 📚 Referencias

* https://flask.palletsprojects.com/
* https://openweathermap.org/api
* https://docs.docker.com/
* https://www.postman.com/
* https://docs.python.org/3/library/tkinter.html
* https://pillow.readthedocs.io/
