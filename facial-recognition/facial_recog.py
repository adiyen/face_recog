import face_recognition

Krishna_image1 = face_recognition.load_image_file("Krishna_image.png")
Krishna_image2 = face_recognition.load_image_file("Krishna2_image.png")

Krishna_encoding1 = face_recognition.face_encodings(Krishna_image1)[0]
Krishna_encoding2 = face_recognition.face_encodings(Krishna_image2)[0]


results = face_recognition.compare_faces([Krishna_encoding1], Krishna_encoding2)
print(results)

if results == [True]:
    print("Both are Same!")
else:
    print("Someone else is here!")