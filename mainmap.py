import folium
import branca
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_excel('TokyoCafe.xlxs')
df
location = df['latitude'].mean(), df['longitude'].mean()
m = folium.Map(location=location,zoom_start=3)
m

# code making chart
#df_temp=pd.DataFrame
#for index in :
#    df['Study'] =
#   df['Date'] = 
#   df['Chill'] = 

    
 #   df_temp= pd.append(figure)
#return df

#df=pd.concat([df, df_temp])
