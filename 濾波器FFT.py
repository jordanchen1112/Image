import numpy as np
import cv2
from matplotlib import pyplot as plt 


#FFT
img = cv2.imread('RIM9.jpg',0)
# print(img.shape)
f_img = np.fft.fft2(img)


fshift = np.fft.fftshift(f_img) #低頻移中間
magnitude_spectrum = 20*np.log(np.abs(f_img)) #shift前的頻譜
magnitude_spectrum_shift = 20*np.log(np.abs(fshift)) #shift後的頻譜

rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2) 


#遮罩(LPF)
mask = np.zeros((rows,cols),np.uint8)
mask[crow-100:crow+100, ccol-100:ccol+100] = 1
fshift_L = fshift * mask

fshift_back_L = np.fft.ifftshift(fshift_L)
img_back_L = np.fft.ifft2(fshift_back_L)
LPF_img_back = np.abs(img_back_L)
LPF_img = np.abs(LPF_img_back)

#HPF
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
fshift_back = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(fshift_back)
HPF_img_back = np.abs(img_back)
HPF_img = np.abs(HPF_img_back)


plt.figure(figsize=(20,10))
plt.subplot(231),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('FFT')
plt.subplot(233),plt.imshow(magnitude_spectrum_shift, cmap = 'gray')
plt.title('Shift_FFT')
plt.subplot(234),plt.imshow(HPF_img, cmap = 'gray')
plt.title('HPF_image')
plt.subplot(235),plt.imshow(LPF_img, cmap = 'gray')
plt.title('LPF_image')

plt.show()

# cv2.namedWindow('HPF_img', cv2.WINDOW_NORMAL)
# cv2.imshow("HPF_img", HPF_img )
# cv2.waitKey(0)
# cv2.destroyAllWindows()