from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import ephem
import datetime

import os
import time
from time import sleep
import numpy as np
from ephem import degree

#iss tle most accurate
line1 = "ISS (ZARYA)"

line2 = "1 25544U 98067A   19095.68649177  .00002173  00000-0  42341-4 0  9993"
line3 = "2 25544  51.6448   1.6253 0002230 148.7687 296.9409 15.52489908163993"

iss = ephem.readtle(line1, line2, line3)

num = 10000
x = "2019-04-05 13:15:17.0"

#miller projection (there are other types)
map = Basemap(projection='mill')

    #design and plot
map.drawcoastlines()
map.fillcontinents()
map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])

#fill colour
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
plt.title('day and night')



lats = np.arange(num)
lons = np.arange(num)
for z in range(num):

    x = "2019-04-05 13:15:17.0"
    x = datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S.%f')
    x = x + datetime.timedelta(seconds = z)

    iss.compute(x)

    #print (iss.sublong / degree, iss.sublat / degree)




#draw sin wave for iss
#map.matplotlib.markers
    lats[z]= (iss.sublat /degree)

    lons[z]= (iss.sublong /degree)
    #print (lons[z], lats[z])
    #print('%s;%s;%s' % ( x,lons[z], lats[z]))

x, y = map(lons, lats)
    
map.scatter(x, y, marker='o',color='m', s=1, zorder=10)


    #map.plot([lats],[lons])
from datetime import datetime
# shade the night areas      
date = datetime(2019, 5, 4, 13)
CS=map.nightshade(date)
#CS = map.nightshade(x)
plt.show()
