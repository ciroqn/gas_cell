# Plotting absorbances, correpsonding to max peaks in CO2 spectra, against pressures at which they were taken. Pressures for these measurements range 
# from 10-150 mbar.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# See overall plot beforehand:
data = pd.read_csv('pressab_gas2.csv', header=1)

data.head()

print(data.columns.tolist()) # again, had trouble with col name. Turns out there was an extra space...

x = data['pressure / mbar']
y = data['bend absorbance']

plt.rcParams['figure.figsize'] = (12, 8)
plt.scatter(x, y)

# Plot data

from scipy.optimize import curve_fit

def StrtLineModel(x, m, c):
    y_lin = m*x + c
    return (y_lin)

x_select = x[:4]  # this data selects only up to 70 mbar. This is because the data from 10-70 mbar follow a linear path.
y_select = y[:4]

# Call the fitting function - which returns two objects. The variables 'popt' and 'pcov' 
popt, pcov = curve_fit(StrtLineModel, x_select, y_select)

print(popt)
print(pcov)

# Calculate the errors on the returned parameters
perr = np.sqrt(np.diag(pcov)) # squares of the error values are 
                              # on the covariance matrix diagonal

# For readability, extract values from popt and perr into named variables
m_fit = popt[0]
c_fit = popt[1]
m_err = perr[0]
c_err = perr[1]
    
# Now we can print out the optimised fit parameters and 1-sigma estimates
print('fit parameter 1-sigma error')
print('***************************************************')
print (f'm = {m_fit:.2f} +/- {m_err:.2f}')
print (f'c = {c_fit:.2f} +/- {c_err:.2f}')
print('***************************************************')

# Now plot the data and add the optimised line. 
# This time we already have a function defined to 
# calculate the straight line - called this time with the optimised 
# parameters returned by curvefit()

from scipy.stats import linregress

# This single line does the linear regression fit
m, c, r, p, stderr = linregress(x_select, y_select)

print(f'Gradient: {m:.2f} +/- {stderr:.2f}, Intercept: {c:.2f}')
print(f'Correlation coefficient: {r:.3f}')
# Plot the line on to the data:
xstart = x_select.min() - 1                 # calculate start and end x values
xend   = x_select.max() + 70                 # for plotting the fitted line 
xlin   = np.linspace(xstart, xend, 50) # create array of x values for the line
ylin   = m*xlin+c                      # generate the y values for the straight line

plt.scatter(x, y, label='Data points')                      # plot the data points

plt.plot(xlin, ylin, color = 'red', label='Linear Best fit')    # plot the fitted line 
plt.legend()
#plt.title('Absorbance of IR in $CO_{2}$ samples with various pressures')
plt.xlabel('Pressure / mbar')
plt.ylabel('Absorbance')
plt.rcParams['font.size'] = 18
plt.show()

plt.scatter(x, y)
plt.plot(x_select, StrtLineModel(x_select, m_fit, c_fit), color = 'red')
plt.show()

