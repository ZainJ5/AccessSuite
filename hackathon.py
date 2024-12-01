import sys
import os
import io
from PySide6.QtCore import Qt
from ui_form import Ui_Hackathon
from PySide6.QtGui import QPixmap,QIcon
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QButtonGroup
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import azure.cognitiveservices.speech as speechsdk
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices import vision
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

class Hackathon(QWidget):
    def __init__(self, parent=None):
        self.file_name = ""
        super().__init__(parent)
        self.ui = Ui_Hackathon()
        self.ui.setupUi(self)
        icon=("")

        self.description = ""
        self.setWindowIcon(QIcon(icon));
        self.setWindowTitle("AccessSuite")
        self.setFixedSize(754, 461)
        flags = self.windowFlags()
        flags |= Qt.WindowMinimizeButtonHint
        self.setWindowFlags(flags)
        self.ui.pushButton.clicked.connect(self.openFileDialog)
        self.ui.generate.clicked.connect(self.image_analysis)
        self.ui.speaker.clicked.connect(self.ImageSpeakerClicked)

        self.ui.text.clicked.connect(self.TextClicked)
        self.ui.speech.clicked.connect(self.SpeechClicked)
        self.ui.imageana.clicked.connect(self.VisionClicked)
        self.ui.chatbot.clicked.connect(self.ChatBotClicked)

        self.ui.generatespeech.clicked.connect(self.GenerateAudio)
        self.ui.GenerateText.clicked.connect(self.Generatetext)
        self.ui.signlanguage.clicked.connect(self.signLanguage)

        self.ui.stackedWidget.setCurrentIndex(2)

        self.ui.GenerateText.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border-radius: 20px; "
                                            "font-family: 'Roboto';"
                                            "color: black; "
                                            "font-size: 15px;"
                                            "padding-left: 80px;"
                                            "padding-top: 2px;")

        self.ui.GenerateText.setText("TAP TO START RECORDING...")

        group1 = QButtonGroup(self)
        group1.addButton(self.ui.text)
        group1.addButton(self.ui.chatbot)
        group1.addButton(self.ui.speech)
        group1.addButton(self.ui.imageana)
        group1.addButton(self.ui.signlanguage)

        self.ui.Textinput.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)


        icon = QIcon(":/new/prefix1/Images/Speech to text.png")
        self.ui.speech.setIcon(icon)
        self.ui.speech.setIconSize(QSize(30, 30))

        icon1 = QIcon(":/new/prefix1/Images/Text to speech.png")
        self.ui.text.setIcon(icon1)
        self.ui.text.setIconSize(QSize(30, 30))

        icon2 = QIcon(":/new/prefix1/Images/Image Analysis.png")
        self.ui.imageana.setIcon(icon2)
        self.ui.imageana.setIconSize(QSize(26, 26))

        icon3 = QIcon(":/new/prefix1/Images/Chatbot.png")
        self.ui.chatbot.setIcon(icon3)
        self.ui.chatbot.setIconSize(QSize(30, 30))

        icon4 = QIcon(":/new/prefix1/Images/Vector.png")
        self.ui.pushButton.setIcon(icon4)
        self.ui.pushButton.setIconSize(QSize(20, 20))

        icon5 = QIcon(":/new/prefix1/Images/SignLogo.png")
        self.ui.signlanguage.setIcon(icon5)
        self.ui.signlanguage.setIconSize(QSize(30, 30))

        photo = QPixmap(":/new/prefix1/Images/mic.png")
        h = self.ui.mic.height()
        w = self.ui.mic.width()
        self.ui.mic.setPixmap(photo.scaled(w, h))

        photo1 = QPixmap(":/new/prefix1/Images/Clock.png")
        h1 = self.ui.clock.height()
        w1 = self.ui.clock.width()
        self.ui.clock.setPixmap(photo1.scaled(w1, h1))

        photo2 = QPixmap(":/new/prefix1/Images/Profile.png")
        h2 = self.ui.profile.height()
        w2 = self.ui.profile.width()
        self.ui.profile.setPixmap(photo2.scaled(w2, h2))

        photo3 = QPixmap(":/new/prefix1/Images/Signlanguage.jpg")
        h3 = self.ui.languagephoto.height()
        w3 = self.ui.languagephoto.width()
        self.ui.languagephoto.setPixmap(photo3.scaled(w3, h3))


    def signLanguage(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def TextClicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)


    def SpeechClicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.GenerateText.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border-radius: 20px; "
                                            "font-family: 'Roboto';"
                                            "color: black; "
                                            "font-size: 15px;"
                                            "padding-left: 80px;"
                                            "padding-top: 2px;")

        self.ui.GenerateText.setText("TAP TO START RECORDING...")
        self.ui.Result.setText("")


    def ChatBotClicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def VisionClicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def ImageSpeakerClicked(self):
        imagetext = self.description
        if imagetext != "Description : " and imagetext != "":
            self.text_to_speech(imagetext)


    def GenerateAudio(self):
        EnteredText = self.ui.Textinput.toPlainText()
        if EnteredText:
           self.text_to_speech(EnteredText)
           self.ui.noaudio.setText("")
           self.ui.Textinput.setText("")

        else:
           self.ui.noaudio.setText("No Text Detected")
           self.ui.noaudio.setStyleSheet("QLabel { color: Red; }")

    def Generatetext(self):
        self.ui.GenerateText.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border-radius: 20px; "
                                            "font-family: 'Roboto';"
                                            "color: black; "
                                            "font-size: 15px;"
                                            "padding-left: -50px;"
                                            "padding-top: 2px;")

        self.ui.GenerateText.setText("Listening...")
        result = self.recognize_from_microphone()
        self.ui.Result.setText(result)


    def text_to_speech(self, text):
        speech_key = "API_KEY"
        speech_region = "westus"

        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

        # The neural multilingual voice can speak different languages based on the input text.
        speech_config.speech_synthesis_voice_name = 'en-US-AvaMultilingualNeural'

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                return speech_synthesis_result.audio_data

    def openFileDialog(self):
        self.description = ""
        options = QFileDialog.Options()
        self.file_name , _= QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp *.jpeg)", options=options)
        if self.file_name:
            img = QPixmap(self.file_name)
            self.ui.Photo.setPixmap(img)
            self.ui.Photo.setScaledContents(True)
            self.ui.error.setText("")
            self.ui.description.setText("")



    def image_analysis(self):

        if self.file_name:
            image_path = self.file_name
            subscription_key = 'API_KEY'
            endpoint = 'END_POINT'

            credentials = CognitiveServicesCredentials(subscription_key)
            client = ComputerVisionClient(endpoint, credentials)

            with open(image_path, "rb") as image_file:
                image_data = image_file.read()

            image_stream = io.BytesIO(image_data)
            features = [VisualFeatureTypes.description]
            image_analysis = client.describe_image_in_stream(image_stream)

            if image_analysis.captions:
                answer = image_analysis.captions[0].text
            else:
                answer = "No description found."

            self.description = "Description : " + answer
            self.ui.description.setText(self.description)
        else:
            self.ui.error.setText("Invalid File Path")
            self.ui.error.setStyleSheet("QLabel { color: Red; }")

    def recognize_from_microphone(self):
        self.ui.GenerateText.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border-radius: 20px; "
                                            "font-family: 'Roboto';"
                                            "color: black; "
                                            "font-size: 15px;"
                                            "padding-left: -50px;"
                                            "padding-top: 2px;")

        self.ui.GenerateText.setText("Listening...")

        speech_key = '9740c0f7b333475da7bc2faa182a563c'
        service_region = 'eastus'

        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        speech_config.speech_recognition_language = "en-US"

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        self.ui.GenerateText.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border-radius: 20px; "
                                            "font-family: 'Roboto';"
                                            "color: black; "
                                            "font-size: 15px;"
                                            "padding-left: -20px;"
                                            "padding-top: 2px;")
        self.ui.GenerateText.setText("Listening ended.")

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return speech_recognition_result.text
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            return "No speech could be recognized: {}".format(speech_recognition_result.no_match_details)
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_recognition_result.cancellation_details
                reason = cancellation_details.reason
                error_details = cancellation_details.error_details
                error_message = "Speech recognition canceled. Reason: {}".format(reason)
                if reason == speechsdk.CancellationReason.Error:
                    error_message += ". Error details: {}".format(error_details)
                return error_message



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Hackathon()
    widget.show()
    sys.exit(app.exec())




