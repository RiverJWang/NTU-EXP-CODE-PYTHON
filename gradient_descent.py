import numpy as np

x_data = [ 338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
y_data = [ 640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]
# ydata = b + w * xdata

x = np.arange(-200, -100, 1)  # bias
y = np.arange(-5, 5, 0.1)  # weight
z = np.zeros((len(x), len(y)))
X, Y = np.meshgrid(x, y)
for i in range(len(x)):
    for j in range(len(x)):
        b = x[i]
        w = y[j]
        z[j][i] = 0
        for n in range(len(x_data)):
            z[j][i] = z[j][i] + (y_data[n] - b - w*x_data[n]**2)
        z[j][i] = z[j][i]/len(x_data)
