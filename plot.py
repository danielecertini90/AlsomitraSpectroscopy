import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import seaborn as sb

# Read in the file
df = pd.read_csv('seed/XYZ_S1.dat', sep='\t', skiprows=[0,1], names=['EM','EX','I'])

wave_low = 600
wave_high = 900

wave_low_ex = wave_low_em = wave_low
wave_high_ex = wave_high_em = wave_high

df = df.drop( df[df['EX'] < wave_low_ex].index  )
df = df.drop( df[df['EX'] > wave_high_ex].index  )
df = df.drop( df[df['EM'] < wave_low_em].index  )
df = df.drop( df[df['EM'] > wave_high_em].index  )

# Restructure the dataframe in preparation for plotting
df = df.pivot(index='EM', columns='EX', values='I')


# See what the data looks like
#print(df.head())


# Reverse the Y axis
df = df.iloc[::-1]
#
xVals = df.index.tolist() 
yVals = np.array( df[850].values.tolist() ) 
yVals += np.array( df[855].values.tolist() )
yVals += np.array( df[860].values.tolist() )

# delete the last 10 elements of the arrays (some noise)
#xVals = xVals[: len(xVals) - 10]
#yVals = yVals[: len(yVals) - 10]

#print(xVals)
#print(yVals)

# Plot the heatmap
#plt.plot(xVals, yVals)
#sb.heatmap(df, norm=LogNorm(vmin=1000, vmax = 10000000) )
#plt.show()
'''

fig, axs = plt.subplots(2)
axs[0].plot(xVals, yVals)
axs[0].set_title('Intensity of Reflected Light (Incident = 850-860nm)')
axs[0].set_xlabel('Wavelength of Reflected Light [nm]')
axs[0].set_ylabel('[Arb]')

plot_log = False
if plot_log:
    sb.heatmap( df, ax=axs[1], norm=LogNorm(vmin=100000, vmax = 10000000) )
    axs[1].set_title('Intensity of Reflected Light vs Incident Light')
    axs[1].set_xlabel('Wavelength of Incident Light [nm]')
    axs[1].set_ylabel('Wavelength of Reflected Light [nm]')
else:
    sb.heatmap( df, ax=axs[1])
    axs[1].set_title('Intensity of Reflected Light vs Incident Light')
    axs[1].set_xlabel('Wavelength of Incident Light [nm]')
    axs[1].set_ylabel('Wavelength of Reflected Light [nm]')
'''
fig1, axs1 = plt.subplots(1)
fig2, axs2 = plt.subplots(1)
fig3, axs3 = plt.subplots(1)
# Plot Slice
axs1.plot(xVals, yVals)
axs1.set_title('Intensity of Reflected Light (Incident = 850-860nm)')
axs1.set_xlabel('Wavelength of Reflected Light [nm]')
axs1.set_ylabel('[Arb]')
# Plot 3D Log Scale
sb.heatmap( df, ax=axs2, norm=LogNorm(vmin=100000, vmax = 10000000) )
axs2.set_title('Intensity of Reflected Light vs Incident Light')
axs2.set_xlabel('Wavelength of Incident Light [nm]')
axs2.set_ylabel('Wavelength of Reflected Light [nm]')
# Plot 3D Normal Scale
sb.heatmap( df, ax=axs3)
axs3.set_title('Intensity of Reflected Light vs Incident Light')
axs3.set_xlabel('Wavelength of Incident Light [nm]')
axs3.set_ylabel('Wavelength of Reflected Light [nm]')
plt.tight_layout()

plt.show()
