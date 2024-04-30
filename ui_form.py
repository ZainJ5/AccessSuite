# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QStackedWidget, QTextEdit, QWidget)
import rc_ALLIMAGES
import rc_Resources

class Ui_Hackathon(object):
    def setupUi(self, Hackathon):
        if not Hackathon.objectName():
            Hackathon.setObjectName(u"Hackathon")
        Hackathon.resize(754, 461)
        Hackathon.setStyleSheet(u"background-color: #ffffff;\n"
"\n"
"")
        self.label = QLabel(Hackathon)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 146, 463))
        self.label.setStyleSheet(u"background-color: #0A5F59;\n"
"border-radius:20px;\n"
"")
        self.stackedWidget = QStackedWidget(Hackathon)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(145, 0, 621, 461))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(233, 246, 240);\n"
"border-radius: 20px;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.Photo = QLabel(self.page)
        self.Photo.setObjectName(u"Photo")
        self.Photo.setGeometry(QRect(71, 70, 461, 221))
        self.Photo.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"border-radius: 20px; \n"
"")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 298, 111, 31))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QLabel, QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0A5F59, stop:1 #3EB489);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    padding: 4px 4px;\n"
"    font-weight: 500;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QLabel:hover, QPushButton:hover {\n"
"    background-color: #6BC75C;\n"
"\n"
"}\n"
"")
        self.generate = QPushButton(self.page)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(260, 423, 111, 31))
        self.generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.generate.setStyleSheet(u"QLabel, QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0A5F59, stop:1 #3EB489);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    padding: 4px 4px;\n"
"    font-weight: 500;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QLabel:hover, QPushButton:hover {\n"
"    background-color: #6BC75C;\n"
"\n"
"}\n"
"")
        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 581, 51))
        self.label_12.setStyleSheet(u"QStackWidget,QLabel{\n"
"background-color: white;\n"
"border-radius: 19px;\n"
"font-weight: bold;\n"
"font-family: \"Roboto\";\n"
"color: black;\n"
"font-size: 18px;\n"
"padding-left: 165px;\n"
"}")
        self.description = QTextEdit(self.page)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(50, 334, 501, 81))
        self.description.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"border-radius: 20px;\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"font-family: \"Poppins\";\n"
"color: black;\n"
"padding-left: 10px;\n"
"padding-top: 8px;")
        self.error = QLabel(self.page)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(437, 294, 91, 20))
        self.speaker = QPushButton(self.page)
        self.speaker.setObjectName(u"speaker")
        self.speaker.setGeometry(QRect(510, 382, 30, 30))
        self.speaker.setCursor(QCursor(Qt.PointingHandCursor))
        self.speaker.setStyleSheet(u"border-radius: 5px;\n"
"background-image: url(:/Images/Speaker.png);\n"
"background-color: rgb(220, 220, 220);\n"
"")
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.Textinput = QTextEdit(self.page_4)
        self.Textinput.setObjectName(u"Textinput")
        self.Textinput.setGeometry(QRect(16, 80, 571, 231))
        self.Textinput.setStyleSheet(u"QTextEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    font-family: \"Roboto\";\n"
"    color: black;\n"
"    font-size: 18px;\n"
"    padding-left: 8px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"")
        self.generatespeech = QPushButton(self.page_4)
        self.generatespeech.setObjectName(u"generatespeech")
        self.generatespeech.setGeometry(QRect(230, 344, 151, 41))
        self.generatespeech.setCursor(QCursor(Qt.PointingHandCursor))
        self.generatespeech.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(41, 128, 185);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    padding: 8px 8px;\n"
"    font-weight: 500;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 84, 163);\n"
"}\n"
"")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 581, 51))
        self.label_4.setStyleSheet(u"QStackWidget,QLabel{\n"
"background-color: white;\n"
"border-radius: 19px;\n"
"font-weight: bold;\n"
"font-family: \"Roboto\";\n"
"color: black;\n"
"font-size: 18px;\n"
"padding-left: 165px;\n"
"}")
        self.noaudio = QLabel(self.page_4)
        self.noaudio.setObjectName(u"noaudio")
        self.noaudio.setGeometry(QRect(450, 320, 131, 21))
        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.Result = QTextEdit(self.page_3)
        self.Result.setObjectName(u"Result")
        self.Result.setGeometry(QRect(20, 100, 571, 231))
        self.Result.setStyleSheet(u"QTextEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    font-family: \"Roboto\";\n"
"    color: black;\n"
"    font-size: 18px;\n"
"    padding-left: 8px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"")
        self.Result.setReadOnly(True)
        self.mic = QLabel(self.page_3)
        self.mic.setObjectName(u"mic")
        self.mic.setGeometry(QRect(220, 377, 20, 20))
        self.mic.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.GenerateText = QPushButton(self.page_3)
        self.GenerateText.setObjectName(u"GenerateText")
        self.GenerateText.setGeometry(QRect(20, 360, 571, 51))
        self.GenerateText.setCursor(QCursor(Qt.PointingHandCursor))
        self.GenerateText.setStyleSheet(u"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    font-family: \"Roboto\";\n"
"    color: black;\n"
"    font-size: 15px;\n"
"    padding-left: 80px;\n"
"    padding-top: 2px;")
        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 10, 581, 51))
        self.label_11.setStyleSheet(u"QStackWidget,QLabel{\n"
"background-color: white;\n"
"border-radius: 19px;\n"
"font-weight: bold;\n"
"font-family: \"Roboto\";\n"
"color: black;\n"
"font-size: 18px;\n"
"padding-left: 170px;\n"
"}")
        self.stackedWidget.addWidget(self.page_3)
        self.Result.raise_()
        self.GenerateText.raise_()
        self.mic.raise_()
        self.label_11.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 581, 51))
        self.label_3.setStyleSheet(u"QStackWidget,QLabel{\n"
"background-color: white;\n"
"border-radius: 19px;\n"
"font-weight: bold;\n"
"font-family: \"Roboto\";\n"
"color: black;\n"
"font-size: 18px;\n"
"padding-left: 235px;\n"
"}")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(55, 77, 176, 209))
        self.label_5.setStyleSheet(u"QStackWidget,QLabel{\n"
"background-color: white;\n"
"border-radius: 19px;\n"
"font-weight: light;\n"
"font-family: \"Poppins\";\n"
"color: black;\n"
"font-size: 15px;\n"
"padding-left: 10px;\n"
"}")
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(342, 350, 241, 41))
        self.label_6.setStyleSheet(u"QStackWidget,QLabel{\n"
"background-color: white;\n"
"font-size: 12px;\n"
"font-family: \"Poppins\";\n"
"color: black;\n"
"font-weight: semi-bold;\n"
"padding-up: 2px;\n"
"padding-left: 8px;\n"
"padding-right: 8px;\n"
"border-radius: 19px;\n"
"}")
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 410, 510, 39))
        self.label_7.setStyleSheet(u"QStackWidget,QLabel{\n"
"background-color: white;\n"
"border-radius: 19px;\n"
"font-weight: light;\n"
"font-family: \"Poppins\";\n"
"color: black;\n"
"font-size: 15px;\n"
"padding-left: 10px;\n"
"}")
        self.clock = QLabel(self.page_2)
        self.clock.setObjectName(u"clock")
        self.clock.setGeometry(QRect(549, 25, 23, 23))
        self.clock.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.profile = QLabel(self.page_2)
        self.profile.setObjectName(u"profile")
        self.profile.setGeometry(QRect(30, 275, 28, 27))
        self.profile.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(63, 89, 161, 131))
        self.label_9.setStyleSheet(u"QStackWidget,QLabel{\n"
"background-color: white;\n"
"font-size: 11px;\n"
"font-family: \"Poppins\";\n"
"color: black;\n"
"padding-up: 2px;\n"
"}")
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(63, 88, 166, 20))
        self.label_10.setStyleSheet(u"QStackWidget,QLabel{\n"
"background-color: white;\n"
"font-weight: bold;\n"
"font-size: 11px;\n"
"font-family: \"Poppins\";\n"
"color: black;\n"
"padding-up: 2px;\n"
"}")
        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 200, 150, 31))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QLabel, QPushButton {\n"
"    background-color: rgb(134, 249, 115);\n"
"    font-weight: bold;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 12px;\n"
"    border-radius :15px;\n"
"}\n"
"\n"
"QLabel:hover, QPushButton:hover {\n"
"    background-color: #6BC75C;\n"
"\n"
"}\n"
"")
        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 240, 151, 31))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QLabel, QPushButton {\n"
"	background-color: rgb(134, 249, 115);\n"
"    font-weight: bold;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 11px;\n"
"    border-radius :15px;\n"
"}\n"
"\n"
"QLabel:hover, QPushButton:hover {\n"
"    background-color: #6BC75C;\n"
"\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 581, 51))
        self.label_8.setStyleSheet(u"QStackWidget,QLabel{\n"
"background-color: white;\n"
"border-radius: 19px;\n"
"font-weight: bold;\n"
"font-family: \"Roboto\";\n"
"color: black;\n"
"font-size: 18px;\n"
"padding-left: 230px;\n"
"}")
        self.languagephoto = QLabel(self.page_5)
        self.languagephoto.setObjectName(u"languagephoto")
        self.languagephoto.setGeometry(QRect(110, 76, 382, 376))
        self.languagephoto.setStyleSheet(u"border-radius: 0px;")
        self.languagephoto_2 = QLabel(self.page_5)
        self.languagephoto_2.setObjectName(u"languagephoto_2")
        self.languagephoto_2.setGeometry(QRect(100, 71, 402, 388))
        self.languagephoto_2.setStyleSheet(u"border: 2px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_5)
        self.label_8.raise_()
        self.languagephoto_2.raise_()
        self.languagephoto.raise_()
        self.text = QPushButton(Hackathon)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(0, 110, 145, 41))
        self.text.setCursor(QCursor(Qt.PointingHandCursor))
        self.text.setStyleSheet(u"QPushButton {\n"
"    border-radius: 19px;\n"
"    background-color: #084C45;\n"
"    color: white;\n"
"    font: bold 14px;\n"
"padding-left: 7px;\n"
"padding-right: 10px;\n"
"  padding-up: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #063D37;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    color: black;\n"
"    background-color: rgb(233, 246, 240);\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.text.setCheckable(True)
        self.text.setChecked(False)
        self.text.setAutoExclusive(True)
        self.speech = QPushButton(Hackathon)
        self.speech.setObjectName(u"speech")
        self.speech.setGeometry(QRect(0, 40, 145, 41))
        self.speech.setCursor(QCursor(Qt.PointingHandCursor))
        self.speech.setStyleSheet(u"QPushButton {\n"
"    border-radius: 19px;\n"
"    background-color: #084C45;\n"
"    color: white;\n"
"    font: bold 14px;\n"
"padding-left: 7px;\n"
"padding-right: 10px;\n"
"  padding-up: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #063D37;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    color: black;\n"
"    background-color: rgb(233, 246, 240);\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/new/prefix1/Images/Chatbot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.speech.setIcon(icon)
        self.speech.setCheckable(True)
        self.speech.setChecked(True)
        self.speech.setAutoExclusive(True)
        self.imageana = QPushButton(Hackathon)
        self.imageana.setObjectName(u"imageana")
        self.imageana.setGeometry(QRect(0, 180, 145, 41))
        self.imageana.setCursor(QCursor(Qt.PointingHandCursor))
        self.imageana.setStyleSheet(u"QPushButton {\n"
"    border-radius: 19px;\n"
"    background-color: #084C45;\n"
"    color: white;\n"
"    font: bold 14px;\n"
"padding-left: 7px;\n"
"padding-right: 10px;\n"
"  padding-up: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #063D37;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    color: black;\n"
"    background-color: rgb(233, 246, 240);\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/new/prefix1/Images/Image Analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.imageana.setIcon(icon1)
        self.imageana.setCheckable(True)
        self.imageana.setAutoExclusive(True)
        self.chatbot = QPushButton(Hackathon)
        self.chatbot.setObjectName(u"chatbot")
        self.chatbot.setGeometry(QRect(0, 250, 145, 41))
        self.chatbot.setCursor(QCursor(Qt.PointingHandCursor))
        self.chatbot.setStyleSheet(u"QPushButton {\n"
"    border-radius: 19px;\n"
"    background-color: #084C45;\n"
"    color: white;\n"
"    font: bold 14px;\n"
"padding-left: 7px;\n"
"padding-right: 50px;\n"
"  padding-up: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #063D37;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    color: black;\n"
"    background-color: rgb(233, 246, 240);\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.chatbot.setCheckable(True)
        self.chatbot.setAutoExclusive(True)
        self.signlanguage = QPushButton(Hackathon)
        self.signlanguage.setObjectName(u"signlanguage")
        self.signlanguage.setGeometry(QRect(0, 320, 145, 41))
        self.signlanguage.setCursor(QCursor(Qt.PointingHandCursor))
        self.signlanguage.setStyleSheet(u"QPushButton {\n"
"    border-radius: 19px;\n"
"    background-color: #084C45;\n"
"    color: white;\n"
"    font: bold 14px;\n"
"padding-left: 7px;\n"
"padding-right: 10px;\n"
"  padding-up: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #063D37;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    color: black;\n"
"    background-color: rgb(233, 246, 240);\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.signlanguage.setCheckable(True)
        self.signlanguage.setAutoExclusive(True)

        self.retranslateUi(Hackathon)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Hackathon)
    # setupUi

    def retranslateUi(self, Hackathon):
        Hackathon.setWindowTitle(QCoreApplication.translate("Hackathon", u"Hackathon", None))
        self.label.setText("")
        self.Photo.setText("")
        self.pushButton.setText(QCoreApplication.translate("Hackathon", u"Upload", None))
        self.generate.setText(QCoreApplication.translate("Hackathon", u"Generate", None))
        self.label_12.setText(QCoreApplication.translate("Hackathon", u"IMAGE TO TEXT CONVERTER", None))
        self.description.setHtml(QCoreApplication.translate("Hackathon", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Poppins'; font-size:12px; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.error.setText("")
        self.speaker.setText("")
        self.Textinput.setPlaceholderText(QCoreApplication.translate("Hackathon", u" write text to start converting...", None))
        self.generatespeech.setText(QCoreApplication.translate("Hackathon", u"Generate", None))
        self.label_4.setText(QCoreApplication.translate("Hackathon", u"TEXT  TO SPEECH TEXT CONVERTER", None))
        self.noaudio.setText("")
        self.Result.setPlaceholderText(QCoreApplication.translate("Hackathon", u"Text will be generated here...", None))
        self.mic.setText("")
        self.GenerateText.setText(QCoreApplication.translate("Hackathon", u"TAP TO START RECORDING...", None))
        self.label_11.setText(QCoreApplication.translate("Hackathon", u" SPEECH TO TEXT CONVERTER", None))
        self.label_3.setText(QCoreApplication.translate("Hackathon", u"AI Assisistant", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("Hackathon", u"I feel stressed for a last couple of days.", None))
        self.label_7.setText(QCoreApplication.translate("Hackathon", u"Write a comment...", None))
        self.clock.setText("")
        self.profile.setText("")
        self.label_9.setText(QCoreApplication.translate("Hackathon", u"Don\u2019t hesitate to let me know\n"
"about emotions, thoughts, or\n"
"any obstacles your dealing \n"
"with right now.Write a message\n"
"or choose one of the topics \n"
"below to get started.\n"
"", None))
        self.label_10.setText(QCoreApplication.translate("Hackathon", u"Hi! How can i help you today?", None))
        self.pushButton_2.setText(QCoreApplication.translate("Hackathon", u"Manage Anxiety", None))
        self.pushButton_3.setText(QCoreApplication.translate("Hackathon", u"Stop negative self-talk", None))
        self.label_8.setText(QCoreApplication.translate("Hackathon", u"Sign Language", None))
        self.languagephoto.setText("")
        self.languagephoto_2.setText("")
        self.text.setText(QCoreApplication.translate("Hackathon", u"Text to Speech", None))
        self.speech.setText(QCoreApplication.translate("Hackathon", u"Speech to Text", None))
        self.imageana.setText(QCoreApplication.translate("Hackathon", u"Image Analysis", None))
        self.chatbot.setText(QCoreApplication.translate("Hackathon", u"Chatbot", None))
        self.signlanguage.setText(QCoreApplication.translate("Hackathon", u"Sign Language", None))
    # retranslateUi

