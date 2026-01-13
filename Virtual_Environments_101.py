import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg


# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template Window")

        form_layout = qtw.QFormLayout()
        grid_layout = qtw.QGridLayout()
        self.label = qtw.QLabel("Demo")
        grid_layout.addLayout(form_layout, 0, 0)
        form_layout.addRow("Name: ", qtw.QLineEdit())
        form_layout.addRow("Location: ", qtw.QLineEdit())
        combo_box = qtw.QComboBox()
        combo_box.addItems(["One", "Two", "Three"])
        combo_box.setCurrentIndex(2)
        grid_layout.addWidget(combo_box, 1, 0, 1, 3)
        button_1 = qtw.QPushButton()
        button_2 = qtw.QPushButton()
        grid_layout.addWidget(button_1, 2, 1)
        grid_layout.addWidget(button_2, 2, 3)
        
        widget = qtw.QWidget()
        widget.setLayout(grid_layout)
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = qtw.QApplication([])

window = MainWindow()
window.show()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event 
# loop has stopped.