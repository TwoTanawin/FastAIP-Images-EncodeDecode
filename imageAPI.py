from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import base64
from typing import Optional
import json

app = FastAPI()

def encode_image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_image

@app.post("/upload-image/")
async def upload_image(name: str, description: str, image: UploadFile = File(...)):
    try:
        # Save the uploaded file
        with open(f"images/{image.filename}", "wb") as f:
            f.write(image.file.read())

        # Encode the image to Base64
        encoded_image = encode_image_to_base64(f"images/{image.filename}")

        # Create a dictionary with the image data
        data = {
            "name": name,
            "description": description,
            "image": encoded_image
        }

        # Convert the dictionary to JSON
        json_data = json.dumps(data, indent=2)

        # Save the JSON data to a file
        with open("json/output.json", "w") as json_file:
            json_file.write(json_data)

        return JSONResponse(content={"message": "Done!"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
