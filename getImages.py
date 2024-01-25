import requests
import base64
import numpy as np
import cv2
from datetime import datetime

url = "http://localhost:8000/encode_image"  # Replace with the actual URL where your FastAPI server is running

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    print(" image :", data["image"])
    encoded_image = data["image"]
    decoded_image = base64.b64decode(encoded_image)
    # Convert binary data to a NumPy array
    nparr = np.frombuffer(decoded_image, np.uint8)

    # Decode the NumPy array to an OpenCV image
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save the image using OpenCV
    cv2.imwrite(f"output/decoded_image_{timestamp}.jpg", image)

    print(f"done : {timestamp}")
else:
    print("Error:", response.status_code)
    print(response.json())
