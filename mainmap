pip install folium
conda install geopandas

import folium
import branca
import pandas as pd

maindf = pd.read_csv('uni_if.csv')
maindf
location = df['Latitude'].mean(), df['Longitude'].mean()
m = folium.Map(location=location,zoom_start=3)
m

def popup_html(row):
    i = row
    Study=df['Institution Name'].iloc[i]
    Date=df['Institution Name'].iloc[i]
    Chill=df['Institution Name'].iloc[i]

    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"

    html = """<!DOCTYPE html>
<html>
<head>
<h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(institution_name) + """
</head>
    <table style="height: 126px; width: 350px;">
<tbody>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">institution_name</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(institution_name) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">State</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(State) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Program</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(Program) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">institution_type</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(institution_type) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Priority_Deadline</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(Priority_Deadline) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Final_Deadline</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(Final_Deadline) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Program_Structure</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(Program_Structure) + """
</tr>
</tbody>
</table>
</html>
"""
    return html

  for i in range(0, len(df)):
    state_type = df['State_nic'].iloc[i]
    if state_type == 'Distance':
        color = 'gray'
    else:
        color = 'darkblue'

    html = popup_html(i)
    iframe = branca.element.IFrame(html=html,width=510,height=280)
    popup = folium.Popup(folium.Html(html, script=True), max_width=500)
    folium.Marker([df['Latitude'].iloc[i],df['Longitude'].iloc[i]],
                  popup=popup,icon=folium.Icon(color=color, icon='cafe', prefix='fa')).add_to(m)
m
