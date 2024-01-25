from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import base64

app = FastAPI()

@app.get("/encode_image")
async def encode_image():
    image_path = "/app/jsonImages/images/dog.jpg"

    try:
        # Read the contents of the image file
        with open(image_path, "rb") as image_file:
            image_content = image_file.read()

        # Your image encoding logic goes here
        # For example, you can use base64 encoding
        encoded_image = base64.b64encode(image_content).decode()

        # Create a JSON object with the specified structure
        response_data = {
            "name": "home-1",
            "date": datetime.now().isoformat(),
            "image": encoded_image
        }

        # Return the JSON object
        return response_data

    except FileNotFoundError:
        return JSONResponse(content={"error": "Image not found"}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"error": f"An error occurred: {str(e)}"}, status_code=500)
