import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import CookieClickerWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CookieClickerWindow()
    window.show()
    sys.exit(app.exec_())