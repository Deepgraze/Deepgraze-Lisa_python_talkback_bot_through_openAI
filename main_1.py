import pyttsx3
from config import apikey
import speech_recognition as sr
import datetime
import webbrowser
import os
import openai
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for PRompt :{prompt}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "assistant",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    TextToVoice("This is your result sir")
    print(response["choices"][0]["message"]["content"])
    text += response["choices"][0]["message"]["content"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai\prompt- {' '.join(prompt.split('chat')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def ai_1(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for PRompt :{prompt}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "assistant",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    x = (response["choices"][0]["message"]["content"])
    print(f"Lisa : {x}")
    TextToVoice(x)
    text += response["choices"][0]["message"]["content"]
    if not os.path.exists("Baate"):
        os.mkdir("Baate")
    with open(f"Baate\prompt- {' '.join(prompt.split('chat')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def TextToVoice(command):
    eng = pyttsx3.init()
    voices = eng.getProperty('voices')
    eng.setProperty('voice', voices[1].id)
    rate = eng.getProperty('rate')
    eng.setProperty('rate', rate * 0.6)
    eng.say(command)
    eng.runAndWait()

class GifApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('GIF Player')
        self.setGeometry(100, 100, 400, 400)

        self.movie = QMovie("../../OneDrive/Documents/docx/AI visualization design.gif")
        self.label = QLabel(self)
        self.label.setMovie(self.movie)
        self.movie.start()


        start_button = QPushButton(QIcon("../../OneDrive/Documents/docx/Premium PSD _ 3d play button dark theme.jpg"), "", self)
        start_button.clicked.connect(self.start_animation)
        start_button.setGeometry(62, 217, 61, 51)
        start_button.setIconSize(QSize(50, 50))

        close_button = QPushButton(QIcon("../../OneDrive/Documents/docx/Premium PSD _ 3d pause button dark theme.jpg"), "", self)
        close_button.clicked.connect(self.close_application)
        start_button.setGeometry(342, 217, 61, 51)
        close_button.setIconSize(QSize(50, 50))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(start_button)
        vbox.addWidget(close_button)

        self.setLayout(vbox)
    def Start(self):
        while True:

            self.MyText = self.TakeCommand().lower()

            web_sites = [["youtube", "https://www.youtube.com/"], ["amazon", "https://www.amazon.com/"],
                         ["google", "https://www.google.com/"], ["flipkart", "https://www.flipkart.com/"]]
            for site in web_sites:
                if f"open {site[0]}" in self.MyText:
                    webbrowser.open(site[1])
                    TextToVoice(f"openinig {site[0]} sir .. ..")

            if "the time" in self.MyText:
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                sec = datetime.datetime.now().strftime("%S")
                TextToVoice(f"Sir the time is {hour} hours {min} minutes and {sec} seconds")
            # todo: check for open an app
            if "using chat" in self.MyText:
                TextToVoice("wait")
                ai(prompt=self.MyText)
            if "open" in self.MyText:
                print("")
            else:
                ai_1(prompt=self.MyText)

    def TakeCommand(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening...")
            # r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            MyText = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.MyText}")

        except Exception as e:
            print(e)
            TextToVoice("Unable to Recognize your voice Sir..")
            return "None"
        return self.MyText

    def TextToVoice_1(self):
        self.eng = pyttsx3.init()
        voices = self.eng.getProperty('voices')
        self.eng.setProperty('voice', voices[1].id)
        rate = self.eng.getProperty('rate')
        self.eng.setProperty('rate', rate * 0.8)
        self.eng.say("Hello I'm Lisa how can I help you")
        self.eng.runAndWait()
    def start_animation(self):
        self.movie.start()
        while True:
            self.TextToVoice_1()
            self.Start()


    def close_application(self):
        self.movie.stop()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GifApp()
    ex.show()
    sys.exit(app.exec_())