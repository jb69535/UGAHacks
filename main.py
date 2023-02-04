import pandas as pd
import folium
import branca
import webbrowser

class Map:
    def init(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start

    def showMap(self):
        #Create the map
        my_map = folium.Map(location = self.center, zoom_start = self.zoom_start)
        #Display the map
        my_map.save("map.html")
        webbrowser.open("map.html")



df = pd.read_excel('TokyoCafe.xlsx')


request = "https://geo.ipify.org/api/v1?apiKey=%s&ipAddress=%s" % (API_KEY, i)

try:
	with urlopen(request) as url:
            data = json.loads(url.read().decode())


location = float(data["location"]["lat"], float(data["location"]["lng"])
m = folium.Map(location=location,zoom_start=13)
m


def auto_open(path):
    html_page = f'{path}'
    f_map.save(html_page)
    # open in browser.
    new = 2
    webbrowser.open(html_page, new=new)

def popup_html(row):
    i = row
    Name = df['Name'].iloc[i]
    Study = df['Study'].iloc[i]
    Date = df['Date'].iloc[i]
    Chill =df['Chill'].iloc[i]

    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"

    html = """<!DOCTYPE html>
<html>
<head>
<h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(Name) + """
</head>
    <table style="height: 100px; width: 250px;">
<tbody>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Study</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(Study) + """
</tr>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Date</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(Date) + """
</tr>
<tr>
<td style="background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Chill</span></td>
<td style="width: 150px;background-color: """ + right_col_color + """;">{}</td>""".format(Chill) + """
</tr>
</tbody>
</table>
</html>
"""
    return html

for i in range(0, len(df)):
    html = popup_html(i)
    iframe = branca.element.IFrame(html=html, width=510, height=280)
    popup = folium.Popup(folium.Html(html, script=True), max_width=500)
    folium.Marker([df['latitude'].iloc[i], df['longitude'].iloc[i]],
                  popup=popup, icon=folium.Icon(color='blue', icon='info-sign', prefix='fa')).add_to(m)


Tokyomap='Tokyomap.html'

m.save('Tokyomap.html')

webbrowser.open(Tokyomap)

subdf=pd.DataFrame()
subdf=df['Name', 'Address','latitude', 'longitude']



######
import tkinter
import sys

from random import *

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class QtGUI(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("CafeName")

        self.resize(360, 400)

        self.index = 1

        self.but_list = []

        label1 = QLabel(self.intialL1, self)

        label1.move(10, 10)

        label2 = QLabel(self.intialL2, self)

        label2.move(10, 50)

        # 숫자 버튼 생성

        for i in range(1, length):
            self.make_button_num(self.index)

            self.index = self.index + 1

        # 로또 번호 생성 버튼 생성

        button = QPushButton('Generate', self)

        button.move(20, 350)

        button.clicked.connect(lambda: self.print_label(label2))

        # 선택 번호 초기화

        button1 = QPushButton('refresh', self)

        button1.move(100, 350)

        button1.clicked.connect(self.refresh_but)

        self.show()

    def Make_Number(self):

        Number = []

        Number.extend(self.selected_num)

        while len(Number) & lt; 6:

            v = randint(1, 45)

            if v not in Number:
                Number.append(v)

        return Number

    def make_button_num(self, index):

        button = QPushButton(str(index), self)

        button.resize(30, 30)

        w = 0

        v = 0

        if index & lt; 11:

            w = 100

            v = index

        elif index & lt; 21:

            w = 150

            v = index - 10

        elif index & lt; 31:

            w = 200

            v = index - 20

        elif index & lt; 41:

            w = 250

            v = index - 30

        else:

            w = 300

            v = index - 40

        button.move(v * 30, w)

        self.but_list.append(button)

        button.clicked.connect(lambda: self.inputnum(button))

    def print_label(self, label):

        Number = self.Make_Number()

        Number.sort()

        label.setText(str(Number))

    def inputnum(self, button):

        if len(self.selected_num) & lt; 5:

            self.selected_num.append(int(button.text()))

            button.setEnabled(False)

    def refresh_but(self):

        self.selected_num = []

        for i in self.but_list:
            i.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = QtGUI()

    app.exec_()

def btn1press():
    StudyR=input("Rate for Study: ")
    df.iloc[i,]



def btn2press():



btn.config(command=btnpress)
btn1.config(command = btn1press)
btn2.config(command = btn2press)

win.pack()

win.mainloop()

####

