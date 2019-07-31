# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 535)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("socks4gui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnListen = QtWidgets.QPushButton(self.centralwidget)
        self.btnListen.setObjectName("btnListen")
        self.horizontalLayout.addWidget(self.btnListen)
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setEnabled(False)
        self.btnStop.setCheckable(False)
        self.btnStop.setChecked(False)
        self.btnStop.setFlat(False)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.tabCapture = QtWidgets.QWidget()
        self.tabCapture.setObjectName("tabCapture")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tabCapture)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lstCapture = QtWidgets.QListWidget(self.tabCapture)
        self.lstCapture.setObjectName("lstCapture")
        self.verticalLayout_2.addWidget(self.lstCapture)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cmbViewObject = QtWidgets.QComboBox(self.tabCapture)
        self.cmbViewObject.setObjectName("cmbViewObject")
        self.cmbViewObject.addItem("")
        self.cmbViewObject.addItem("")
        self.cmbViewObject.addItem("")
        self.horizontalLayout_2.addWidget(self.cmbViewObject)
        self.cmbViewType = QtWidgets.QComboBox(self.tabCapture)
        self.cmbViewType.setObjectName("cmbViewType")
        self.cmbViewType.addItem("")
        self.cmbViewType.addItem("")
        self.cmbViewType.addItem("")
        self.horizontalLayout_2.addWidget(self.cmbViewType)
        self.btnClearHistory = QtWidgets.QPushButton(self.tabCapture)
        self.btnClearHistory.setObjectName("btnClearHistory")
        self.horizontalLayout_2.addWidget(self.btnClearHistory)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.txtData = QtWidgets.QTextEdit(self.tabCapture)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.txtData.setFont(font)
        self.txtData.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.txtData.setReadOnly(True)
        self.txtData.setAcceptRichText(True)
        self.txtData.setObjectName("txtData")
        self.verticalLayout_3.addWidget(self.txtData)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmbDetailType = QtWidgets.QComboBox(self.tabCapture)
        self.cmbDetailType.setObjectName("cmbDetailType")
        self.cmbDetailType.addItem("")
        self.cmbDetailType.addItem("")
        self.cmbDetailType.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbDetailType)
        self.chkShowEdit = QtWidgets.QCheckBox(self.tabCapture)
        self.chkShowEdit.setChecked(True)
        self.chkShowEdit.setObjectName("chkShowEdit")
        self.horizontalLayout_3.addWidget(self.chkShowEdit)
        self.btnSaveDetail = QtWidgets.QPushButton(self.tabCapture)
        self.btnSaveDetail.setObjectName("btnSaveDetail")
        self.horizontalLayout_3.addWidget(self.btnSaveDetail)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tabCapture, "")
        self.tabHijack = QtWidgets.QWidget()
        self.tabHijack.setObjectName("tabHijack")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabHijack)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.chkReplace = QtWidgets.QCheckBox(self.tabHijack)
        self.chkReplace.setChecked(True)
        self.chkReplace.setObjectName("chkReplace")
        self.horizontalLayout_5.addWidget(self.chkReplace)
        self.chkIgnore = QtWidgets.QCheckBox(self.tabHijack)
        self.chkIgnore.setChecked(True)
        self.chkIgnore.setObjectName("chkIgnore")
        self.horizontalLayout_5.addWidget(self.chkIgnore)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.chkEncap = QtWidgets.QCheckBox(self.tabHijack)
        self.chkEncap.setObjectName("chkEncap")
        self.horizontalLayout_7.addWidget(self.chkEncap)
        self.txtEncap = QtWidgets.QLineEdit(self.tabHijack)
        self.txtEncap.setObjectName("txtEncap")
        self.horizontalLayout_7.addWidget(self.txtEncap)
        self.btnEncap = QtWidgets.QPushButton(self.tabHijack)
        self.btnEncap.setObjectName("btnEncap")
        self.horizontalLayout_7.addWidget(self.btnEncap)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tblRule = QtWidgets.QTableWidget(self.tabHijack)
        self.tblRule.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblRule.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblRule.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblRule.setObjectName("tblRule")
        self.tblRule.setColumnCount(4)
        self.tblRule.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblRule.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblRule.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblRule.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblRule.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tblRule)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnAddRule = QtWidgets.QPushButton(self.tabHijack)
        self.btnAddRule.setObjectName("btnAddRule")
        self.horizontalLayout_6.addWidget(self.btnAddRule)
        self.btnUpRule = QtWidgets.QPushButton(self.tabHijack)
        self.btnUpRule.setObjectName("btnUpRule")
        self.horizontalLayout_6.addWidget(self.btnUpRule)
        self.btnDownRule = QtWidgets.QPushButton(self.tabHijack)
        self.btnDownRule.setObjectName("btnDownRule")
        self.horizontalLayout_6.addWidget(self.btnDownRule)
        self.btnDelRule = QtWidgets.QPushButton(self.tabHijack)
        self.btnDelRule.setObjectName("btnDelRule")
        self.horizontalLayout_6.addWidget(self.btnDelRule)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tabHijack, "")
        self.tabSetting = QtWidgets.QWidget()
        self.tabSetting.setObjectName("tabSetting")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabSetting)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.tabSetting)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.txtSetPort = QtWidgets.QLineEdit(self.tabSetting)
        self.txtSetPort.setObjectName("txtSetPort")
        self.horizontalLayout_8.addWidget(self.txtSetPort)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.tabSetting)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.txtSetLog = QtWidgets.QLineEdit(self.tabSetting)
        self.txtSetLog.setObjectName("txtSetLog")
        self.horizontalLayout_9.addWidget(self.txtSetLog)
        self.btnLog = QtWidgets.QPushButton(self.tabSetting)
        self.btnLog.setObjectName("btnLog")
        self.horizontalLayout_9.addWidget(self.btnLog)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.tabSetting)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.txtSetHexLen = QtWidgets.QLineEdit(self.tabSetting)
        self.txtSetHexLen.setObjectName("txtSetHexLen")
        self.horizontalLayout_10.addWidget(self.txtSetHexLen)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.tabSetting)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.txtSetDataLen = QtWidgets.QLineEdit(self.tabSetting)
        self.txtSetDataLen.setObjectName("txtSetDataLen")
        self.horizontalLayout_11.addWidget(self.txtSetDataLen)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tabSetting, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.txtConsole = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtConsole.sizePolicy().hasHeightForWidth())
        self.txtConsole.setSizePolicy(sizePolicy)
        self.txtConsole.setReadOnly(True)
        self.txtConsole.setObjectName("txtConsole")
        self.verticalLayout_4.addWidget(self.txtConsole)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Socks4GUI - trichimtrich"))
        self.btnListen.setText(_translate("MainWindow", "Listen"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.cmbViewObject.setItemText(0, _translate("MainWindow", "All"))
        self.cmbViewObject.setItemText(1, _translate("MainWindow", "From Sender"))
        self.cmbViewObject.setItemText(2, _translate("MainWindow", "From Receiver"))
        self.cmbViewType.setItemText(0, _translate("MainWindow", "All"))
        self.cmbViewType.setItemText(1, _translate("MainWindow", "Edited Packet"))
        self.cmbViewType.setItemText(2, _translate("MainWindow", "Ignored Packet"))
        self.btnClearHistory.setText(_translate("MainWindow", "Clear"))
        self.txtData.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.cmbDetailType.setItemText(0, _translate("MainWindow", "Hexdump"))
        self.cmbDetailType.setItemText(1, _translate("MainWindow", "Raw data"))
        self.cmbDetailType.setItemText(2, _translate("MainWindow", "Base64"))
        self.chkShowEdit.setText(_translate("MainWindow", "Show Edit"))
        self.btnSaveDetail.setText(_translate("MainWindow", "Save Raw"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCapture), _translate("MainWindow", "Capturing"))
        self.chkReplace.setText(_translate("MainWindow", "Enable Replace Mode"))
        self.chkIgnore.setText(_translate("MainWindow", "Enable Ignore Mode"))
        self.chkEncap.setText(_translate("MainWindow", "Enable Encap/Decap"))
        self.btnEncap.setText(_translate("MainWindow", "Browse"))
        item = self.tblRule.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "isEnabled"))
        item = self.tblRule.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tblRule.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Match String"))
        item = self.tblRule.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Replace String"))
        self.btnAddRule.setText(_translate("MainWindow", "Add"))
        self.btnUpRule.setText(_translate("MainWindow", "Up"))
        self.btnDownRule.setText(_translate("MainWindow", "Down"))
        self.btnDelRule.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHijack), _translate("MainWindow", "Hijacking"))
        self.label.setText(_translate("MainWindow", "Port:"))
        self.txtSetPort.setText(_translate("MainWindow", "9999"))
        self.label_2.setText(_translate("MainWindow", "Logfile:"))
        self.txtSetLog.setText(_translate("MainWindow", "socks4.log"))
        self.btnLog.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Hexdump width:"))
        self.txtSetHexLen.setText(_translate("MainWindow", "16"))
        self.label_4.setText(_translate("MainWindow", "Data length:"))
        self.txtSetDataLen.setText(_translate("MainWindow", "1024"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetting), _translate("MainWindow", "Setting"))


