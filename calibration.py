import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define straight-line model
def StrtLineModel(x, m, c):
    y_lin = m*x + c
    return (y_lin)

# x-values and y-values here:

x = np.array([545, 5842]) #Put ADC values here (vacuum and atmospheric pressures, respectively)
y = np.array([0, 1021])  # Latter number will vary (Check OU Weather Station for pressure). Vacuum is, of course, 0.


############## Find line of best fit of data & plot

# Call the fitting function - which returns two objects.
popt, pcov = curve_fit(StrtLineModel, x, y)

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

plt.rcParams['figure.figsize'] = [12,8]
plt.xlabel('ADC')
plt.ylabel('Pressure / mbars')
plt.title('Calibration of Pressure Sensor')
plt.scatter(x, y)
plt.plot(x, StrtLineModel(x, m_fit, c_fit), color = 'red')
