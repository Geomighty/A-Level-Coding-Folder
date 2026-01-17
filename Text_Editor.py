import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, \
    QPushButton, QVBoxLayout, QLineEdit, QColorDialog, QMessageBox, QFileDialog, QHBoxLayout, QTextEdit
import PyQt6.QtCore as qtc 

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("George's Text Edit")

        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()

        open_button = QPushButton("Open")
        open_button.clicked.connect(self.open_action)
        horizontal_layout.addWidget(open_button)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_action)
        horizontal_layout.addWidget(save_button)

        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(self.quit_action)
        horizontal_layout.addWidget(quit_button)

        widget = QWidget()
        widget.setLayout(vertical_layout)
        self.setCentralWidget(widget)

        main_text = QTextEdit()
        text = main_text.toPlainText()
        main_text.setPlainText(text)
        vertical_layout.addWidget(main_text)
        vertical_layout.addLayout(horizontal_layout)

    def open_action(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Open File",             
            "",                   
            "Text Files (*.txt);;All Files (*)" 
        )

        if file_path:
            try:
          
                with open(file_path, 'r') as f:
                    content = f.read()
                    self.text.setText(content) 
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file: {e}")

    def save_action(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "Text Files (*.txt);;All Files (*)"
        )

        if file_path:
            try:
                text_content = self.text.toPlainText()
                with open(file_path, 'w') as f:
                    f.write(text_content)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file: {e}")
    
    def quit_action(self):
        dlg = QMessageBox.warning(self, "Quit?", "Are you sure", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        print(dlg)
        if dlg == QMessageBox.StandardButton.Ok:
            self.app.quit()


app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()