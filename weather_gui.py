import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime
from PIL import Image, ImageTk


def obtener_emoji(clima):
    clima = clima.lower()
    if "nube" in clima:
        return "☁️"
    elif "lluv" in clima:
        return "🌧️"
    elif "torment" in clima:
        return "⛈️"
    elif "niev" in clima:
        return "❄️"
    elif "sol" in clima or "despejado" in clima:
        return "☀️"
    elif "niebla" in clima:
        return "🌫️"
    else:
        return "🌤️"


def consultar_clima():
    ciudad = entrada_ciudad.get().strip()

    if not ciudad:
        messagebox.showwarning(
            "Advertencia",
            "Por favor, ingresa una ciudad."
        )
        return

    try:
        respuesta = requests.get(
            f"http://127.0.0.1:5000/weather/{ciudad}"
        )

        datos = respuesta.json()

        if respuesta.status_code != 200:
            messagebox.showerror(
                "Error",
                datos.get("error", "Ciudad no encontrada")
            )
            return

        emoji = obtener_emoji(datos["weather"])
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

        clima_label.config(
            text=f"{emoji} {datos['weather'].capitalize()}"
        )

        ciudad_label.config(
            text=f"📍 Ciudad: {datos['city']}, {datos['country']}"
        )

        temp_label.config(
            text=f"🌡️ Temperatura: {datos['temperature']} °C"
        )

        sensacion_label.config(
            text=f"🥵 Sensación térmica: {datos['feels_like']} °C"
        )

        humedad_label.config(
            text=f"💧 Humedad: {datos['humidity']} %"
        )

        viento_label.config(
            text=f"🌬️ Viento: {datos['wind']} m/s"
        )

        fecha_label.config(
            text=f"🕒 Consultado: {fecha}"
        )

    except requests.exceptions.ConnectionError:
        messagebox.showerror(
            "Error",
            "No se pudo conectar con la API.\n"
            "Verifica que Docker esté ejecutándose."
        )


# ==========================
# Ventana principal
# ==========================
ventana = tk.Tk()
ventana.title("Weather App Premium")
ventana.geometry("550x750")
ventana.configure(bg="#4A90E2")
ventana.resizable(False, False)


# ==========================
# Imagen superior
# ==========================
try:
    imagen = Image.open("weather_icon.png")
    imagen = imagen.resize((120, 120))  # Reducido ligeramente para ganar espacio

    icono = ImageTk.PhotoImage(imagen)

    label_icono = tk.Label(
        ventana,
        image=icono,
        bg="#4A90E2"
    )
    label_icono.pack(pady=(15, 0))  # Reducido el margen inferior

except FileNotFoundError:
    print("No se encontró weather_icon.png")


# ==========================
# Encabezado
# ==========================
titulo = tk.Label(
    ventana,
    text="Weather App",
    font=("Arial", 22, "bold"),  # Reducido de 24 a 22
    bg="#4A90E2",
    fg="white"
)
titulo.pack()

subtitulo = tk.Label(
    ventana,
    text="Consulta el clima de cualquier ciudad",
    font=("Arial", 11),  # Reducido de 12 a 11
    bg="#4A90E2",
    fg="white"
)
subtitulo.pack(pady=(0, 10))


# ==========================
# Tarjeta principal
# ==========================
frame = tk.Frame(
    ventana,
    bg="white",
    padx=25,
    pady=15,  # Reducido de 25 a 15 para evitar el desborde inferior
    bd=2,
    relief="groove"
)
# Eliminados expand=True y fill="both" para que el frame se adapte al contenido de forma natural
frame.pack(
    padx=20,
    pady=(5, 20)
)


# ==========================
# Entrada de ciudad
# ==========================
tk.Label(
    frame,
    text="🌍 Ciudad",
    font=("Arial", 13, "bold"),
    bg="white"
).pack(anchor="w")

entrada_ciudad = tk.Entry(
    frame,
    font=("Arial", 13),
    width=32
)
entrada_ciudad.pack(pady=5)


# ==========================
# Botón
# ==========================
boton = tk.Button(
    frame,
    text="🔍 Consultar clima",
    command=consultar_clima,
    font=("Arial", 12, "bold"),
    bg="#28A745",
    fg="white",
    padx=15,
    pady=5,  # Reducido de 10 a 5
    cursor="hand2"
)
boton.pack(pady=10)


# ==========================
# Separador
# ==========================
tk.Frame(
    frame,
    height=2,
    bg="#D3D3D3"
).pack(fill="x", pady=10)


# ==========================
# Resultados
# ==========================
clima_label = tk.Label(
    frame,
    text="🌤️ Bienvenido",
    font=("Arial", 22, "bold"),
    bg="white",
    fg="#1F2937"
)
clima_label.pack(pady=5)


# Se redujeron las fuentes de las etiquetas de 15 a 13 y el pady de 5 a 4
ciudad_label = tk.Label(
    frame,
    text="📍 Ciudad:",
    font=("Arial", 13),
    bg="white"
)
ciudad_label.pack(anchor="w", pady=4)

temp_label = tk.Label(
    frame,
    text="🌡️ Temperatura:",
    font=("Arial", 13),
    bg="white"
)
temp_label.pack(anchor="w", pady=4)

sensacion_label = tk.Label(
    frame,
    text="🥵 Sensación térmica:",
    font=("Arial", 13),
    bg="white"
)
sensacion_label.pack(anchor="w", pady=4)

humedad_label = tk.Label(
    frame,
    text="💧 Humedad:",
    font=("Arial", 13),
    bg="white"
)
humedad_label.pack(anchor="w", pady=4)

viento_label = tk.Label(
    frame,
    text="🌬️ Viento:",
    font=("Arial", 13),
    bg="white"
)
viento_label.pack(anchor="w", pady=4)

fecha_label = tk.Label(
    frame,
    text="🕒 Consultado:",
    font=("Arial", 13),
    bg="white"
)
fecha_label.pack(anchor="w", pady=4)


# ==========================
# Ejecutar aplicación
# ==========================
ventana.mainloop()