import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget,
                             QMessageBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from predictions import PredictionGenerator


class CookieClickerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cookie Clicker")

        self.clicks = 0
        self.prediction_limit = 3
        self.predictions_made = 0
        self.prediction_generator = PredictionGenerator()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.cookie_image = QLabel(self)
        pixmap = QPixmap("resources/cookie.jpg").scaled(350, 350, Qt.KeepAspectRatio)  # Масштабирование с сохранением пропорций
        self.cookie_image.setPixmap(pixmap)
        self.cookie_image.mousePressEvent = self.on_cookie_click

        self.clicks_label = QLabel(f"Нажатий: {self.clicks} / 10")
        self.prediction_label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.cookie_image)
        layout.addWidget(self.clicks_label)
        layout.addWidget(self.prediction_label)
        self.central_widget.setLayout(layout)

    def on_cookie_click(self, event):
        if self.clicks < 10:
            self.clicks += 1
            self.clicks_label.setText(f"Нажатий: {self.clicks} / 10")
            if self.clicks % 10 == 0 and self.predictions_made < self.prediction_limit:
                prediction = self.prediction_generator.get_prediction()
                self.prediction_label.setText(prediction)
                self.predictions_made += 1
        else:
            QMessageBox.information(self, "Информация", "Вы уже сделали 10 нажиманий!")