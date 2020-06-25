from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import scraper

weather = scraper.Weather("https://www.knmi.nl/nederland-nu/weer/verwachtingen")
racing = scraper.Racing("https://racingnews365.nl/")
gaming = scraper.Gaming("https://www.pcgamer.com/news/")
news = scraper.News("https://nos.nl")  

class Ui_Win(object):
    def setupUi(self, Win):
        #Init main window
        Win.setObjectName("Win")
        Win.resize(800, 600)
        Win.setStyleSheet("""color: rgb(255, 255, 255);\n
                            background-color: rgb(0, 0, 0);\n
                            font: 12pt \"Verdana\";""")

        self.centralwidget = QtWidgets.QWidget(Win)
        self.centralwidget.setObjectName("centralwidget")

        #Init main grid
        self.grid_layout_win = QtWidgets.QGridLayout(self.centralwidget)
        self.grid_layout_win.setObjectName("grid_layout_win")

        #Init gaming groupbox 
        self.gaming_box = QtWidgets.QGroupBox(self.centralwidget)
        self.gaming_box.setObjectName("gaming_box")

        #Init gaming grid
        self.grid_gaming = QtWidgets.QGridLayout(self.gaming_box)
        self.grid_gaming.setObjectName("grid_gaming")

        #Init gaming scroll area
        self.scroll_area_gaming = QtWidgets.QScrollArea(self.gaming_box)
        self.scroll_area_gaming.setMaximumSize(QtCore.QSize(368, 226))
        self.scroll_area_gaming.setWidgetResizable(True)
        self.scroll_area_gaming.setObjectName("scroll_area_gaming")
        self.scroll_area_gaming_contents = QtWidgets.QWidget()
        self.scroll_area_gaming_contents.setGeometry(QtCore.QRect(0, 0, 366, 224))
        self.scroll_area_gaming_contents.setObjectName("scroll_area_gaming_contents")
        self.grid_scroll_gaming = QtWidgets.QGridLayout(self.scroll_area_gaming_contents)
        self.grid_scroll_gaming.setObjectName("grid_scroll_gaming")
        self.scroll_area_gaming.setWidget(self.scroll_area_gaming_contents)

        #Init gaming label
        self.gaming_label = QtWidgets.QLabel(self.scroll_area_gaming_contents)
        self.gaming_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gaming_label.setWordWrap(True)
        self.gaming_label.setObjectName("gaming_label")

        #Add gaming stuff to the main grid
        self.grid_gaming.addWidget(self.scroll_area_gaming, 0, 0, 1, 1)
        self.grid_scroll_gaming.addWidget(self.gaming_label, 0, 0, 1, 1)
        self.grid_layout_win.addWidget(self.gaming_box, 0, 1, 1, 1)

        #Init racing group box
        self.racing_box = QtWidgets.QGroupBox(self.centralwidget)
        self.racing_box.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.racing_box.setObjectName("racing_box")

        #Init racing grid
        self.grid_racing = QtWidgets.QGridLayout(self.racing_box)
        self.grid_racing.setObjectName("grid_racing")

        #Init racing scroll area
        self.scroll_area_racing = QtWidgets.QScrollArea(self.racing_box)
        self.scroll_area_racing.setMaximumSize(QtCore.QSize(386, 226))
        self.scroll_area_racing.setWidgetResizable(True)
        self.scroll_area_racing.setObjectName("scroll_area_racing")
        self.scroll_area_racing_contents = QtWidgets.QWidget()
        self.scroll_area_racing_contents.setGeometry(QtCore.QRect(0, 0, 366, 224))
        self.scroll_area_racing_contents.setObjectName("scroll_area_racing_contents")
        self.scroll_grid_racing = QtWidgets.QGridLayout(self.scroll_area_racing_contents)
        self.scroll_grid_racing.setObjectName("scroll_grid_racing")

        #Init racing label
        self.racing_label = QtWidgets.QLabel(self.scroll_area_racing_contents)
        self.racing_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.racing_label.setWordWrap(True)
        self.racing_label.setObjectName("racing_label")

        #Add racing stuff to the main grid
        self.scroll_grid_racing.addWidget(self.racing_label, 0, 0, 1, 1)
        self.scroll_area_racing.setWidget(self.scroll_area_racing_contents)
        self.grid_racing.addWidget(self.scroll_area_racing, 0, 0, 1, 1)
        self.grid_layout_win.addWidget(self.racing_box, 1, 1, 1, 1)

        #Init weather groupbox
        self.weather_box = QtWidgets.QGroupBox(self.centralwidget)
        self.weather_box.setObjectName("weather_box")

        #Init weather grid
        self.grid_weather = QtWidgets.QGridLayout(self.weather_box)
        self.grid_weather.setObjectName("gridLayout_4")

        #Init weather scroll area
        self.scroll_area_weather = QtWidgets.QScrollArea(self.weather_box)
        self.scroll_area_weather.setMaximumSize(QtCore.QSize(386, 226))
        self.scroll_area_weather.setWidgetResizable(True)
        self.scroll_area_weather.setObjectName("scroll_area_weather")
        self.scroll_area_weather_contents = QtWidgets.QWidget()
        self.scroll_area_weather_contents.setGeometry(QtCore.QRect(0, 0, 366, 224))
        self.scroll_area_weather_contents.setObjectName("scroll_area_weather_contents")
        self.scroll_grid_weather = QtWidgets.QGridLayout(self.scroll_area_weather_contents)
        self.scroll_grid_weather.setObjectName("scroll_grid_weather")

        #Init weather label
        self.weather_label = QtWidgets.QLabel(self.scroll_area_weather_contents)
        self.weather_label.setMaximumSize(QtCore.QSize(16777215, 490238))
        self.weather_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.weather_label.setWordWrap(True)
        self.weather_label.setObjectName("weather_label")

        #Add weather stuff to grid
        self.scroll_grid_weather.addWidget(self.weather_label, 0, 0, 1, 1)
        self.scroll_area_weather.setWidget(self.scroll_area_weather_contents)
        self.grid_weather.addWidget(self.scroll_area_weather, 0, 0, 1, 1)
        self.grid_layout_win.addWidget(self.weather_box, 1, 0, 1, 1)

        #Init news group box
        self.news_box = QtWidgets.QGroupBox(self.centralwidget)
        self.news_box.setMaximumSize(QtCore.QSize(4188, 324324))
        self.news_box.setObjectName("news_box")

        #Init news grid
        self.grid_news = QtWidgets.QGridLayout(self.news_box)
        self.grid_news.setObjectName("gridLayout_2")

        #Init scroll area
        self.scroll_area_news = QtWidgets.QScrollArea(self.news_box)
        self.scroll_area_news.setMaximumSize(QtCore.QSize(368, 226))
        self.scroll_area_news.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area_news.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scroll_area_news.setWidgetResizable(True)
        self.scroll_area_news.setObjectName("scroll_area_news")
        self.scroll_area_news_contents = QtWidgets.QWidget()
        self.scroll_area_news_contents.setGeometry(QtCore.QRect(0, 0, 349, 252))
        self.scroll_area_news_contents.setObjectName("scroll_area_news_contents")
        self.scroll_grid_news = QtWidgets.QGridLayout(self.scroll_area_news_contents)
        self.scroll_grid_news.setObjectName("scroll_grid_news")

        #Init news label
        self.news_label = QtWidgets.QLabel(self.scroll_area_news_contents)
        self.news_label.setToolTipDuration(-1)
        self.news_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.news_label.setStyleSheet("gridline-color: rgb(85, 255, 127);\n"
"selection-color: rgb(85, 255, 255);\n"
"border-color: rgb(255, 170, 255);")
        self.news_label.setScaledContents(False)
        self.news_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.news_label.setWordWrap(True)
        self.news_label.setObjectName("news_label")

        #Add news stuff to main grid
        self.scroll_grid_news.addWidget(self.news_label, 0, 1, 1, 1)
        self.scroll_area_news.setWidget(self.scroll_area_news_contents)
        self.grid_news.addWidget(self.scroll_area_news, 0, 0, 1, 1)
        self.grid_layout_win.addWidget(self.news_box, 0, 0, 1, 1)

        Win.setCentralWidget(self.centralwidget)

        #Menubar
        self.menubar = QtWidgets.QMenuBar(Win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        Win.setMenuBar(self.menubar)

        #Statusbar
        self.statusbar = QtWidgets.QStatusBar(Win)
        self.statusbar.setObjectName("statusbar")
        Win.setStatusBar(self.statusbar)

        #Update button
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setObjectName("update_button")
        self.update_button.clicked.connect(self.update)
        self.update_button.setStyleSheet("""
                                        border-radius: 35px;        
                                        border-width: 1px;
                                        border-color: rgb(255, 170, 0);
                                        border-style: solid;
                                        """)
        self.grid_layout_win.addWidget(self.update_button, 2, 0, 1, 2)

        self.retranslateUi(Win)
        QtCore.QMetaObject.connectSlotsByName(Win)

    def retranslateUi(self, Win):
        self._translate = QtCore.QCoreApplication.translate

        #Set titles
        self.gaming_box.setTitle(self._translate("Win", "Gaming News"))
        self.racing_box.setTitle(self._translate("Win", "Racing News"))
        self.weather_box.setTitle(self._translate("Win", "Weather"))
        self.news_box.setTitle(self._translate("Win", "Nos News"))
        Win.setWindowTitle(self._translate("Win", "Dashboard"))

        #Set icon
        Win.setWindowIcon(QtGui.QIcon('e:/vscodeprojects/Dashboard/current-events-512.png'))

        #Set label text
        news_label_text_1 = "Article 1: \n" + news.article_1 + "\n" * 2 + "link: " + news.link_1 +"\n" * 2
        news_label_text_2 = "Article 2: \n" + news.article_2 + "\n" * 2 + "link: " + news.link_2
        news_label_text = news_label_text_1 + news_label_text_2
        self.news_label.setText(self._translate("MainWindow", news_label_text))

        racing_label_text_1 = "Article 1: \n" + racing.article_1 + "\n" * 2 + "link: " + racing.link_1 +"\n" * 2
        racing_label_text_2 = "Article 2: \n" + racing.article_2 + "\n" * 2 + "link: " + racing.link_2 +"\n" * 2
        racing_label_text_3 = "Article 3: \n" + racing.article_3 + "\n" * 2 + "link: " + racing.link_3
        racing_label_text = racing_label_text_1 + racing_label_text_2 + racing_label_text_3
        self.racing_label.setText(self._translate("MainWindow", racing_label_text))

        gaming_label_text_1 = "Article 1: \n" + gaming.article_1 + "\n" * 2 + "link: " + gaming.link_1 +"\n" * 2
        gaming_label_text_2 = "Article 2: \n" + gaming.article_2 + "\n" * 2 + "link: " + gaming.link_2 +"\n" * 2
        gaming_label_text_3 = "Article 3: \n" + gaming.article_3 + "\n" * 2 + "link: " + gaming.link_3

        gaming_label_text = gaming_label_text_1 + gaming_label_text_2 + gaming_label_text_3
        self.gaming_label.setText(self._translate("MainWindow", gaming_label_text))

        weather_label_text = weather.weather + "\nlink: https://www.knmi.nl/nederland-nu/weer/verwachtingen"
        self.weather_label.setText(self._translate("MainWindow", weather_label_text))

        self.update_button.setText(self._translate("Win", "Refresh"))

    def update(self):
        weather = scraper.Weather("https://www.knmi.nl/nederland-nu/weer/verwachtingen")
        racing = scraper.Racing("https://racingnews365.nl/")
        gaming = scraper.Gaming("https://www.pcgamer.com/news/")
        news = scraper.News("https://nos.nl")

        #Set label text
        news_label_text_1 = "Article 1: \n" + news.article_1 + "\n" * 2 + "link: " + news.link_1 +"\n" * 2
        news_label_text_2 = "Article 2: \n" + news.article_2 + "\n" * 2 + "link: " + news.link_2
        news_label_text = news_label_text_1 + news_label_text_2
        self.news_label.setText(self._translate("MainWindow", news_label_text))

        racing_label_text_1 = "Article 1: \n" + racing.article_1 + "\n" * 2 + 'link: <a href="' + racing.link_1 + '">Link</a>' + "\n" * 2
        racing_label_text_2 = "Article 2: \n" + racing.article_2 + "\n" * 2 + "link: " + racing.link_2 +"\n" * 2
        racing_label_text_3 = "Article 3: \n" + racing.article_3 + "\n" * 2 + "link: " + racing.link_3
        racing_label_text = racing_label_text_1 + racing_label_text_2 + racing_label_text_3
        self.racing_label.setText(self._translate("MainWindow", racing_label_text))
        self.racing_label.setOpenExternalLinks(True)

        gaming_label_text_1 = "Article 1: \n" + gaming.article_1 + "\n" * 2 + "link: " + gaming.link_1 +"\n" * 2
        gaming_label_text_2 = "Article 2: \n" + gaming.article_2 + "\n" * 2 + "link: " + gaming.link_2 +"\n" * 2
        gaming_label_text_3 = "Article 3: \n" + gaming.article_3 + "\n" * 2 + "link: " + gaming.link_3

        gaming_label_text = gaming_label_text_1 + gaming_label_text_2 + gaming_label_text_3
        self.gaming_label.setText(self._translate("MainWindow", gaming_label_text))

        weather_label_text = weather.weather + "\nlink: https://www.knmi.nl/nederland-nu/weer/verwachtingen"
        self.weather_label.setText(self._translate("MainWindow", weather_label_text))

        self.update_button.setText(self._translate("Win", "Refresh"))
        
def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Win = QtWidgets.QMainWindow()
    ui = Ui_Win()
    ui.setupUi(Win)
    Win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()