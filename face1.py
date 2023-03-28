import cv2

def face(picture_name):
	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
	#讀jpg檔
	img = cv2.imread(picture_name)
	#轉灰階
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#偵測臉部
	faces = face_cascade.detectMultiScale(
	    gray,
	    scaleFactor=1.08,
	    minNeighbors=10,
	    minSize=(16, 48))

	#繪製臉部方框v
	for (x, y, w, h) in faces:
	    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  #(0,255,0)=(blue, green,red)

	#顯示圖片
	cv2.namedWindow('img', cv2.WINDOW_NORMAL)
	cv2.imshow('img', img)
	cv2.waitKey()
	cv2.destroyAllWindows()

	return -1


face('a.jpg')