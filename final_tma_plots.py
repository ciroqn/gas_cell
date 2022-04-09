# multiple plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def LinearBaseline(x, y, points):
    x1 = x[0]
    x2 = x[len(x)-1]
    y1 = np.mean(y[0:points])
    y2 = np.mean(y[-points:-1])
    
    grad = (y2-y1)/(x2-x1)
    intercept = y1-grad*x1

    baseline_fit = grad*x + intercept
    
    return baseline_fit

# Could of course use glob and loops, but...
  
# Read data
data1 = pd.read_csv('gasA_10mbar.csv', header=4) #-> this may bring up error in Jupyter
data2 = pd.read_csv('gasA_20mbar.csv', header=4)
data3 = pd.read_csv('gasA_50mbar.csv', header=4)
data4 = pd.read_csv('gasA_100mbar.csv', header=4)
data5 = pd.read_csv('gasA_120mbar.csv', header=4)
data6 = pd.read_csv('gasA_150mbar.csv', header=4)

# Zero baseline

background = pd.read_csv('background_sample.csv', header=4)
baseline1 = LinearBaseline(data1['wavenumber / cm-1'], data1['Absorbance'], 20)
baseline2 = LinearBaseline(data2['wavenumber / cm-1'], data2['Absorbance'], 20)
baseline3 = LinearBaseline(data3['wavenumber / cm-1'], data3['Absorbance'], 20)
baseline4 = LinearBaseline(data4['wavenumber / cm-1'], data4['Absorbance'], 20)
baseline5 = LinearBaseline(data5['wavenumber / cm-1'], data5['Absorbance'], 20)

# Subtract background scans:
data1_absorbance = data1['Absorbance'] - background['Absorbance']
data1_absorbance_corr = data1_absorbance -baseline1
print(max(data1['Absorbance']))
listA_1 = data1_absorbance_corr.tolist()
print(max(listA_1))

data2_absorbance = data2['Absorbance'] - background['Absorbance']
data2_absorbance_corr = data2_absorbance - baseline2
print(max(data2['Absorbance']))

data3_absorbance = data3['Absorbance'] - background['Absorbance']
data3_absorbance_corr = data3_absorbance - baseline3
print(max(data3['Absorbance']))

data4_absorbance = data4['Absorbance'] - background['Absorbance']
data4_absorbance_corr = data4_absorbance - baseline4
print(max(data4['Absorbance']))

data5_absorbance = data5['Absorbance'] - background['Absorbance']
data5_absorbance_corr = data5_absorbance - baseline5
print(max(data5['Absorbance']))

# Plot CO2 scans:

plt.rcParams['figure.figsize'] = [18,14]
plt.rcParams['font.size'] = 18
plt.xlabel('Wavenumber / $cm^-1$')
plt.ylabel('Absorbance (A)')
plt.plot(data1['wavenumber / cm-1'], data1_absorbance_corr, label="10 mbar (max A: 0.072)")
plt.plot(data2['wavenumber / cm-1'], data2_absorbance_corr+0.1, label="20 mbar (max A: 0.15)")
plt.plot(data3['wavenumber / cm-1'], data3_absorbance_corr+0.2, label="50 mbar (max A: 0.45)")
plt.plot(data4['wavenumber / cm-1'], data4_absorbance_corr+0.3, label="100 mbar (max A: 1.25)")
plt.plot(data5['wavenumber / cm-1'], data5_absorbance_corr+0.49, label="120 mbar (max A: 1.64)")

plt.legend()
ax = plt.gca()

plt.annotate("$CO_{2}$ Vib. 1 (3800-3500 $cm^-1$)",
            xy=(3600, 0.68), xycoords='data',
            xytext=(3850, 0.8), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
plt.annotate("$CO_{2}$ Vib. 2 (3800-3500 $cm^-1$)",
            xy=(2300, 1.6), xycoords='data',
            xytext=(2200, 1.9), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
plt.annotate("$CO$ Vib. 1 (~2200-2100 $cm^-1$)",
            xy=(2150, 0.65), xycoords='data',
            xytext=(2200, 1.0), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )


rectA = patches.Rectangle(xy=(3500,-0.05), width=300, height=0.7, linewidth=1.5, linestyle='--', edgecolor='r', facecolor='none')
rectA_1 = patches.Rectangle(xy=(2100,-0.05), width=100, height=0.7, linewidth=1.5, linestyle='--', edgecolor='r', facecolor='none')
ax.add_patch(rectA)
ax.add_patch(rectA_1)

plt.gca().invert_xaxis()
plt.show()

# Do necessary subtractions for gas B:

dataB1 = pd.read_csv('gasB_20mbar.csv', header=4)
dataB2 = pd.read_csv('gasB_20_mbar.csv', header=4)
dataB3 = pd.read_csv('gasB_50mbar.csv', header=4)
dataB4 = pd.read_csv('gasB_90mbar.csv', header=4)
dataB5 = pd.read_csv('gasB_120mbar.csv', header=4)
dataB6 = pd.read_csv('gasB_200mbar.csv', header=4)
dataB7 = pd.read_csv('gasB_280mbar.csv', header=4)

backgroundB = pd.read_csv('background_gasB.csv', header=4)
baselineB1 = LinearBaseline(dataB1['wavenumber / cm-1'], dataB1['Absorbance'], 20)
baselineB2 = LinearBaseline(dataB2['wavenumber / cm-1'], dataB2['Absorbance'], 20)
baselineB3 = LinearBaseline(dataB3['wavenumber / cm-1'], dataB3['Absorbance'], 20)
baselineB4 = LinearBaseline(dataB4['wavenumber / cm-1'], dataB4['Absorbance'], 20)
baselineB5 = LinearBaseline(dataB5['wavenumber / cm-1'], dataB5['Absorbance'], 20)
baselineB6 = LinearBaseline(dataB6['wavenumber / cm-1'], dataB5['Absorbance'], 20)
baselineB7 = LinearBaseline(dataB7['wavenumber / cm-1'], dataB7['Absorbance'], 20)

print(max(dataB6['Absorbance']))
data1_absorbanceB = dataB1['Absorbance'] - backgroundB['Absorbance']
data1_absorbance_corrB = data1_absorbanceB -baselineB1
list1 = data1_absorbance_corrB.tolist()
print(max(list1))

data2_absorbanceB = dataB2['Absorbance'] - backgroundB['Absorbance']
data2_absorbance_corrB = data2_absorbanceB - baselineB2
list2 = data2_absorbance_corrB.tolist()
print(max(list2))

data3_absorbanceB = dataB3['Absorbance'] - backgroundB['Absorbance']
data3_absorbance_corrB = data3_absorbanceB - baselineB3
list3 = data3_absorbance_corrB.tolist()
print(max(list3))

data4_absorbanceB = dataB4['Absorbance'] - backgroundB['Absorbance']
data4_absorbance_corrB = data4_absorbanceB - baselineB4
list4 = data4_absorbance_corrB.tolist()
print(max(list4))

data5_absorbanceB = dataB5['Absorbance'] - backgroundB['Absorbance']
data5_absorbance_corrB = data5_absorbanceB - baselineB5
list5 = data5_absorbance_corrB.tolist()
print(max(list5))

data6_absorbanceB = dataB6['Absorbance'] - backgroundB['Absorbance']
data6_absorbance_corrB = data6_absorbanceB - baselineB6
list6 = data6_absorbance_corrB.tolist()
print(max(list6))

data7_absorbanceB = dataB7['Absorbance'] - backgroundB['Absorbance']
data7_absorbance_corrB = data7_absorbanceB - baselineB7
list7 = data7_absorbance_corrB.tolist()
print(max(list7))

# Plot scans for gas B:

import matplotlib.patches as patches

plt.rcParams['figure.figsize'] = [18,14]
plt.rcParams['font.size'] = 14
plt.rcParams['legend.loc'] = 'upper left'
plt.xlabel('Wavenumber / $cm^{-1}$')
plt.ylabel('Absorbance (A)')
plt.plot(dataB1['wavenumber / cm-1'], data1_absorbance_corrB+0.15, label="10 mbar (max A: 0.035)")
plt.plot(dataB2['wavenumber / cm-1'], data2_absorbance_corrB+0.2, label="20 mbar (max A: 0.057)")
plt.plot(dataB3['wavenumber / cm-1'], data3_absorbance_corrB+0.25, label="50 mbar (max A: 0.11)")
plt.plot(dataB4['wavenumber / cm-1'], data4_absorbance_corrB+0.3, label="100 mbar (max A: 0.19)")
plt.plot(dataB5['wavenumber / cm-1'], data5_absorbance_corrB+0.39, label="120 mbar (max A: 0.25)")
plt.plot(dataB7['wavenumber / cm-1'], data7_absorbance_corrB, label="280 mbar (max A: 0.56)")
plt.legend()
ax = plt.gca()
plt.annotate("$CH_{4}$ Vib. 1 (3019 $cm^{-1}$)",
            xy=(3000, 0.58), xycoords='data',
            xytext=(2950, 0.65), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )

plt.annotate("$CH_{4}$ Vib. 2 (1306 $cm^{-1}$)",
            xy=(1300, 0.54), xycoords='data',
            xytext=(1500, 0.63), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )

plt.annotate("$CH_{4}$ Vib. 3 (~2840-2680 $cm^{-1}$)",
            xy=(2750, 0.402), xycoords='data',
            xytext=(2900, 0.45), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
plt.annotate("$CH_{4}$ Vib. 4 (~1600-1400 $cm^{-1}$)",
            xy=(1500, 0.402), xycoords='data',
            xytext=(2200, 0.42), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"), 
            )

plt.annotate("$CH_{4}$ Base Reading (~3200-3170 $cm^{-1}$)",
            xy=(3185, 0.402), xycoords='data',
            xytext=(3850, 0.52), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"), 
            )

plt.annotate("$CH_{4}$ Base Reading (~1240-1180 $cm^{-1}$)",
            xy=(1200, 0.402), xycoords='data',
            xytext=(2190, 0.5), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"), 
            )
plt.annotate("Potential trace gas region ($CH_{3}OH, C_{2}H_{6}$)",
            xy=(2950, 0.39), xycoords='data',
            xytext=(2800, 0.33), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"), 
            )



rect = patches.Rectangle(xy=(2680,0.383), width=160, height=0.02, zorder=3,linewidth=1.5, linestyle='--',edgecolor='r', facecolor='none')
rect1 = patches.Rectangle(xy=(1400,0.383), width=160, height=0.02, zorder=3,linewidth=1.5, linestyle='--', edgecolor='r', facecolor='none')
rect2 = patches.Rectangle(xy=(3170,0.383), width=30, height=0.02, zorder=3,linewidth=1.5,linestyle='--', edgecolor='r', facecolor='none')
rect3 = patches.Rectangle(xy=(1180,0.383), width=60, height=0.02, zorder=3,linewidth=1.5,linestyle='--', edgecolor='r', facecolor='none')
rect4 = patches.Rectangle(xy=(2850,0.383), width=250, height=0.02, zorder=3,linewidth=1.5,linestyle='--', edgecolor='b', facecolor='none')
ax.add_patch(rect)
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)
ax.add_patch(rect4)

plt.gca().invert_xaxis()
plt.savefig('gasB_mixture.png')
plt.show()

