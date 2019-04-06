import cv2
import numpy as np
import face_recognition

def scan():

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0)
    user_id = input("Enter user id: ")
    name = input("Enter your name: ")

    f = open("names.txt", "a")
    f.write(user_id + ":" + name + "\n")
    f.close()

    sampleNum = 0
    while True:
        ret, img = cam.read()
        sampleNum += 1
        cv2.waitKey(100)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.imwrite("dataSet/" + str(name) + "." + str(user_id) + "." + str(sampleNum) + ".jpg", img)
            cv2.waitKey(100)
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Face", img)
        k = cv2.waitKey(1)
        if sampleNum > 25:
            break

    cam.release()
cv2.destroyAllWindows()
if __name__ == "__main__":
    scan()

