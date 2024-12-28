from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.story_box = QtWidgets.QTextEdit(self.centralwidget)
        self.story_box.setGeometry(QtCore.QRect(30, 30, 431, 501))
        self.story_box.setObjectName("story_box")
        font = QtGui.QFont("Comic Sans MS", 24)  
        font.setBold(True)  
        self.story_box.setFont(font)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(490, 30, 273, 139))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.welcome = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(36)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        self.Story_maker = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(22)
        self.Story_maker.setFont(font)
        self.Story_maker.setObjectName("Story_maker")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome.setText(_translate("MainWindow", "Welcome!"))
        self.Story_maker.setText(_translate("MainWindow", "Make me story"))
    
