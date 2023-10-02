from PyQt5.QtWidgets import *
from mainapp import MainApp
def main():
    a = QApplication([])
    w = MainApp()
    a.exec_()

main()