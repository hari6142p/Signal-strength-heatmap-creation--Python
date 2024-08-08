import pandas as pd
import folium
from folium.plugins import HeatMap

data = pd.read_csv('airtelnet.csv')
m = folium.Map(location=[data['lat'].mean(), data['lon'].mean()], zoom_start=12)
heat_data = [[row['lat'], row['lon'], row['signal']] for index, row in data.iterrows()]
data['signal'] = data['signal'] + 120
data['signal'] = (round((data['signal'] / 60)*10))/10
gradient = {0: 'red', 0.1: 'red', 0.2: 'red', 0.3: 'red', 0.4: 'red', 0.5: 'red',
            0.6: 'yellow', 0.7: 'yellow', 0.8: 'yellow', 0.9: 'green', 1: 'green'}
folium.plugins.HeatMap(heat_data, gradient=gradient).add_to(m)
legend_html = '''
     <div style="position: fixed;
                 top: 10px; right: 10px; width: 200px; height: 50px;
                 background-color: rgba(255, 255, 255, 0.5);
                 border-radius: 5px; padding: 10px;
                 z-index:9999;">
      <p style="margin-bottom:5px;"><strong>Signal Strength</strong></p>
      <div style="display:flex; justify-content: space-between;">
        <div style="width:30%; background-color:red; height:15px;"></div>
        <div style="width:30%; background-color:yellow; height:15px;"></div>
        <div style="width:30%; background-color:green; height:15px;"></div>
      </div>
      <p style="margin-top:5px;"><span style="margin-right:20px; color:black">Weak</span><span style="margin-right:20px; color:black">Medium</span><span style="color:black">Strong</span></p>
     </div>
     '''
m.get_root().html.add_child(folium.Element(legend_html))
m.save('network_heatmap.html')
