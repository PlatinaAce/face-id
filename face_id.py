from deepface import DeepFace
from scipy.spatial.distance import cosine

user_database = {}

def register_face(user_id, img_path):
    embedding_obj = DeepFace.represent(img_path, model_name="Facenet")
    embedding = embedding_obj[0]['embedding']

    user_database[user_id] = embedding
    print(f"User {user_id} has been registered.")

def verify_face(user_id, img_path):
    if user_id not in user_database:
        print("User not registered.")
        return False

    registered_embedding = user_database[user_id]

    embedding_obj = DeepFace.represent(img_path, model_name="Facenet")
    embedding = embedding_obj[0]['embedding']

    similarity = 1 - cosine(registered_embedding, embedding)
    threshold = 0.6

    if similarity > threshold:
        print("Verification successful!")
        print("Similarity: ", similarity)
        return True
    else:
        print("Verification failed.")
        print("Similarity: ", similarity)
        return False

register_face("user1", "user1.png")
register_face("user2", "user2.png")
register_face("user3", "user3.png")

for i in range(1, 13):
    print(f"User 1's Attempt {i}")
    is_verified = verify_face(f"user{1}", f"attempt{i}.png")
    print("Face verified:", is_verified)
    print()

print()
for i in range(1, 13):
    print(f"User 2's Attempt {i}")
    is_verified = verify_face(f"user{2}", f"attempt{i}.png")
    print("Face verified:", is_verified)
    print()

print()
for i in range(1, 13):
    print(f"User 3's Attempt {i}")
    is_verified = verify_face(f"user{3}", f"attempt{i}.png")
    print("Face verified:", is_verified)
    print()