import pandas as pd 
import folium
import branca
import numpy as np
import plotly.express as px


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


#Define coordinates of where we want to center our map
coords = [35.7036892655866, 139.66090693994255]
map = Map(center = coords, zoom_start = 13)
map.showMap()

# import plotly.graph_objects as go

df = pd.read_excel('TokyoCafe.xlsx')
print(df)


# code making chart
df_temp = pd.DataFrame

#for i in range(df.index):
 #   df['Study'] =
#   df['Date'] = 
#   df['Chill'] = 


 #   df_temp= pd.append(figure)
#return df

#df=pd.concat([df, df_temp])