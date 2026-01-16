import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, \
    QPushButton, QVBoxLayout, QLineEdit, QColorDialog, QMessageBox, QFileDialog, QHBoxLayout
import PyQt6.QtCore as qtc 

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("George's Text Edit")

        #Layout Boxes
        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()

        #Open Button
        open_button = QPushButton("Open")
        #open_button.clicked.connect(self.open_action)
        horizontal_layout.addWidget(open_button)

        #Save Button
        save_button = QPushButton("Save")
        #save_button.clicked.connect(self.save_action)
        horizontal_layout.addWidget(save_button)

        #Quit button
        quit_button = QPushButton("Quit")
        #quit_button.clicked.connect(self.quit_action)
        horizontal_layout.addWidget(quit_button)

        #Central Widget
        widget = QWidget()
        widget.setLayout(horizontal_layout)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()