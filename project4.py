from requests import get

loc = get('https://ipapi.co/json/') 
ip = loc.json() 

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grouplabel = QtWidgets.QLabel(self.centralwidget)
        self.grouplabel.setGeometry(QtCore.QRect(260, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.grouplabel.setFont(font)
        self.grouplabel.setObjectName("grouplabel")
        self.display1 = QtWidgets.QLabel(self.centralwidget)
        self.display1.setGeometry(QtCore.QRect(210, 30, 241, 31))
        self.display1.setObjectName("display1")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(40, 410, 511, 61))
        self.output.setFrameShape(QtWidgets.QFrame.Box)
        self.output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output.setText("")
        self.output.setObjectName("output")
        self.buttonIP = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.IP())
        self.buttonIP.setGeometry(QtCore.QRect(200, 60, 221, 27))
        self.buttonIP.setObjectName("buttonIP")
        self.buttonLoc = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Location())
        self.buttonLoc.setGeometry(QtCore.QRect(200, 90, 221, 27))
        self.buttonLoc.setObjectName("buttonLoc")
        self.buttonCountry = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Country())
        self.buttonCountry.setGeometry(QtCore.QRect(200, 120, 221, 27))
        self.buttonCountry.setObjectName("buttonCountry")
        self.buttonPop = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Population())
        self.buttonPop.setGeometry(QtCore.QRect(200, 150, 221, 27))
        self.buttonPop.setObjectName("buttonPop")
        self.buttoPost = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Postal())
        self.buttoPost.setGeometry(QtCore.QRect(200, 180, 221, 27))
        self.buttoPost.setObjectName("buttoPost")
        self.buttonLat = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Latitude())
        self.buttonLat.setGeometry(QtCore.QRect(200, 210, 221, 27))
        self.buttonLat.setObjectName("buttonLat")
        self.buttonLong = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.Longitude())
        self.buttonLong.setGeometry(QtCore.QRect(200, 240, 221, 27))
        self.buttonLong.setObjectName("buttonLong")
        self.buttonCash = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Cash())
        self.buttonCash.setGeometry(QtCore.QRect(200, 240, 221, 27))
        self.buttonCash.setObjectName("buttonCash")
        self.buttonTime = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Timezone())
        self.buttonTime.setGeometry(QtCore.QRect(200, 270, 221, 27))
        self.buttonTime.setObjectName("buttonTime")
        self.buttonLang = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.Languages())
        self.buttonLang.setGeometry(QtCore.QRect(200, 300, 221, 27))
        self.buttonLang.setObjectName("buttonLang")
        self.buttonASN = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.ASN())
        self.buttonASN.setGeometry(QtCore.QRect(200, 330, 221, 27))
        self.buttonASN.setObjectName("buttonASN")
        self.buttonISP = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.ISP())
        self.buttonISP.setGeometry(QtCore.QRect(200, 360, 221, 27))
        self.buttonISP.setObjectName("buttonISP")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def IP(self):  
        self.output.setText("Your public IP address is " + ip['ip'])
    
    def Location(self):  
        self.output.setText("Your Location is  " + ip['city'] + ", " + ip['region'] + ", " + ip['region_code'] + ", " + ip['country_name']  + ", " + ip['country_code'])

    def Country(self):  
        self.output.setText("Your country's Capital is " + ip['country_capital'])

    def Population(self):  
        self.output.setText("Your country\'s Population is {}" .format(ip['country_population']))

    def Postal(self):  
        self.output.setText("Your Postal/Zip code is "+ ip['postal'])
    
    def Latitude(self):  
        self.output.setText("Your Latitude is {}" .format(ip['latitude']))

    def Longitude(self):  
        self.output.setText("Your Longitude is {}" .format(ip['longitude']))

    def Cash(self):  
        self.output.setText('Your country\'s Currency is ' + ip['currency_name']  + ", " + ip['currency'])

    def Timezone(self):  
        self.output.setText("Your country\'s Timezone is " + ip['timezone'])

    def Languages(self):  
        self.output.setText('Your country\'s Languages is ' + ip['languages'])

    def ASN(self):  
        self.output.setText("Your Autonomous System Number is " + ip['asn'])

    def ISP(self):  
        self.output.setText("Your Internet Service Provider is " + ip['org'])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grouplabel.setText(_translate("MainWindow", "BONAKid"))
        self.display1.setText(_translate("MainWindow", "What do you want to display? "))
        self.buttonIP.setText(_translate("MainWindow", " Public IP Address"))
        self.buttonLoc.setText(_translate("MainWindow", "Current Location "))
        self.buttonCountry.setText(_translate("MainWindow", "Capital of the Country"))
        self.buttonPop.setText(_translate("MainWindow", " Country Population"))
        self.buttoPost.setText(_translate("MainWindow", "Postal code"))
        self.buttonLat.setText(_translate("MainWindow", "Your Latitude"))
        self.buttonLong.setText(_translate("MainWindow", "Your Longitude"))
        self.buttonCash.setText(_translate("MainWindow", "Your Country's Currency"))
        self.buttonTime.setText(_translate("MainWindow", "Your Country\'s Timezone"))
        self.buttonLang.setText(_translate("MainWindow", "Your Country\'s Languages"))
        self.buttonASN.setText(_translate("MainWindow", "Autonomous System Number"))
        self.buttonISP.setText(_translate("MainWindow", "Internet Service Provider"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
