import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMainWindow
from principal import Ui_Buscardor
from resultado import Ui_Resultado
import os
###########################
###########################
# el programa me tiro varios errores
###########################
###########################

class resultado(QMainWindow):
    def __init__(self):
        super(Resultado, self).__init__() # no me encuentra resultado
        self.ui = Ui_Buscardor()
        self.ui.setupUi(self)
        self.opened_file = None
    @Slot()
    def cerrar(self):
        self.close()

class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_Buscardor()
        self.ui.setupUi(self)
        self.opened_file = None

    @Slot()
    def buscar(self):
        self.user_input = self.ui.lblNombre.text()
        print(self.user_input)
        self.user = os.popen("whoami").read()
        print(self.user)
        self.user = self.user.rsplit()
        self.user_ruta = "/home/" + self.user[0]
        print(self.user_ruta)
        os.chdir(self.user_ruta)
        self.resultado = os.popen("find -not -path '/\.' | grep '" + self.user + "'").read() # sigue con lo mismo del error
        #self.resultado = os.popen("find -not -path '/\.' | grep '" + self.user + "'").read()
        #TypeError: must be str, not list
        #Process finished with exit code 0
        print(self.resultado)
        self.ventanita = Resultado() # no me encuentra resultado
        self.ventainita.ui.txtResultado.setText(self.resultado)
        self.ventanita.show()


    @Slot()
    def borrar(self):
        self.ui.lblNombre.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec_())