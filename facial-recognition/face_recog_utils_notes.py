import cv2
import random
import signal
from glob import glob
import face_recognition

def load_users_notes(names_file, data_dir):
    
    f = open('names.txt', "r")
    users = []
    for line in f:
        user_id, name = line.strip().split(":")
        user = {
            "user_id": user_id,
            "name": name,
            "pics": glob(f"{data_dir}/{name}.{user_id}*.jpg")
        }
        while True:
            picture = user["pics"]
            image = face_recognition.load_image_file(picture)
            encodings = face_recognition.face_encodings(image)
            if len(encodings) == 0:
                # No Face in the image
                print(f"No Face File: {picture}")
            elif len(encodings) > 1:
                # Multiple Faces Found
                print(f"Multiple faces File: {picture}")
            else:
                # Take the only face
                user["encoding"] = face_recognition.face_encodings(image)[0]     
                break
        users.append(user)
    f.close()
    return users

def find_face_notes(users):
    print("hi")
#     face_locations = []
#     face_encodings = []
#     face_names = []
#     process_img = True

#     camera = cv2.VideoCapture(0)
#     running = True
#     while running:
#         ret, img = camera.read()

#         small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

#         rgb_small_img = small_img[:, :, ::-1]

#         if process_img:
#             face_locations = face_recognition.face_locations(rgb_small_img)
#             face_encodings = face_recognition.face_encodings(rgb_small_img, face_locations)

#             face_names = []
#             for face_encoding in face_encodings:
#                 for user in users:
#                     known_face_encodings = [user["encoding"]]
#                     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#                     name = "Unknown"
#                     if True in matches:
#                         name = user["name"]
#                         # with open(str(name) + '_notes.txt', 'r') as f:
#                         #     notes = f.read()
#                         # print(notes)
#                         #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
#                         #running = False
#                         break
#                 face_names.append(name)
#         process_img = not processs_img

#         for (top, right, bottom, left), name in zip(face_locations, face_names):

#             top *= 4
#             right *= 4
#             bottom *= 4
#             left *= 4
#             cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

#             cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             cv2.putText(img, name, (left + 12, bottom - 6), font, 1.0, (255, 255, 255), 1)

#         cv2.imshow('Video', img)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     camera.release()
#     cv2.destroyAllWindows()
