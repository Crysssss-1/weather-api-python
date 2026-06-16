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