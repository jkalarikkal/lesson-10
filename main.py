import cv2

carvpath = cv2.VideoCapture('/Users/jaanvikalarikkal/Desktop/open CV/lesson 10/cars.mp4')
caars = cv2.CascadeClassifier('/Users/jaanvikalarikkal/Desktop/open CV/lesson 10/cars.xml')

while True:
    ret, frames = carvpath.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    car = caars.detectMultiScale(gray, 1.1, 1)
    for (x,y,w,z) in car:
        cv2.rectangle(frames, (x, y), (x + w, y + z), (255, 0, 0), 2)

    cv2.imshow('OpenCV', frames)
    key = cv2.waitKey(0)
    if key == 27:
        break

