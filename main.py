import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor

class Circle:
    def __init__(self, x, y, diameter, color):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setWindowTitle("Random Circles")
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.drawButton = QPushButton(self.centralwidget)
        self.drawButton.setText("Draw Circle")
        self.drawButton.setObjectName("drawButton")
        
        self.layout.addWidget(self.drawButton)
        MainWindow.setCentralWidget(self.centralwidget)

class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.circles = []
        self.ui.drawButton.clicked.connect(self.add_circle)
        
    def add_circle(self):
        diameter = random.randint(20, 150)
        x = random.randint(0, self.width() - diameter - 10)
        y = random.randint(60, self.height() - diameter - 10)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append(Circle(x, y, diameter, color))
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(circle.color)
            painter.drawEllipse(circle.x, circle.y, circle.diameter, circle.diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec_())
