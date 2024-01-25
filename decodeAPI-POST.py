import requests

# Specify the URL of the FastAPI endpoint
url = "http://127.0.0.1:8000/upload-image/"

# Specify query parameters
params = {
    "name": "test-1",
    "description": "home-1",
}

# Specify the path to the image file
image_path = "/app/jsonImages/images/dog.jpg"

# Create a dictionary for the files parameter
files = {"image": open(image_path, "rb")}

# Perform the HTTP POST request with query parameters
response = requests.post(url, params=params, files=files)

# Print the response
print(response.status_code)
print(response.json())
