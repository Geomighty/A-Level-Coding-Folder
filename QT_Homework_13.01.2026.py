import sys
# FIX 1: Import widgets from the specific submodule 'QtWidgets'
from PyQt6.QtWidgets import (QApplication, QMainWindow, QFormLayout, 
                             QLineEdit, QLabel, QPushButton, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template Window")

        # FIX 2: QMainWindow needs a "Central Widget" to hold the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        form_layout = QFormLayout()
        central_widget.setLayout(form_layout)

        # FIX 3: Use 'self.' to make these variables accessible in other methods
        self.line_edit = QLineEdit() 
        form_layout.addRow("Feet:", self.line_edit)

        self.label = QLabel("Result will appear here")
        form_layout.addRow("Metres:", self.label)

        button = QPushButton("Convert")
        form_layout.addRow(button) # Add the button to the layout

        button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        # FIX 4: Get text from the widget, don't try to convert the widget itself
        text_input = self.line_edit.text()
        
        # Check if input is valid before converting
        if text_input:
            try:
                feet = float(text_input) # Use float, not int, for better precision
                new_number = feet * 0.3048
                
                # FIX 5: Convert the number back to a string for setText
                self.label.setText(str(round(new_number, 2)))
            except ValueError:
                self.label.setText("Enter a number!")

# FIX 6: You need an Application instance and an execution loop to run the window
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()