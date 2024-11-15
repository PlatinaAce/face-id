# Group 4(김지원, 황종서, 박동일) - Face Recognition System (Face ID)

## Project Overview
This project implements a system to register and verify user faces using the `DeepFace` and `scipy` libraries. Users can register their face images, which are stored as embedding vectors in a database, and later verify their identity by comparing a new face image to the stored embedding. Cosine similarity is used to calculate the similarity between the registered and input embeddings, with a predefined threshold determining the verification result.

### Key Features
1. **Face Registration**: Users can register their face images, which are converted into embedding vectors and stored in a database.
2. **Face Verification**: Verifies new face images by comparing their embeddings with the stored embeddings of a registered user.
3. **Cosine Similarity Metric**: Utilized to measure the similarity between embeddings with a threshold for successful verification.

## Demo
- Example images of user registration and verification attempts are included in the script (`user1.png`, `user2.png`, etc.). Replace these with your own images to test the functionality.

## Required Libraries and Installation
- **DeepFace**: A modern library for facial recognition and analysis.
  - Install with: `pip install deepface`
- **scipy**: Used for cosine similarity calculations.
  - Install with: `pip install scipy`

## How to Run
1. Clone this repository or download the script.
2. Ensure you have the required libraries installed (see above).
3. Prepare the images for registration and verification.
   - Registration images (e.g., `user1.png`, `user2.png`) represent the faces to register.
   - Verification images (e.g., `attempt1.png`, `attempt2.png`) represent faces to verify.
4. Modify the script to point to your image file paths.
5. Run the script to see the registration and verification process in action.

## References
- **DeepFace Documentation**: [https://github.com/serengil/deepface](https://github.com/serengil/deepface)
- Blogs on using DeepFace for facial recognition: [https://blog.kbanknow.com/31](https://blog.kbanknow.com/31)