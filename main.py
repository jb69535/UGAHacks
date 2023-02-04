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

location = df['latitude'].mean(), df['longitude'].mean()
m = folium.Map(location=location,zoom_start=3)
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
    <table style="height: 126px; width: 350px;">
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

