# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana(object):
    def setupUi(self, Ventana):
        Ventana.setObjectName("Ventana")
        Ventana.resize(836, 506)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Ventana.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Ventana)
        self.centralwidget.setObjectName("centralwidget")
        self.lblXestion = QtWidgets.QLabel(self.centralwidget)
        self.lblXestion.setGeometry(QtCore.QRect(290, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblXestion.setFont(font)
        self.lblXestion.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.lblXestion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblXestion.setObjectName("lblXestion")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(240, 220, 100, 31))
        self.btnAceptar.setStyleSheet("font: 12pt \"Tahoma\";")
        self.btnAceptar.setObjectName("btnAceptar")
        self.lblApel = QtWidgets.QLabel(self.centralwidget)
        self.lblApel.setGeometry(QtCore.QRect(30, 120, 80, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblApel.setFont(font)
        self.lblApel.setStyleSheet("")
        self.lblApel.setAlignment(QtCore.Qt.AlignCenter)
        self.lblApel.setObjectName("lblApel")
        self.lblNombre = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre.setGeometry(QtCore.QRect(30, 160, 80, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblNombre.setFont(font)
        self.lblNombre.setStyleSheet("")
        self.lblNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.lblDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblDNI.setGeometry(QtCore.QRect(450, 160, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblDNI.setFont(font)
        self.lblDNI.setStyleSheet("")
        self.lblDNI.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDNI.setObjectName("lblDNI")
        self.lineTop = QtWidgets.QFrame(self.centralwidget)
        self.lineTop.setGeometry(QtCore.QRect(20, 100, 800, 16))
        self.lineTop.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineTop.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineTop.setObjectName("lineTop")
        self.lineEditDni = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDni.setGeometry(QtCore.QRect(130, 120, 311, 20))
        self.lineEditDni.setObjectName("lineEditDni")
        self.lineEditApel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditApel.setGeometry(QtCore.QRect(130, 160, 311, 20))
        self.lineEditApel.setObjectName("lineEditApel")
        self.lineEditNome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNome.setGeometry(QtCore.QRect(550, 160, 261, 20))
        self.lineEditNome.setObjectName("lineEditNome")
        self.lineBottom = QtWidgets.QFrame(self.centralwidget)
        self.lineBottom.setGeometry(QtCore.QRect(20, 190, 800, 16))
        self.lineBottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineBottom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineBottom.setObjectName("lineBottom")
        self.btnSair = QtWidgets.QPushButton(self.centralwidget)
        self.btnSair.setGeometry(QtCore.QRect(390, 220, 100, 31))
        self.btnSair.setStyleSheet("font: 12pt \"Tahoma\";")
        self.btnSair.setObjectName("btnSair")
        Ventana.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 25))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        Ventana.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana)
        self.statusbar.setObjectName("statusbar")
        Ventana.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(Ventana)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(Ventana)
        QtCore.QMetaObject.connectSlotsByName(Ventana)

    def retranslateUi(self, Ventana):
        _translate = QtCore.QCoreApplication.translate
        Ventana.setWindowTitle(_translate("Ventana", "MainWindow"))
        self.lblXestion.setText(_translate("Ventana", "XESTION CLIENTES"))
        self.btnAceptar.setText(_translate("Ventana", "Aceptar"))
        self.lblApel.setText(_translate("Ventana", "DNI"))
        self.lblNombre.setText(_translate("Ventana", "APELLIDOS"))
        self.lblDNI.setText(_translate("Ventana", "NOMBRE"))
        self.btnSair.setText(_translate("Ventana", "Salir"))
        self.menuArchivo.setTitle(_translate("Ventana", "Archivo"))
        self.actionSalir.setText(_translate("Ventana", "Salir"))
        self.actionSalir.setShortcut(_translate("Ventana", "Ctrl+S"))
