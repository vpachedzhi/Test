import sys
from HeroDisplay import Hero_Display
from Map import Map
from PyQt4 import QtGui
from MainWindow import MainWindow


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    MW = MainWindow()
    MW.show()

    sys.exit(app.exec_())
