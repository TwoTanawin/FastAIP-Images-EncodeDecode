import json
import base64

# Function to encode an image file to Base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_image

# Example image path
image_path = "output/images/dog.jpg"

# Encode the image to Base64
encoded_image = encode_image_to_base64(image_path)

# Create a dictionary with the image data
data = {
    "name": "Your Item",
    "description": "Some description",
    "image": encoded_image
}

# Convert the dictionary to JSON
json_data = json.dumps(data, indent=2)

# Save the JSON data to a file
with open("json/output.json", "w") as json_file:
    json_file.write(json_data)

print("Done !")
