import json
import base64
import cv2
import numpy as np

# Function to decode Base64-encoded image and save it using OpenCV
def decode_and_save_image(json_file_path, output_image_path):
    # Read JSON file
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    # Extract Base64-encoded image from JSON data
    encoded_image = data.get("image", "")

    # Decode Base64 to binary data
    decoded_image = base64.b64decode(encoded_image)

    # Convert binary data to numpy array
    image_array = np.frombuffer(decoded_image, dtype=np.uint8)

    # Decode image using OpenCV
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Save the decoded image
    cv2.imwrite(output_image_path, image)

# Example usage
json_file_path = "json/output.json"
output_image_path = "output/output_image.jpg"

decode_and_save_image(json_file_path, output_image_path)
