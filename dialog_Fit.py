# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_Fit.ui'
#
# Created: Thu Jul 19 19:30:54 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 745)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(1140, 680, 110, 41))
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(30, 60, 1221, 601))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1219, 599))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 678, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(88, 677, 62, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMaximum(2.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(160, 682, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.pB_reload = QtWidgets.QPushButton(Dialog)
        self.pB_reload.setGeometry(QtCore.QRect(1167, 20, 81, 27))
        self.pB_reload.setObjectName("pB_reload")
        self.pB_savecondtion = QtWidgets.QPushButton(Dialog)
        self.pB_savecondtion.setGeometry(QtCore.QRect(1020, 20, 131, 27))
        self.pB_savecondtion.setObjectName("pB_savecondtion")
        self.cB_use_anotherParams = QtWidgets.QCheckBox(Dialog)
        self.cB_use_anotherParams.setGeometry(QtCore.QRect(30, 23, 191, 22))
        self.cB_use_anotherParams.setObjectName("cB_use_anotherParams")
        self.lE_params = QtWidgets.QLineEdit(Dialog)
        self.lE_params.setEnabled(False)
        self.lE_params.setGeometry(QtCore.QRect(230, 20, 731, 31))
        self.lE_params.setObjectName("lE_params")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "Close", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "S02:", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("Dialog", "fit S02", None, -1))
        self.pB_reload.setText(QtWidgets.QApplication.translate("Dialog", "Reload", None, -1))
        self.pB_savecondtion.setText(QtWidgets.QApplication.translate("Dialog", "Save conditions", None, -1))
        self.cB_use_anotherParams.setText(QtWidgets.QApplication.translate("Dialog", "Use another parameters", None, -1))
        self.lE_params.setToolTip(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Write another parameters for fitting.</span></p><p><span style=\" font-size:10pt;\">Ex.1: parameter name: dR, initial value: 0.05, status[guess or set]: guess</span></p><p><span style=\" font-size:10pt;\">=&gt; dR=[0.05, guess] (use quotation mark for strings. Separate each parameters with \';\')</span></p><p><span style=\" font-size:10pt;\">Ex.2: parameter name: alpha, initial value: 0.05, status[guess or set]: guess, \'alpha\' should be between 0 and 1</span></p><p><span style=\" font-size:10pt;\">=&gt; dR=[0.05, guess, (0:1)] (use quotation mark for strings. Separate each parameters with \';\')</span><br/></p></body></html>", None, -1))

