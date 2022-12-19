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

fig, ax= plt.subplots(subplot_kw={'projection':'polar'})

r= np.arange(0,2,0.01)

theta = 2 *np.pi *r

ax.plot(theta,r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2]) # Less radial ticks
ax.set_rlabel_position(-22.5) # Move radial labels away from plotted line

ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')


## plotting the figure
#for i in rads:
#    plt.polar(i, r, 'g.')
#

#display
plt.show()

