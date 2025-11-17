# Source - https://stackoverflow.com/a
# Posted by Alessandro, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-08, License - CC BY-SA 3.0

import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

fn = 'data/test/test_382cedb7-3579-4b3f-b533-1fab36d5a3f2_2025.01_18.nc'
ds = nc.Dataset(fn)

print(ds)

for dim in ds.dimensions.values():
    print(dim)

print()

for var in ds.variables.values():
    print(var)

print(ds['AirTemperatureMean'].shape)

# for x in range(len(ds['AirTemperatureMean'])):
#     for y in range(len(ds['AirTemperatureMean'][x])):
#         for v in range(len(ds['AirTemperatureMean'][x][y])):
#             val = ds['AirTemperatureMean'][x][y][v]
#             if val is not np.ma.masked:
#                 print(f'({x}, {y}, {v}) -> {val}')

x = 0
lat = []
lon = []
for y in range(len(ds['AirTemperatureMean'][x])):
    for v in range(len(ds['AirTemperatureMean'][x][y])):
        val = ds['AirTemperatureMean'][x][y][v]
        if val is not np.ma.masked:
            lat.append(ds['lat'][y])
            lon.append(ds['lon'][v])
            print(f'({ds['time'][x]}, {ds['lat'][y]}, {ds['lon'][v]}) -> {val}')

plt.plot(lon, lat, 'o')
plt.show()