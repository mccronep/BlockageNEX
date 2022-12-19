#
try:
    #
    from matplotlib import use
    #use("agg")
    #
    import calendar
    import os
    import numpy as np
    import matplotlib.pyplot as plt
    from netCDF4 import Dataset
    import cartopy.feature as cfeat
    #
    import cartopy.crs as ccrs
except:
    print('Python Module Failure')
    print('Check out python modules')


#
dadash='-------------------------------------'
print(dadash+dadash)

pi = 355.0/113.0

deg2rad = pi/180.0

WARNING_INIT_ERROR = 1

plt.axes(projection = 'polar')
#plt.set_theta_zero_location("N")

r=3

rads = np.arange(0, (2 * np.pi), 0.01)

# plotting the circle
for i in rads:
    plt.polar(i, r, 'g.')

#display
plt.show()

