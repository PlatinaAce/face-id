from deepface import DeepFace
from scipy.spatial.distance import cosine

user_database = {}

def register_face(user_id, img_path):
    embedding_obj = DeepFace.represent(img_path, model_name="Facenet")
    embedding = embedding_obj[0]['embedding']

    user_database[user_id] = embedding
    print(f"User {user_id} has been registered.")

def verify_face(user_id, img_path):
    registered_embedding = user_database[user_id]

    embedding_obj = DeepFace.represent(img_path, model_name="Facenet")
    embedding = embedding_obj[0]['embedding']

    similarity = 1 - cosine(registered_embedding, embedding)
    threshold = 0.8

    if similarity > threshold:
        print("Verification successful!")
        return True
    else:
        print("Verification failed.")
        return False

register_face("user1", "user1.jpg")

is_verified = verify_face("user1", "attempt1.jpg")
print("Face verified:", is_verified)
print()

is_verified = verify_face("user1", "attempt2.jpg")
print("Face verified:", is_verified)
print()

is_verified = verify_face("user1", "attempt3.jpg")
print("Face verified:", is_verified)