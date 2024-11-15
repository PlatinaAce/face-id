from deepface import DeepFace

user_database = {}

def register_face(user_id, img_path):
    embedding_obj = DeepFace.represent(img_path, model_name="Facenet")
    embedding = embedding_obj[0]['embedding']
    user_database[user_id] = embedding
    print(f"User {user_id} has been registered.")

register_face("user1"  ,"user1.jpg")