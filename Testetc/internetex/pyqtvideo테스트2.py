import sys

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import QDir, Qt, QUrl, pyqtSlot

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)

dir_audience=''
dir_movie = ''
dir_export = ''
select_emotion = 'happy'

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("highlight_export_form.ui", self)
        self.ui.show()

        self.ui.load_audience.clicked.connect(self.load_audience_clicked)
        self.ui.load_movie.clicked.connect(self.load_movie_clicked)

        self.ui.start_recog.clicked.connect(self.start_recog_clicked)

        self.ui.radio_happy.toggled.connect(self.on_radio_button_toggled)
        self.ui.radio_surprised.toggled.connect(self.on_radio_button_toggled)

    def load_audience_clicked(self, event):
        dir_audience, _ = QFileDialog.getOpenFileName(self, "Open Audience", QDir.homePath())
        self.path_audience.setText(dir_audience)

    def load_movie_clicked(self, event):
        dir_movie, _ = QFileDialog.getOpenFileName(self, "Open Movie", QDir.homePath())
        self.path_movie.setText(dir_movie)

    def start_recog_clicked(self, event):
        self.check_1.setText("start_recognition")

    def on_radio_button_toggled(self):
        if self.radio_happy.isChecked():
            select_emotion='happy'
            self.check_3.setText(select_emotion)

        elif self.radio_surprised.isChecked():
            select_emotion='surprised'
            self.check_3.setText(select_emotion)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())