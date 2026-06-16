import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QVBoxLayout,
    QMessageBox
)

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setGeometry(300, 300, 350, 300)

        self.label_ciudad = QLabel("Ingresa una ciudad:")
        self.input_ciudad = QLineEdit()

        self.boton = QPushButton("Consultar clima")
        self.boton.clicked.connect(self.obtener_clima)

        self.resultado = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.label_ciudad)
        layout.addWidget(self.input_ciudad)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def obtener_clima(self):
        ciudad = self.input_ciudad.text().strip()

        if not ciudad:
            QMessageBox.warning(
                self,
                "Advertencia",
                "Ingresa una ciudad."
            )
            return

        try:
            respuesta = requests.get(
                f"http://localhost:5000/weather/{ciudad}"
            )

            datos = respuesta.json()

            if respuesta.status_code != 200:
                QMessageBox.critical(
                    self,
                    "Error",
                    datos.get("error", "No se encontró la ciudad.")
                )
                return

            self.resultado.setText(
                f"Ciudad: {datos['city']}, {datos['country']}\n"
                f"Temperatura: {datos['temperature']} °C\n"
                f"Sensación: {datos['feels_like']} °C\n"
                f"Clima: {datos['weather']}\n"
                f"Humedad: {datos['humidity']} %\n"
                f"Viento: {datos['wind']} m/s"
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"No se pudo conectar con la API.\n{e}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = WeatherApp()
    ventana.show()

    sys.exit(app.exec_())