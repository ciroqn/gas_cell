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
data1 = pd.read_csv('gasA_10mbar.csv', header=4)
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

# Plot methane scans
