# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NoDone.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
from icon import Uisetup
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u":/icon/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setMenuRole(QAction.TextHeuristicRole)
        self.actionFeedback = QAction(MainWindow)
        self.actionFeedback.setObjectName(u"actionFeedback")
        self.actioncheckupdate = QAction(MainWindow)
        self.actioncheckupdate.setObjectName(u"actioncheckupdate")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionEnglish_UK = QAction(MainWindow)
        self.actionEnglish_UK.setObjectName(u"actionEnglish_UK")
        self.actionzh_hans_cn = QAction(MainWindow)
        self.actionzh_hans_cn.setObjectName(u"actionzh_hans_cn")
        self.actionzh_hant_cn = QAction(MainWindow)
        self.actionzh_hant_cn.setObjectName(u"actionzh_hant_cn")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 120, 541))
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setDisabled(True)
        self.pushButton.setGeometry(QRect(20, 20, 75, 24))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(130, 10, 661, 541))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 81, 20))
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(116, 20, 91, 22))
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 50, 241, 111))
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 54, 16))
        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 20, 113, 20))
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 50, 101, 16))
        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 50, 113, 20))
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 80, 54, 16))
        self.comboBox_2 = QComboBox(self.groupBox_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(110, 80, 111, 22))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 180, 171, 16))
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 180, 75, 24))
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(450, 490, 91, 24))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 210, 54, 16))
        self.comboBox_4 = QComboBox(self.groupBox_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(90, 210, 91, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setToolTipsVisible(False)
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuLanguage = QMenu(self.menuEdit)
        self.menuLanguage.setObjectName(u"menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionFeedback)
        self.menuHelp.addAction(self.actioncheckupdate)
        self.menuEdit.addAction(self.menuLanguage.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionQuit)
        self.menuLanguage.addAction(self.actionEnglish_UK)
        self.menuLanguage.addAction(self.actionzh_hans_cn)
        self.menuLanguage.addAction(self.actionzh_hant_cn)

        self.retranslateUi(MainWindow)
        self.actionAbout.triggered.connect(self.ShowAbout)
        self.actionFeedback.triggered.connect(self.OpenFeedback)
        self.actionEnglish_UK.triggered.connect(self.translate_to_en_UK)
        self.actionzh_hans_cn.triggered.connect(self.translate_to_zh_hans)
        self.actionzh_hant_cn.triggered.connect(self.translate_to_zh_hant)
        self.actioncheckupdate.triggered.connect(self.checkupdate)
        self.pushButton_2.clicked.connect(self.chagefile)
        self.pushButton_3.clicked.connect(self.CreatPPT)
        self.actionQuit.triggered.connect(MainWindow.close)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Simple PPT", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", "About", None))
        self.actionFeedback.setText(QCoreApplication.translate("MainWindow", "Feedback", None))
        self.actioncheckupdate.setText(QCoreApplication.translate("MainWindow", "checkupdate", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", "Quit", None))
        self.actionEnglish_UK.setText("English(UK)")
        self.actionzh_hans_cn.setText("中文（简体）")
        self.actionzh_hant_cn.setText("中文（繁體）")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", "Function", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "Creat PPT", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", "Creat PPT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "format", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow",  "pptx", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", "title page", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "title text", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "subtitle text", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Style", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", "Title Slide", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", "Title and Content", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", "Section Header", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", "Two Content", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", "Comparison", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", "Title Only", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", "Blank", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", "Content with Caption", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", "Pictrue with Caption", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", "Title and vertical text", None))
        self.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", "Vertical headings and text", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", "text(.docx file or markdown)", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", "Change file", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", "Creat", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "text style", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", "Title Slide", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", "Title and Content", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", "Section Header", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", "Two Content", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", "Comparison", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", "Title Only", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", "Blank", None))
        self.comboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", "Content with Caption", None))
        self.comboBox_4.setItemText(8, QCoreApplication.translate("MainWindow", "Pictrue with Caption", None))
        self.comboBox_4.setItemText(9, QCoreApplication.translate("MainWindow", "Title and vertical text", None))
        self.comboBox_4.setItemText(10, QCoreApplication.translate("MainWindow", "Vertical headings and text", None))

        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", "Edit", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", "Language", None))
    # retranslateUi

