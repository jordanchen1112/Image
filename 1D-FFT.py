import numpy as np
import cv2
from matplotlib import pyplot as plt 
import math

N = 500
T = 1.0 / 1200.0
x = np.linspace(0.0, N*T, N)
y = np.sin(60.0 * 2.0*np.pi*x) + 0.5*np.sin(110.0 * 2.0*np.pi*x) + 1.5*np.sin(290.0 * 2.0*np.pi*x)

y_f = np.fft.fft(y)
x_f = np.fft.fftfreq(np.size(x,0),T)

fig, ax = plt.subplots()
ax.plot(x_f,np.abs(y_f))
plt.show()