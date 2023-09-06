import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
from _datetime import datetime


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        self.distance_label = QLabel("Distance:")
        self.distance_line_adit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_line_adit = QLineEdit()

        calculate_button = QPushButton("Calculate speed")
        calculate_button.clicked.connect(self.calculate_speed)

        self.output_label = QLabel("")

        self.combo = QComboBox()
        self.combo.addItems(['Metrics (km)', 'Imperial (miles)'])

        # Add widgets to grid
        grid.addWidget(self.distance_label, 0, 0)
        grid.addWidget(self.distance_line_adit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_adit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, )
        grid.addWidget(self.output_label, 3, 0, )
        grid.addWidget(self.combo, 0, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        combo_text = self.combo.currentText()
        distance = self.distance_line_adit.text()
        time = self.time_line_adit.text()
        if combo_text == 'Metrics (km)':
            result_km = int(distance) / int(time)
            self.output_label.setText(f"Average Speed: {result_km} km/h")
        elif combo_text == "Imperial (miles)":
            result_miles = int(distance) / (1.6093440 * int(time))
            self.output_label.setText(f"Average Speed: {result_miles} mph")


app = QApplication(sys.argv)
age_calculator = SpeedCalculator()
age_calculator.show()
sys.exit(app.exec())
