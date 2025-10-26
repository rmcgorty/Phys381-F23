'''
niceplot.py

Sets up some defaults for publication-quality plots. Also defines some
constants for use in plots.

import with:
from niceplot import *
'''

import matplotlib
from matplotlib import pyplot as plt
import numpy as np

# column widths for Nature (in inches)
onecol = 89 / 25.4
twocol = 183 / 25.4
golden = 1.618  # golden ratio

# useful colors
gray10 = '#191919'
gray20 = '#333333'
gray30 = '#4C4C4C'
gray40 = '#666666'
gray50 = '#7F7F7F'
gray60 = '#999999'
gray70 = '#B2B2B2'
gray80 = '#CCCCCC'
gray90 = '#E5E5E5'

gray25 = '#3F3F3F'
gray75 = '#BFBFBF'

black = '#000000'

warm_red = '#E64F2C'
blue_214 = '#7BAFDE' # Pantone DS 214-5
blue_645 = '#739ABC'    # Pantone 645
blue_653 = '#21578A'    # Pantone 653
green_556 = '#70A489'   # Pantone 556
violet = '#4B08A1'      # Pantone violet
reflex_blue = '#002395' # Pantone reflex blue
green_330 = '#005751'   # Pantone 330
yellow_117 = '#C79900'  # Pantone 116

# colors to use for plots
axis_color = black #gray40 

# Set some defaults for plotting to get nice output for publication 
matplotlib.rcParams['lines.linewidth'] = 0.5 
matplotlib.rcParams['lines.antialiased'] = False 
matplotlib.rcParams['patch.linewidth'] = 0.5 
matplotlib.rcParams['patch.antialiased'] = False 
matplotlib.rcParams['font.family'] = 'sans-serif'
# figure out how to change font to Myriad before submission
matplotlib.rcParams['legend.fontsize'] = 8#12
matplotlib.rcParams['legend.handlelength'] = 1.5
matplotlib.rcParams['font.sans-serif'] = ['DejaVu Sans']
matplotlib.rcParams['font.size'] = 8#12#7
matplotlib.rcParams['axes.titlesize'] = 8#12 #7
matplotlib.rcParams['axes.labelsize'] = 8#12 #7
matplotlib.rcParams['axes.linewidth'] = 0.5 
matplotlib.rcParams['xtick.labelsize'] = 8#10
matplotlib.rcParams['xtick.major.size'] = 3 
matplotlib.rcParams['ytick.major.size'] = 3
matplotlib.rcParams['ytick.labelsize'] = 8#10
# with this parameter off, fonts will be editable in inkscape
matplotlib.rcParams['svg.fonttype'] = 'none'
matplotlib.rcParams['pdf.compression'] = 0 
matplotlib.rcParams['pdf.fonttype'] = 42		# embed truetype fonts
matplotlib.rcParams['axes.edgecolor'] = axis_color
matplotlib.rcParams['figure.facecolor'] = 'w'
matplotlib.rcParams['xtick.color'] = axis_color
matplotlib.rcParams['ytick.color'] = axis_color

matplotlib.rcParams['figure.subplot.bottom'] = 0.15
matplotlib.rcParams['figure.subplot.left'] = 0.15


#############################################################################

msize = 4  #marker size
medgew = 1 #marker edge width

axes_label_fontsize = 6
axes_tick_fontsize = 6

figwidth_inches = 3



fig,ax = plt.subplots(figsize=(figwidth_inches,figwidth_inches/1.618)) 

xdata = np.array([1, 2,3,4, 5,  6,  7,8,9,10])
ydata = np.array([270,190,130,98,101,42,18,8,1,-3])
ydata2 = np.abs(ydata[::-1])**0.5

ax.plot(xdata, ydata, 's', color=warm_red,
        ms=msize, mew=medgew, mec=gray20, alpha=0.7)

ax2 = ax.twinx()  #creating a new axis that will share the x-axis
ax2.plot(xdata, ydata2, 'o', color=reflex_blue,
        ms=msize, mew=medgew, mec=gray20, alpha=0.7)

ax.set_xlabel("Angular frequency (rad/s)", fontsize=axes_label_fontsize)
ax.set_ylabel("Storage modulus, G' (Pa)", fontsize=axes_label_fontsize)
ax.tick_params(axis='both', direction='in', which='both', labelsize=axes_tick_fontsize)

ax2.set_ylabel("Something else (A.U.)", fontsize=axes_label_fontsize)
ax2.tick_params(axis='both', direction='in', which='both', labelsize=axes_tick_fontsize)

ax.yaxis.labelpad = 0 #can be used to move the axis label towards or away from the axis
ax.xaxis.labelpad = 0

plt.savefig("test.svg", bbox_inches='tight')
