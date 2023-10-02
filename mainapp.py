from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from api import *
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("CurrencyConverter.ui", self)
        self.setWindowTitle("Currency Converter")
        self.show()
        self.connectSignals()
        self.populateComboBoxes()
        self.lineEdit_2.setReadOnly(1)
    def convert(self):
        currencyValue1 = self.lineEdit.text()
        if currencyValue1 == '':
            QMessageBox.critical(self, 'Error!', 'You must provide an input first!')
            return
        currency1 = self.comboBox.currentText()
        currency2 = self.comboBox_2.currentText()
        if currency1 == currency2:
            QMessageBox.critical(self, 'Error!', 'The two currencies must be distinct!')
            return
        r = convertCurrencies(currency1, currency2)
        finalValue = round(float(currencyValue1) * r, 5)
        self.lineEdit_2.setText(str(finalValue))
    def populateComboBoxes(self):
        currencyList = ['ARS', 'AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'EGP', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'INR', 'JPY', 'KPW', 'LTL', 'NOK', 'PLN', 'RON', 'RSD', 'SEK',
                        'TRY', 'USD']

        self.comboBox.addItems(currencyList)
        self.comboBox_2.addItems(currencyList)
    def switchCurrencies(self):
        currencyValue1 = self.lineEdit.text()
        currencyValue2 = self.lineEdit_2.text()
        aux = currencyValue2
        self.lineEdit_2.setText(currencyValue1)
        self.lineEdit.setText(aux)
        currency1 = self.comboBox.currentText()
        currency2 = self.comboBox_2.currentText()
        indexToReplaceFirst = self.comboBox.findText(currency2)
        indexToReplaceSecond = self.comboBox_2.findText(currency1)
        self.comboBox.setCurrentIndex(indexToReplaceFirst)
        self.comboBox_2.setCurrentIndex(indexToReplaceSecond)
    def connectSignals(self):
        self.convertButton.clicked.connect(self.convert)
        self.switchButton.clicked.connect(self.switchCurrencies)
