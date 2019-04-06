import face_recognition
import cv2
import random
from glob import glob

camera = cv2.VideoCapture(0)

rand_pic = random.randint(15, 21)

f = open("names.txt", "r")
users = []
for line in f:
    user_id, person_name = line.split(":")
    print(user_id, person_name)
    user = {
        "user_id": user_id,
        "name": person_name,
        "pics": glob(f"dataSet/{name}.{user_id}*.jpg")
    }
    random_pic = random.choice(user["pics"])
    
    image = face_recognition.load_image_file(random_pic)
    user["encoding"] = face_recognition.face_encodings(image)[0]
    users.append(user)
f.close()

krishna_image = face_recognition.load_image_file(str(random1_pic))

krishna_face_encoding = face_recognition.face_encodings(krishna_image)[0]

appa_image = face_recognition.load_image_file(str(random2_pic))

appa_face_encoding = face_recognition.face_encodings(appa_image)[0]

known_face_encodings = [

    krishna_face_encoding,
    appa_face_encoding
]
known_face_names = [
    str(person_name)
]

face_locations = []
face_encodings = []
face_names = []
process_img = True

while True:
    ret, img = camera.read()

    small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)


    rgb_small_img = small_img[:, :, ::-1]

    if process_img:
        face_locations = face_recognition.face_locations(rgb_small_img)
        face_encodings = face_recognition.face_encodings(rgb_small_img, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]


            face_names.append(name)

    process_img = not process_img

    for (top, right, bottom, left), name in zip(face_locations, face_names):

        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, name, (left + 12, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()