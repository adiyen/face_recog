from face_recog_utils import load_users, find_face

if __name__ == "__main__":
    users = load_users("names.txt", "dataSet")
    find_face(users)