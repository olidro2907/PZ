from PyQt5 import QtWidgets, uic
from Projekt import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit,QPushButton, QMessageBox, QGraphicsScene
from PyQt5.QtGui import QIcon, QPixmap
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.NameImage.setFocus()
        self.ui.Load.clicked.connect(self.akcja)
        self.ui.Remove.clicked.connect(self.akcja)
        self.ui.NameImage.setText("C:/Users/Oliwia Drozdek/Pictures/MOJE NAJLEPSZE ZDJĘCIA/")
        self.scene=QGraphicsScene()

    def akcja(self):
        try:
            nadawca=self.sender()
            if nadawca.text()=='Załaduj':
                nazwa=self.ui.NameImage.text()
                pixmap=QPixmap()
                pixmap.load(nazwa)
                h=self.ui.View.height()
                w=self.ui.View.width()
                self.scene.addPixmap(pixmap.scaled(w,h))
                self.ui.View.setScene(self.scene)

            elif nadawca.text()=='Usuń':
                self.ui.NameImage.clear()

        except ValueError:
            QMessageBox.warning(self, "Błąd","Nie udało się wczytać zdjęcia.", QMessageBox.Ok)

app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()
sys.exit(app.exec())

