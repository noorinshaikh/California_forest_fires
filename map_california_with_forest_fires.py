import folium
import pandas

def get_destruction(val):
  if val<100:
    return 'orange'
  elif 1000>val>=100:
    return 'lightred'
  else:
    return 'darkred'
data=pandas.read_excel('california_nearby_fires.xlsx',sheet_name=0)
map_cal=folium.Map(zoom_start=5,width="90%",height="90%",location=[36.778259,-119.417931])
fg=folium.FeatureGroup("Forest_fires")
for index, row in data.iterrows():
    fg.add_child(folium.Marker(location=[float((row['Coordinates'].split(',')[0]).strip()),float((row['Coordinates'].split(',')[1]).strip())],popup=(str(row['Size'])+'\n\n'+str(row['Type'])), icon=folium.Icon(color=get_destruction(int(row['Size'].strip(" Acres"))), icon_color='white')))
fg_pop=folium.FeatureGroup("Population")
fg_pop.add_child(folium.GeoJson(data=('us_states_pop.json'),style_function=lambda x: {'fillColor':'yellow' if x['properties']['pop'] < 4000000 
else 'orange' if 4000000<=x['properties']['pop']<6000000 else 'red' if 6000000<=x['properties']['pop']<8000000 else 'darkred'}))
map_cal.add_child(fg)
map_cal.add_child(fg_pop)
map_cal.add_child(folium.LayerControl())
map_cal.save("Forest_fires.html")
